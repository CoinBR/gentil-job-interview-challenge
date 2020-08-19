from os import getenv
from time import sleep
import xmlrpc.client
from flask import Flask, jsonify

# connection info
url = 'http://odoo:8069'
db = 'challenge'
username = 'coinbr@gmail.com'
password = 'senha'


def get_error_msg(msg, e=''):
    return """
-------------------------------------
[ERROR!] [API-POC]: {}
-------------------------------------
odoo: {}
db: {}
username: {} 
password: {}
-------------------------------------
{}
        """.format(msg, url, db, username, '*' * len(password), e)

# public endpoints
common = xmlrpc.client.ServerProxy('{}/xmlrpc/2/common'.format(url))

# test connection
able_to_connect = False
while not able_to_connect:
    try:
        common.version()
        print("API-POC was able to connect to to odoo")
        able_to_connect = True
    except Exception as e:
        print(get_error_msg("A connection to the odoo api could not be estabilished", e))
        sleep(3)

# authenticate
try:
    uid = common.authenticate(db, username, password, {})
except Exception as e:
    raise RuntimeError(get_error_msg("Could not authenticate to odoo's api", e))

def rpc(*args):
    try:
        models = xmlrpc.client.ServerProxy('{}/xmlrpc/2/object'.format(url))    
        return models.execute_kw(db, uid, password, *args) 
    except Exception as e:
        raise RuntimeError("""
----------------------------
API RPC Call failed.
*args: {}
----------------------------
{}
----------------------------
        """.format([*args], e))

##########################################
# Actual API Calls:



app = Flask(__name__)

@app.route('/', methods=['GET'])
def parented_partners():
    try:
        parentedPartnersIds = rpc('res.partner',
                                    'search', 
                                    [[[ 'mother_name', '!=', False ]]]
                                    )

        partnersAndTheirMothers = rpc('res.partner',
                                        'read',
                                        [parentedPartnersIds],
                                        {'fields': ['name', 'mother_name']}
                                        )
        return jsonify(partnersAndTheirMothers)

    except Exception as e:
        return jsonify({
            "error": get_error_msg("Unable to get ParentedPartners and their mothers info.", e)
        }), 500
