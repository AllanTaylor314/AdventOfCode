<?php
header('Content-Type: text/plain');
include('7in.php');
//var_dump($theArray);
$theListOfSteps = [];
$completedSteps = [];
for ($alpha = 'A'; $alpha != 'F'; $alpha++) {
	$theListOfSteps[$alpha] = 0;
}
$theListOfSteps['F'] = 0;
//var_dump($theListOfSteps);
foreach ($theArray as $theSubArray) {
	$theListOfSteps[$theSubArray[1]]++;
}
for ($loop = 0; $loop < 102; $loop++) {
	foreach (array_keys($theListOfSteps, 0) as $c) {
		$completedSteps[count($completedSteps)] = $c;
		foreach ($theArray as $key => $pair) {
			if (in_array($pair[0], $completedSteps)) {
				$theListOfSteps[$pair[1]] = 0;
				unset($theArray[$key]);
			}
		}
//		var_dump($c);
		unset($theListOfSteps[$c]);
//		var_dump($theListOfSteps);
		//echo $theListOfSteps[$c];
	}
}
//var_dump($theListOfSteps);
//var_dump($completedSteps);
foreach ($completedSteps as $thing ) {echo $thing;}
