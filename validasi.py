import sys
import xmlrpc.client
import datetime

class Odoo():
    def __init__(self):
        """
            Create
            Read
            Update
            Delete
        """
        self.DATA = "rekap-duit" # db name
        self.USER = "abdurrasyid.azhar@gmail.com" # email address
        self.PASS = "odoo123" # password
        # self.PORT = "" # port
        self.URL  = "https://rekap-duit.odoo.com" # base url
        self.URL_COMMON = "{}/xmlrpc/2/common".format(
            self.URL)
        self.URL_OBJECT = "{}/xmlrpc/2/object".format(
            self.URL)

    def authenticateOdoo(self):
        self.ODOO_COMMON = xmlrpc.client.ServerProxy(self.URL_COMMON)
        self.ODOO_OBJECT = xmlrpc.client.ServerProxy(self.URL_OBJECT)
        self.UID = self.ODOO_COMMON.authenticate(
            self.DATA
            , self.USER
            , self.PASS
            , {})

    def userCheckEmail(self, email) :
        odoo_filter = [[("x_studio_email", "=", email)]]
        result_id = self.ODOO_OBJECT.execute_kw(
            self.DATA
            , self.UID
            , self.PASS
            , 'x_username'
            , 'search'
            , odoo_filter
        )
        try:
            return result_id[0]
        except IndexError as e:
            pass

    def userCheckPassword(self, password) :
        odoo_filter = [[("x_studio_password", "=", password)]]
        result_id = self.ODOO_OBJECT.execute_kw(
            self.DATA
            , self.UID
            , self.PASS
            , 'x_username'
            , 'search'
            , odoo_filter
        )
        try:
            return result_id[0]
        except IndexError as e:
            pass

    def validateLogin(self, email, password) :
        return (self.userCheckEmail(email) == self.userCheckPassword(password))

    

email = sys.argv[1]
password = sys.argv[2]

od = Odoo()
od.authenticateOdoo()

if(od.validateLogin(email, password)):
    if(email=="abcd@abcd.com"):
        print("pegawai")
    elif(email=="joker@joker.com"):
        print("pengawas")
    elif(email=="bro@bro.com"):
        print("finance")
    else:
        print("role error")
else:
    print("login error")