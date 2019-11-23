<?php 
  
if (isset($_POST['submit'])) { 
    $nama_barang = $_POST['nama_barang'];
    $jumlah = $_POST['jumlah'];
    $harga = $_POST['harga'];
    $keterangan = $_POST['keterangan'];

    $output = shell_exec("python odoo_income.py $nama_barang $jumlah $harga $keterangan");
    header("Location: home_pegawai.php");
} 

?> 