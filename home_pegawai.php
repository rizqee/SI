<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="utf-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <meta http-equiv="X-UA-Compatible" content="ie=edge" />

    <title>Home</title>

    <link rel="stylesheet" href="homestyle.css" />
    <script src="home_ct.js"></script>
  </head>

  <body>
    <div class = "container">
        <div class = "navbar">
            RekapDuit
            <button type="button" name="logout" onclick="logout()">LOGOUT</button>
        </div>
        <div class = "content">
            <div class="table">
                <table class="main_table">
                    <tr>
                        <th>No.</th>
                        <th>Nama Barang</th>
                        <th>Jumlah</th>
                        <th>Harga</th>
                        <th>Total</th>
                        <th>Rincian</th>
                        <th>Bukti Pembayaran</th>
                        <th>Keterangan</th>
                    </tr>
                    <?php
                        $output = shell_exec("python odoo_show_outcome.py");
                        //echo $output;
                        $array_output = explode(",", $output);
                        //echo $array_output;
                        $x=1;
                        foreach ($array_output as $key => $value) {
                            if ($x<count($array_output)){
                                parse_str($value, $parsed);
                                $total = $parsed['harga'] * $parsed['jumlah'];
                                echo '<tr>';
                                echo '<td>'.$x.'</td>';
                                echo '<td>'. $parsed['nama_barang'] .'</td>';
                                echo '<td>'. $parsed['jumlah'] .'</td>';
                                echo '<td>'. $parsed['harga'] .'</td>';
                                echo '<td>'. $total .'</td>';
                                echo '<td class="rincian"><button class="button rincian">Rincian</button></td>';
                                echo '<td class="bukti pembayaran"><button class="bukti pembayaran">Lihat Bukti</button></td>';
                                echo '<td>'. $parsed['keterangan'] .'</td>';
                                echo '</tr>';
                                $x++;
                            }
                        }
                    ?>
                </table>
            </div>
            <div class="Button" >
                    <button type="button" name = "add" onclick="add_expense()">Add</button>
                    <div class="divider"></div>
                    <button type="button" name = "delete">Delete</button>
            </div>
        </div>
    </div>

  </body>
</html>