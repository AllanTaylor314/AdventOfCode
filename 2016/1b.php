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
$xo=0;
$yo=0;
$locations=[];
foreach ($inputs as $i) {
	if ($i[0] == "L") {
		$direction=($direction+3)%4;
	} else {
		$direction=($direction+1)%4;
	}
	$distance=(int)substr($i,1);
	//echo $direction.", ".$distance."\n";
	$yo=$y;
	$xo=$x;
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
	if ($direction%2==0) { //N/S i.e. y
		for ($j=($y>$yo?$yo:$y)+1; $j < ($y<$yo?$yo:$y); $j++) {
			//echo "y".$j."\n";
			echo "(".$x.",".$j.")\n";
			$locations[$x][$j]++;
			if ($locations[$x][$j]>1) {
				//var_dump($locations);
				echo "HQ (".$x.",".$j.") - ".(abs($x)+abs($j))."\n";
				exit();
			}
		}
	} else {
		for ($j=($x>$xo?$xo:$x)+1; $j < ($x<$xo?$xo:$x); $j++) {
			//echo "x".$j."\n";
			echo "(".$j.",".$y.")\n";
			$locations[$j][$y]++;
			if ($locations[$j][$y]>1) {
				//var_dump($locations);
				echo "HQ (".$j.",".$y.") - ".(abs($j)+abs($y))."\n";
				exit();
			}
		}
	}
	echo "(".$x.",".$y.")+\n";
}
//var_dump($locations);
//echo $x+$y."\n";
//Answer:
?>
