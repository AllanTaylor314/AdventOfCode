<?php
error_reporting(E_ERROR | E_PARSE);
$input=file_get_contents("7.txt");
$inputs=explode("\n",$input,-1);
$sensors=[];
//var_dump($sensors);
/*
	AND         &
	OR          |
	XOR         ^
	NOT         ~
	LSHIFT      <<
	RSHIFT      >>
*/
$prevsensors=[1,2,3];
while ($sensors != $prevsensors) {
	$prevsensors=$sensors;
foreach ($inputs as $i) {
	$j=explode(" -> ",$i);
	$k=explode(" ",$j[0]);
	$a=preg_match('/[0-9]/',$k[0])?(int)$k[0]:(int)$sensors[$k[0]];
	$b=preg_match('/[0-9]/',$k[2])?(int)$k[2]:(int)$sensors[$k[2]];
	$c=preg_match('/[0-9]/',$k[1])?(int)$k[1]:(int)$sensors[$k[1]];
	//echo count($k).";".$a.",".$k[1].",".$b.":".$j[1]."\n";
	switch (count($k)) {
		case 1: //one value is either a number or a reference
			$sensors[$j[1]]=$a;
			break;
		case 2:
			$sensors[$j[1]]= $c^0xFFFF;
			break;
		case 3:
			switch ($k[1]) {
				case "AND":
					$sensors[$j[1]]=($a & $b) & 0xFFFF;
					break;
				case "OR":
					$sensors[$j[1]]=($a | $b) & 0xFFFF;
					break;
				case "LSHIFT":
					$sensors[$j[1]]=($a << $b) & 0xFFFF;
					break;
				case "RSHIFT":
					$sensors[$j[1]]=($a >> $b) & 0xFFFF;
					break;
			}
	}
}
//var_dump($sensors);
//break;
//sleep(1);
echo $sensors["a"]."\n";
}
//Answer: 3176
?>
