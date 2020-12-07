<?php
header('Content-Type: text/plain');
include("3in.php");
//var_dump($inputs);
//$delim = [' @ ',',',': ','x'];
$delim = "/[@,:x]/";
//var_dump($a);
$fabric = array_fill(0, 1000, array_fill(0, 1000, 0));
//var_dump($fabric);
foreach ($a as $c => $i) {
//	$fabric[$i["x"]][$i["y"]] = $i;
	$fabric[$i["x"]][$i["y"]] = 1;
	for ($xp = $i["w"]; $xp != 0; $xp--) {
		for ($yp = $i["w"]; $yp != 0; $yp--) {
			$fabric[($i["x"]+$xp)][($i["y"]+$yp)] = 1;
		}
	}
}
/*/var_dump($fabric);
//print($fabric);
foreach ($fabric as $f) {
	echo implode('',$f);
	echo "\n";
}
//*/
