<?php
header('Content-Type: text/plain');
include("3in.php");
$used_squares = [];
foreach ($a as $c) {
	$x = $c['x'];
	$y = $c['y'];
	for ($i = $c["w"]; $i > 0; $i--) {
		for ($j = $c["h"]; $j > 0; $j--) {
			if (isset($used_squares[$i + $x][$j + $y])) {
				$used_squares[$i + $x][$j + $y] = 1;
			} else {
				$used_squares[$i + $x][$j + $y] = 0;
			}
		}
	}
}
//var_dump($used_squares);
$total = 0;
foreach ($used_squares as $subarray) {
	foreach ($subarray as $square) {
		$total += $square;
	}
}
echo $total;
