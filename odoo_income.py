import xmlrpc.client
import datetime
import sys
import random
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
            , {"fields": ["x_name", "x_studio_id_sender", "x_studio_project_name", "x_studio_earnings", "x_studio_date", "x_studio_date_finish_1", "x_studio_field_wtFYA"]})
        return result


def main():
    pengirim = sys.argv[1]
    proyek = sys.argv[2]
    pendapatan = sys.argv[3]
    waktu_awal = sys.argv[4]
    waktu_akhir = sys.argv[5]
    keterangan = sys.argv[6]

    od = Odoo()
    od.authenticateOdoo()

    id_sender = random.randint(1,100)

    income_row = [{"x_name": pengirim
                        , "x_studio_id_sender": id_sender
                        , "x_studio_project_name": proyek
                        , "x_studio_earnings": pendapatan
                        , "x_studio_date": waktu_awal
                        , "x_studio_date_finish_1": waktu_akhir
                        , "x_studio_field_wtFYA":keterangan}]
    income_id = od.incomeAdd(income_row)


if __name__ == '__main__':
    main()