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

    def expenseReadByIdPegawai(self, id_pegawai):
        odoo_filter = [[["x_studio_id_pegawai_1", "=", id_pegawai]]]
        id_pengeluaran = self.ODOO_OBJECT.execute_kw(
            self.DATA
            , self.UID
            , self.PASS
            , 'x_keterangan' 
            , 'search'
            , odoo_filter)

        return (self.expenseRead(id_pengeluaran))
        
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
      
    def expenseAdd(self, expenseRow):
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

    def validateLogin(self, email, password) :
        odoo_filter = [[("x_studio_email", "=", email), ("x_studio_password", "=", password)]]
        result = self.ODOO_OBJECT.execute_kw(
            self.DATA
            , self.UID
            , self.PASS
            , 'x_username'
            , 'search'
            , odoo_filter
        )
        return bool(result)

    def getEmployeeType(self, email, password) :
        email_password_filter = [[("x_studio_email", "=", email), ("x_studio_password", "=", password)]]
        id = self.ODOO_OBJECT.execute_kw(
            self.DATA
            , self.UID
            , self.PASS
            , 'x_username'
            , 'search'
            , email_password_filter
        )
        # id_filter = [[("id", "=", id[0])]]
        emp_type = self.ODOO_OBJECT.execute_kw(
            self.DATA
            , self.UID
            , self.PASS
            , 'x_username'
            , 'read'
            , [id]
            , {"fields": ["x_studio_emp_type"]}
        )
        return emp_type[0]["x_studio_emp_type"]

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
    print(od.expenseAdd(expenses_row))
    od.expensesUpdateStatus(1);
    print(od.expenseReadByIdPegawai(2))
    print(od.expenseRead(1))

    email = "abcd@abcd.com"
    password = "abcd"
    print(od.validateLogin(email,password))
    print(od.validateLogin("abcd@abcd.com", "abcd"))
    print(od.getEmployeeType(email,password))

 
if __name__ == '__main__':
    main()