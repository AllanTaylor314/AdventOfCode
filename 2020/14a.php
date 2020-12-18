<?php
//error_reporting(E_ERROR | E_PARSE);
$input=file_get_contents("14.txt");
$inputs=explode("\n",$input,-1);
$steps=[];
$mem=[];
foreach ($inputs as $i) {
	if ($i[1]=="a") { //as in MaSK
		$mask=str_replace("mask = ","",$i);
	} else {
		$parsed=explode("] = ",str_replace("mem[","",$i));
		$mem[$parsed[0]]=apply_mask((int)$parsed[1],$mask);
	}
}
/*/
foreach ($steps as $key => $step) {
	$mask=array_shift($step);
	foreach ($step as $instruction) {
		$parsed=explode("] = ",str_replace("mem[","",$instruction));
		var_dump($parsed);
	}
}//*/
echo array_sum($mem)."\n";
var_dump($mem);
//var_dump($mem);
//Answer:
function apply_mask($init,$mask)
{
	//echo "$mask\n";
	$bin=sprintf( "%036b",$init);
	//var_dump($bin);
	foreach (str_split($mask) as $index => $m) {
		if ($m=="X") {
			// Do nothing
		} else {
			$bin[$index]=$m;
		}
	}
	//var_dump($mask);
	//var_dump($bin);
	return bindec($bin);
}
?>
