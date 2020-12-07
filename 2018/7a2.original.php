<?php
header('Content-Type: text/plain');
include('7in.php');
//var_dump($theArray);
$theListOfSteps = [];
$completedSteps = [];
for ($alpha = 'A'; $alpha != 'AA'; $alpha++) {
	$theListOfSteps[$alpha] = 0;
}
$theListOfSteps['Z'] = 0;
//var_dump($theListOfSteps);
//foreach ($theArray as $theSubArray) {
//	$theListOfSteps[$theSubArray[1]]++;
//}
//for ($loop = 0; $loop < 150; $loop++) {
	while (count(array_keys($theListOfSteps, 0))) {
		foreach ($theArray as $theSubArray) {
			$theListOfSteps[$theSubArray[1]]++;
		}
		$c = array_keys($theListOfSteps, 0)[0];
		$completedSteps[count($completedSteps)] = $c;
		foreach ($theArray as $key => $pair) {
			if (/*in_array($pair[0], $completedSteps)*/$pair[0] == $c) {
				$theListOfSteps[$pair[1]] = 0;
				unset($theArray[$key]);
			}
		}
		unset($theListOfSteps[$c]);
	}
//}
//var_dump($theListOfSteps);
//var_dump($completedSteps);
foreach ($completedSteps as $thing ) {echo $thing;}
