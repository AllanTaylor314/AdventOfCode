<?php
error_reporting(E_ERROR | E_PARSE);
$input="ckczppom";
$i=0;
while (1) {
	$i++;
	if (substr(md5($input.$i),0,5)==="00000") {
		echo $i."\n";
		exit();
	}
}
//Answer:
?>
