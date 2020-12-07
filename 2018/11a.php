<?php
header('Content-Type: text/plain');
$serial = 8199;
function P($Xin, $Yin) {
	return (((((($Xin+10) * $Yin + $GLOBALS['serial']) * ($Xin+10)) % 1000) - (((($Xin+10) * $Yin + $GLOBALS['serial']) * ($Xin+10)) % 100))/100) - 5;
}
//echo getPower(1,1);
$mostPower = -1000;
$xHasPower = 0;
$yHasPower = 0;
for ($x = 1; $x < 298; $x++) {
	for ($y = 1; $y < 298; $y++) {
		$thisPower =  P($x, $y)   + P($x+1, $y)   + P($x+2, $y)
					+ P($x, $y+1) + P($x+1, $y+1) + P($x+2, $y+1)
					+ P($x, $y+2) + P($x+1, $y+2) + P($x+2, $y+2);
		if ($thisPower > $mostPower) {
			$mostPower = $thisPower;
			$xHasPower = $x;
			$yHasPower = $y;
		}
	}
}
echo $xHasPower.','.$yHasPower;