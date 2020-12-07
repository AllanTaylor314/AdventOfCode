<?php
header('Content-Type: text/plain');
include("3in.php");
$used_squares = [];
foreach ($a as $k => $c) {
	$x = $c['x'];
	$y = $c['y'];
	$uniq = true;
	for ($i = $c["w"]; $i > 0; $i--) {
		for ($j = $c["h"]; $j > 0; $j--) {
			if (isset($used_squares[$i + $x][$j + $y])) {
				$used_squares[$i + $x][$j + $y] = 1;
				$uniq = false;
			} else {
				$used_squares[$i + $x][$j + $y] = 0;
			}
		}
	}
	if ($uniq) {
//		echo $k."\n";
		$answer=$k;
	}
}
//var_dump($used_squares);
$total = 0;
foreach ($used_squares as $subarray) {
	foreach ($subarray as $square) {
		$total += $square;
	}
}
//echo "\n".$answer;

foreach ($a as $k => $c) {
        $x = $c['x'];
        $y = $c['y'];
        $unique = true;
        for ($i = $c["w"]; $i > 0; $i--) {
                for ($j = $c["h"]; $j > 0; $j--) {
                        if (($used_squares[$i + $x][$j + $y]) == 1) {
                                $unique = false;
                        }
                }
        }
        if ($unique) {
                echo $k."\n";
                //$answer=$k;
        }
}
