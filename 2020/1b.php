<?php
error_reporting(E_ERROR | E_PARSE);
$input=file_get_contents("1.txt");
$inputs=explode("\r\n",$input,-1); //-1 to remove empty last
foreach ($inputs as $i) {
	foreach ($inputs as $j) {
		foreach ($inputs as $k) {
		if ((int)$i+(int)$j+(int)$k==2020) {
			echo $i.",".$j.",".$k.",";
			echo (int)$i*(int)$j*(int)$k;
			exit();
		}
	}
	}
}
//Answer:274879808
?>
