<?php 

    $output = shell_exec("python odoo_show_income.py");
    $array_output = explode(",", $output);
    foreach ($array_output as $key => $value) {
        parse_str($value, $parsed);
        print_r($parsed);
    }

    echo '<tr>';
    echo '<td>'. $row['id'] .'</td>';
    echo '<td>'. $row['firstname'] .'</td>';
    echo '<td>'. $row['email'] .'</td>';
    echo '</tr>';
} 

?> 