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

    def incomeAdd(self, incomeRow):
        income_id = self.ODOO_OBJECT.execute_kw(
            self.DATA
            , self.UID
            , self.PASS
            , 'x_income'
            , 'create'
            , incomeRow)
        return income_id

    def incomeRead(self, income_id):
        odoo_filter = [[("id", "=", income_id)]]
        result = self.ODOO_OBJECT.execute_kw(
            self.DATA
            , self.UID
            , self.PASS
            , 'x_income'
            , 'read'
            , [income_id]
            , {"fields": ["x_name", "x_studio_id_sender", "x_studio_project_name", "x_studio_earnings", "x_studio_date", "x_studio_field_wtFYA"]})
        return result


def main():
    od = Odoo()
    od.authenticateOdoo()

    # income_row = [{"x_name":"PT Apa aja"
    #                     , "x_studio_id_sender":2
    #                     , "x_studio_project_name":"Hompimpah"
    #                     , "x_studio_earnings":157689045
    #                     , "x_studio_date":"12/04/2020 - 12/9/2020"
    #                     , "x_studio_field_wtFYA":"waaaw"}]
    # print(od.incomeAdd(income_row))
    for i in range(1,10) :
        print(od.incomeRead(i))


if __name__ == '__main__':
    main()