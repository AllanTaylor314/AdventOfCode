<?php
$input=file_get_contents("1.txt");
$inputs=str_split($input);
//echo substr_count($input,"(")-substr_count($input,")");
$n=0;
foreach($inputs as  $key => $i) {
	if ($i=="(") {
		$n++;
	} elseif ($i==")") {
		$n--;
	}
	if ($n==-1) {
		echo $key+1;
		exit();
	}
}
?>
