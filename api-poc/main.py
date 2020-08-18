from os import getenv
import xmlrpc.client

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
try:
    common.version()
except Exception as e:
    raise RuntimeError(get_error_msg("A connection to the odoo api could not be estabilished", e))

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

print(rpc('res.partner', 'search', [[[ 'mother_name', '!=', False ]]]))