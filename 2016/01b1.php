<?php
error_reporting(E_ERROR | E_PARSE);
$input=file_get_contents("01.txt");
$inputs=explode(", ",$input);
$direction=0; //0 is north
//	0
//3		1
//	2
$x=0;
$y=0;
$locations=[];
foreach ($inputs as $i) {
	if ($i[0] == "L") {
		$direction=($direction+3)%4;
	} else {
		$direction=($direction+1)%4;
	}
	$distance=(int)substr($i,1);
	//echo $direction.", ".$distance."\n";
	switch ($direction) {
		case 0:
			echo 0;
			for ($j=$y; $j < $y+$distance; $j++) {
				$locations[$x][$j]++;
				if ($locations[$x][$j]>1) {
					echo "HQ (".$x.",".$j.")\nDist:".$x+$j."\n";
					var_dump($locations);
					exit("0");
				}
			}
			$y+=$distance;
			break;
		case 1:
			echo 1;
			for ($j=$x; $j < $x+$distance; $j++) {
				$locations[$j][$y]++;
				if ($locations[$j][$y]>1) {
					echo "HQ (".$j.",".$y.")\nDist:".$j+$y."\n";
					var_dump($locations);
					exit("1");
				}
			}
			$x+=$distance;
			break;
		case 2:
			echo 2;
			$y-=$distance;
			for ($j=$y; $j < $y+$distance; $j++) {
				$locations[$x][$j]++;
				if ($locations[$x][$j]>1) {
					echo "HQ (".$x.",".$j.")\nDist:".$x+$j."\n";
					var_dump($locations);
					exit("2");
				}
			}
			break;
		case 3:
			echo 3;
			$x-=$distance;
			for ($j=$x; $j < $x+$distance; $j++) {
				$locations[$j][$y]++;
				if ($locations[$j][$y]>1) {
					echo "HQ (".$j.",".$y.")\nDist:".$j+$y."\n";
					var_dump($locations);
					exit("3");
				}
			}
			break;
	}

	//echo "(".$x.",".$y.")\n";
}
//var_dump($locations);
//echo $x+$y."\n";
//Answer:
?>
