<?php
header('Content-Type: text/plain');
$serial = 8199;
$holo = array_fill(0, 300, array_fill(0, 300, 0));
function P($Xin, $Yin) {
	return (((((($Xin+10) * $Yin + $GLOBALS['serial']) * ($Xin+10)) % 1000) - (((($Xin+10) * $Yin + $GLOBALS['serial']) * ($Xin+10)) % 100))/100) - 5;
}
function IDK($Xin, $Yin, $Area) {
	$t = 0;
	for ($i = $Area - 1; $i >  -1; $i--) {
		for ($j = $Area - 1; $j >  -1; $j--) {
			$t += $GLOBALS['holo'][$Xin + $i][$Yin + $j];
		}
	}
	return $t;
}
//echo getPower(1,1);
for ($x = 1; $x < 301; $x++) {
	for ($y = 1; $y < 301; $y++) {
		$holo[$x][$y] = P($x,$y);
	}
}
$mostPower = -1000;
$xHasPower = 0;
$yHasPower = 0;
$aHasPower = 0;
for ($a = 1; $a < 301; $a++) {
	for ($x = 1; $x < 302 - $a; $x++) {
		for ($y = 1; $y < 302 - $a; $y++) {
			$thisPower = IDK($x, $y, $a);
			if ($thisPower > $mostPower) {
				$mostPower = $thisPower;
				$xHasPower = $x;
				$yHasPower = $y;
				$aHasPower = $a;
			}
		}
	}
	echo $mostPower.':'.$xHasPower.','.$yHasPower.','.$aHasPower."\n";
}
echo "\n".$xHasPower.','.$yHasPower.','.$aHasPower;