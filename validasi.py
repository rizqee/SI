import sys
import xmlrpc.client
import datetime
import odoo
    
email = sys.argv[1]
password = sys.argv[2]

od = odoo.Odoo()
od.authenticateOdoo()

if(od.validateLogin(email, password)):
    print(od.getEmployeeType(email, password))
else:
    print("login error")