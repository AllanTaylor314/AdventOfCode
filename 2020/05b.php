<?php
error_reporting(E_ERROR | E_PARSE);
$input=file_get_contents("5.txt");
$inputs=explode("\n",$input,-1);
$seats=array_fill(0,1024,1);
var_dump($seats);
foreach ($inputs as $i) {
	$bin=bindec('0b'.str_replace(["F","B","L","R"],[0,1,0,1],$i));
	//echo $bin."\n";
	unset($seats[$bin]);
	//if ($bin>$out) {
	//	$out=$bin;
	//}
}
var_dump($seats);
//Then just scroll through the output to find the missing seat
//echo $out."\n";
//Answer: 579
?>
