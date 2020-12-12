<?php
//error_reporting(E_ERROR | E_PARSE);
$input=file_get_contents("12.txt");
$inputs=explode("\n",$input,-1);
$direction=90;
$x=0;
$y=0;
$wax=10;
$way=1;
$di=['N','E','S','W'];
foreach ($inputs as $i) {
	$n=(int)substr($i,1);
	$d=$i[0];
	if ($d=='F') {
		$x+=$n*$wax;
		$y+=$n*$way;
	}
	echo $d;
	switch ($d) {
		case 'L':
			for ($j=$n;$j>0; $j-=90) {
				echo "$j\n";
				$tmp=$way;
				$way=$wax;
				$wax=-1*$tmp;
			}
		break;
		case 'R':
			for ($j=$n;$j>0; $j-=90) {
				echo "$j\n";
				$tmp=$wax;
				$wax=$way;
				$way=-1*$tmp;
			}
		break;
		case 'N':
			$way+=$n;
		break;
		case 'E':
			$wax+=$n;
		break;
		case 'S':
			$way-=$n;
		break;
		case 'W':
			$wax-=$n;
		break;
	}
	echo "$x,$y,($wax,$way)\n";
}
echo $x.",".$y.",".(abs($x)+abs($y))."\n";
//Answer:
?>
