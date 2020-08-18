from os import getenv
import xmlrpc.client

# connection info
url = 'http://odoo:8069'
db = 'challenge'
username = 'coinbr@gmail.com'
password = 'senha'

# public endpoints
common = xmlrpc.client.ServerProxy('{}/xmlrpc/2/common'.format(url))

# test connection
try:
    common.version()
except Exception as e:
    raise RuntimeError("""ERROR: A connection to the odoo api could not be estabilished
    odoo url = {}
    db = {}
    username = {} 
    -------------------------------------
    {}
    """.format(url, db, username, e)) 

