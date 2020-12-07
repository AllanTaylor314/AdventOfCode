<?php
header('Content-Type: text/plain');
include('7in.php');
$theListOfSteps = [];
$completedSteps = [];
for ($alpha = 'A'; $alpha != 'AA'; $alpha++) {
	$theListOfSteps[$alpha] = 0;
}
//$theListOfSteps['Z'] = 0;
while (array_keys($theListOfSteps, 0)) {
	foreach ($theArray as $theSubArray) {
		$theListOfSteps[$theSubArray[1]]++;
	}
	$c = array_keys($theListOfSteps, 0)[0];
	$completedSteps[count($completedSteps)] = $c;
	foreach ($theArray as $key => $pair) {
		if ($pair[0] == $c) {
			$theListOfSteps[$pair[1]] = 0;
			unset($theArray[$key]);
		}
	}
	unset($theListOfSteps[$c]);
}
foreach ($completedSteps as $thing ) {echo $thing;}
