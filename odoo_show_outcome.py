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

od = Odoo()
od.authenticateOdoo()

output=""
for i in range(1,100) :
    row = (od.expenseRead(i))
    if (len(row)!=0):
        output += "nama_barang="
        output += (row[0]["x_studio_nama_barang"]) + "&"
        output += "jumlah="
        output += (str(row[0]["x_studio_jumlah"])) +"&"
        output += "harga="
        output += str((row[0]["x_studio_harga_1"])) + "&"
        output += "id_pegawai="
        output += (str(row[0]["x_studio_id_pegawai_1"])) + "&"
        output += "status_reimburse="
        output += str((row[0]["x_studio_status_reimburse"])) + "&"
        output += "keterangan="
        output += (row[0]["x_name"]) + ","
        
print(output)   