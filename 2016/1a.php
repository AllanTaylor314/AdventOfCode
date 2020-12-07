<?php
error_reporting(E_ERROR | E_PARSE);
$input=file_get_contents("1.txt");
$inputs=explode(", ",$input);
$direction=0; //0 is north
//	0
//3		1
//	2
$x=0;
$y=0;
foreach ($inputs as $i) {
	if ($i[0] == "L") {
		$direction=($direction+3)%4;
	} else {
		$direction=($direction+1)%4;
	}
	$distance=(int)substr($i,1);
	echo $direction.", ".$distance."\n";
	switch ($direction) {
		case 0:
			$y+=$distance;
			break;
		case 1:
			$x+=$distance;
			break;
		case 2:
			$y-=$distance;
			break;
		case 3:
			$x-=$distance;
			break;
	}
	echo "(".$x.",".$y.")\n";
}
echo $x+$y."\n";
//Answer:
?>
