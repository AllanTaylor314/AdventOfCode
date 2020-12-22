<?php
//error_reporting(E_ERROR | E_PARSE);
$input=file_get_contents("22.txt");
$inputs=explode("\n\n",$input."\n",-1);
$p1=explode("\n",$inputs[0]);
$p2=explode("\n",$inputs[1]);
array_shift($p1);
array_shift($p2);
while (count($p1)>0 && count($p2)>0) {
	$c1=array_shift($p1);
	$c2=array_shift($p2);
	if ($c1>$c2) {
		array_push($p1,$c1,$c2);
	} else {
		array_push($p2,$c2,$c1);
	}
	//var_dump($p1);
}
if (count($p1)==0) {$winner=$p2;}
else {$winner=$p1;}
$winner[]=0;
$answer=0;
$winner=array_reverse($winner);
var_dump($winner);
foreach ($winner as $key => $value) {
	$answer+=($key*$value);
}
echo "$answer\n";
//Answer:
?>
