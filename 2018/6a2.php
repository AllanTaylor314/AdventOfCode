<?php
header('Content-Type: text/plain');
include('6in.php');
$inputs = explode("\n",$input);
foreach ($inputs as $id => $in) {
	$xord[$id] = (int)(explode(", ",$in)[0]);
	$yord[$id] = (int)(explode(", ",$in)[1]);
}
$top    = min($yord);
$bottom = max($yord);
$left   = min($xord);
$right  = max($xord);
$count  = array_fill(0,50,0);
function isFinite($x, $y) {
	return ($GLOBALS['left'] < $x && $x < $GLOBALS['right']) && ($GLOBALS['top'] < $y && $y < $GLOBALS['bottom']);
}
function not_tied($array_in) {
	$working = $array_in;
	asort($working);
	return $working[0] != $working[1];
}
function keyofmin($array_in) {
	//echo array_keys($array_in, min($array_in))[0];
	return array_keys($array_in, min($array_in))[0];
}
for ($i = $left; $i < $right+1; $i++) {
	for ($j = $top; $j < $bottom+1; $j++) {
		$distances = [];
		foreach ($xord as $id => $x) {
			$y = $yord[$id];
			$distances[$id] = abs($x - $i) + abs($y - $j);
		}
		if (not_tied($distances)) {
			$count[keyofmin($distances)]++;
		}
	}
}
$maxarea = 0;
foreach ($xord as $id => $x) {
	$y = $yord[$id];
	if (isFinite($x, $y) && $count[$id] > $maxarea) {
		$maxarea = $count[$id];
	}
}
echo $maxarea;
//PART 2
$count2 = 0;
for ($i = $left; $i < $right+1; $i++) {
	for ($j = $top; $j < $bottom+1; $j++) {
		$distances = [];
		foreach ($xord as $id => $x) {
			$y = $yord[$id];
			$distances[$id] = abs($x - $i) + abs($y - $j);
		}
		if (array_sum($distances) < 10000) {
			$count2++;
		}
	}
}
echo "\n".$count2;
