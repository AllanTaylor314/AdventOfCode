<?php
header('Content-Type: text/plain');
include('6in.php');
$inputs = explode("\n",$input);
$coords = [];
foreach ($inputs as $i => $in) {
	$coords[$i] = explode(", ",$in);
}
//var_dump($coords);
//$xyofpts = [];
//var_dump($fabric);
//foreach ($coords as $k => $c) {
//	$xyofpts[$c[0]][$c[1]] = $k;
//}
//$xyofpts[$k]['x'] = $coords[$k][0];
//$xyofpts[$k]['y'] = $coords[$k][1];
$infinite = [];
$distance = 0;
$fabric = array_fill(0, 400, array_fill(0, 400, array_fill(0, 50, 0)));
foreach ($fabric as $x => $xa) {
	foreach ($xa as $y => $ya) {
		foreach ($ya as $id => $d) {
			$fabric[$x][$y][$id] = abs($x-$coords[$id][0]) + abs($y-$coords[$id][1]);
		}
	}
}
var_dump($fabric);
//print_r($fabric);
