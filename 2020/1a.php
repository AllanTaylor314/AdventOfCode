<?php
$input=file_get_contents("1.txt");
$inputs=explode("\r\n",$input,-1);
foreach ($inputs as $i) {
	foreach ($inputs as $j) {
		if ($i+$j==2020) {
			echo $i*$j;
			exit();
		}
	}
}
//Answer:436404
?>
