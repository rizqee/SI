<!DOCTYPE html>
<html>
<head>
    <title>Income</title>
    <meta name="viewport" content="width=device-width, initial-scale=1.0"> 
	<link rel="stylesheet" href="style_reimburse_income.css">
</head>

<body>
    <div class="navbar"> 
        <p class="Title">RekapDuit</p>
        <button class="btnreimburse">Reimburse</button>
        <button class="btnpemasukan">Pemasukan</button>
        <button class="btn_logout">Logout</button>
        <p class="logged_in_as">Logged in as Finance Officer</p>
    </div>

    <div class="main_container" id="container_income">
        <table class="main_table">
            <tr>
                <th>No.</th>
                <th>Nama Pengirim</th>
                <th>Nama Proyek</th>
                <th>Pendapatan</th>
                <th>Waktu Mulai Proyek</th>
                <th>Waktu Akhir Proyek</th>
                <th>Rincian</th>
                <th>Keterangan</th>
            </tr>
            <?php 
                $output = shell_exec("python odoo_show_income.py");
                $array_output = explode(",", $output);
                $x=1;
                foreach ($array_output as $key => $value) {
                    if ($x<count($array_output)){
                        parse_str($value, $parsed);
                        echo '<tr>';
                        echo '<td>'.$x.'</td>';
                        echo '<td>'. $parsed['nama_pengirim'] .'</td>';
                        echo '<td>'. $parsed['nama_proyek'] .'</td>';
                        echo '<td>'. $parsed['pendapatan'] .'</td>';
                        echo '<td>'. $parsed['waktu_proyek_start'] .'</td>';
                        echo '<td>'. $parsed['waktu_proyek_finish'] .'</td>';
                        echo '<td class="rincian"><button class="button rincian">Rincian</button></td>';
                        echo '<td>'. $parsed['keterangan'] .'</td>';
                        echo '</tr>';
                        $x++;
                    }
                }
            ?>
        </table>

        <a href="input_pendapatan.html"><button  class="float">+
        </button></a>
    </div>

</body>
</html>