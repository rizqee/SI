<?php 
  
if (isset($_POST['submit'])) { 
    $pengirim = $_POST['nama_pengirim'];
    $proyek = $_POST['nama_proyek'];
    $pendapatan = $_POST['pendapatan'];
    $waktu_start = $_POST['waktu_proyek_start'];
    $waktu_finish = $_POST['waktu_proyek_finish'];
    $keterangan = $_POST['keterangan'];

    $output = shell_exec("python odoo_income.py $pengirim $proyek $pendapatan $waktu_start $waktu_finish $keterangan");
    $array_output = explode(",", $output);
    foreach ($array_output as $key => $value) {
        parse_str($value, $parsed);
        print_r($parsed);
        echo "\n";
    }
    // echo $array_output;
    // parse_str($output, $parsed);
    // print_r($parsed);
    // echo($output);
    // print_r($output);
    // echo($output);
    // if($output == "pegawai\n"){
    //     header("Location: home_pegawai.html");
    // }else if($output == "pengawas\n"){
    //     header("Location: home_pengawas.html");
    // }else if($output == "finance-officer\n"){
    //     header("Location: Reimburse.html");
    // }else if($output == "login error\n"){
    //     echo("login error");
    // }else if($output == "role error\n"){
    //     echo("role error");
    // }
} 

?> 