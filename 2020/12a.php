<?php
//error_reporting(E_ERROR | E_PARSE);
$input=file_get_contents("12.txt");
$inputs=explode("\n",$input,-1);
$direction=90;
$x=0;
$y=0;
$di=['N','E','S','W'];
foreach ($inputs as $i) {
	$n=(int)substr($i,1);
	$d=$i[0];
	if ($d=='F') {
		$d=$di[$direction/90];
	}
	echo $d;
	switch ($d) {
		case 'L':
			$direction=($direction-$n+360)%360;
		break;
		case 'R':
			$direction=($direction+$n)%360;
		break;
		case 'N':
			$y+=$n;
		break;
		case 'E':
			$x+=$n;
		break;
		case 'S':
			$y-=$n;
		break;
		case 'W':
			$x-=$n;
		break;
	}
	echo "$direction\n";
}
echo $x.",".$y.",".(abs($x)+abs($y))."\n";
//Answer:
?>
