<?php 
  
if (isset($_POST['submit'])) { 
    $email = $_POST['email'];
    $psw = $_POST['psw'];
    
    $output = shell_exec("python validasi.py $email $psw");
    if($output == "pegawai\n"){
        header("Location: home_pegawai.html");
    }else if($output == "pengawas\n"){
        header("Location: home_pengawas.html");
    }else if($output == "finance-officer\n"){
        header("Location: Pendapatan_page.php");
    }else if($output == "login error\n"){
        echo("login error");
    }else if($output == "role error\n"){
        echo("role error");
    }
} 

?> 