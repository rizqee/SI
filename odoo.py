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
    def expensesAdd(self, expenseRow):
        expense_id = self.ODOO_OBJECT.execute_kw(
            self.DATA
            , self.UID
            , self.PASS
            , 'hr.expense'
            , 'create'
            , expenseRow)
        return expense_id
    def partnerCheck(self, partnerName):
        odoo_filter = [[("name", "=", partnerName)]]
        partner_id = self.ODOO_OBJECT.execute_kw(
            self.DATA
            , self.UID
            , self.PASS
            , 'res.partner'
            , 'search'
            , odoo_filter)
        return partner_id[0]

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

    def expenseRead(self, expense_id):
        odoo_filter = [[("id", "=", expense_id)]]
        result = self.ODOO_OBJECT.execute_kw(
            self.DATA
            , self.UID
            , self.PASS
            , 'hr.expense'
            , 'read'
            , [expense_id]
            , {"fields": ["product_id", "unit_amount", "quantity", "total_amount", "reference", "employee_id", "payment_mode"]})
        return result
 
    def validateLogin(self, user_id):
        odoo_filter = [[("id", "=", user_id)]]
        result = self.ODOO_OBJECT.execute_kw(
            self.DATA
            , self.UID
            , self.PASS
            , 'x_username'
            , 'read'
            , [user_id]
            , {"fields": ["x_name", "x_studio_email", "x_studio_password"]})
        return result

    def partnerUpdate(self, partner_id, odoo_filter):
        update_result = self.ODOO_OBJECT.execute_kw(
            self.DATA
            , self.UID
            , self.PASS
            , 'res.partner'
            , 'write'
            , [partner_id, odoo_filter])
        return update_result
    def partnerDelete(self, partner_id):
        delete_result = self.ODOO_OBJECT.execute_kw(
            self.DATA
            , self.UID
            , self.PASS
            , 'res.partner'
            , 'unlink'
            , [partner_id])
        return delete_result
 
def main():
    od = Odoo()
    od.authenticateOdoo()
    print(od.UID)
    # Examples:
 
    # CREATE
    # expenses_row = [{"name":"testbrooooo"
    #                     , "product_id":2
    #                     , "unit_amount":44.0
    #                     , "quantity":55.0
    #                     , "reference":False
    #                     , "employee_id":1
    #                     , "payment_mode":'own_account'}]
    # od.expensesAdd(expenses_row)
    # print(od.expensesAdd(expenses_row))

    # print(od.DATA)
    # print(od)

    # uuid = None
    # print(od.checkUID("abcd@abcd.com", "abcd"))

    for i in range(1,12) :
      print(od.validateLogin(i))
    print(od.userCheckEmail("abcd@abcd.com"))

    # # SEARCH
    # partner_id = od.partnerCheck("HLX")
    # print(partner_id)
 
    # # READ
    # result = od.expenseRead(2)
    # print(result)
 
    # # UPDATE
    # odoo_filter = [{"email":"info@hlx.co", "street":"2628 east 18th street"}]
    # result = od.partnerUpdate(partner_id, odoo_filter)
    # print(result)
 
    # # DELETE
    # result = od.partnerDelete(partner_id)
    # print(result)
 
if __name__ == '__main__':
    main()