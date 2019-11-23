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

    def expenseRead(self, id_pengeluaran):
        result = self.ODOO_OBJECT.execute_kw(
            self.DATA
            , self.UID
            , self.PASS
            , 'x_keterangan'
            , 'read'
            , [id_pengeluaran]
            , {"fields": ["x_name", "x_studio_nama_barang", "x_studio_jumlah", "x_studio_harga_1", "x_studio_id_pegawai_1", "x_studio_status_reimburse"]})
        return result
    
    def expenseReadByIdPegawai(self, id_pegawai):
        odoo_filter = [[["x_studio_id_pegawai_1", "=", id_pegawai]]]
        id_pengeluaran = self.ODOO_OBJECT.execute_kw(
            self.DATA
            , self.UID
            , self.PASS
            , 'x_keterangan' 
            , 'search'
            , odoo_filter)
        
        result = self.ODOO_OBJECT.execute_kw(
            self.DATA
            , self.UID
            , self.PASS
            , 'x_keterangan'
            , 'read'
            , [id_pengeluaran]
            , {"fields": ["x_name", "x_studio_nama_barang", "x_studio_jumlah", "x_studio_harga_1", "x_studio_id_pegawai_1", "x_studio_status_reimburse"]})
        return result
        
    def expensesAdd(self, expenseRow):
        expense_id = self.ODOO_OBJECT.execute_kw(
            self.DATA
            , self.UID
            , self.PASS
            , 'x_keterangan'
            , 'create'
            , expenseRow)
        return expense_id

    def expensesUpdateStatus(self, id_pengeluaran):
        update_result = self.ODOO_OBJECT.execute_kw(
            self.DATA
            , self.UID
            , self.PASS
            , 'x_keterangan'
            , 'write'
            , [[id_pengeluaran], {"x_studio_status_reimburse": True}])
        return update_result

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
    expenses_row = [{
            "x_name" : "ini adalah field keterangan",
            "x_studio_nama_barang" : "added barang",
            "x_studio_jumlah" : 100,
            "x_studio_harga_1" : 50000,
            "x_studio_id_pegawai_1" : 2,
        }]
    print(od.expensesAdd(expenses_row))
    # print(od.expensesAdd(expenses_row))
    od.expensesUpdateStatus(1);
    # print(od.DATA)
    # print(od)

    # uuid = None
    # print(od.checkUID("abcd@abcd.com", "abcd"))

    # for i in range(1,12) :
    #   print(od.validateLogin(i))
    # print(od.userCheckEmail("abcd@abcd.com"))
    print(od.expenseReadByIdPegawai(2))
    print(od.expenseRead(1))

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