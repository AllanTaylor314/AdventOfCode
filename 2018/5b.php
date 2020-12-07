<?php
header('Content-Type: text/plain');
include('5in.php');
$master_inputs = str_split($input);
$did_something = true;
$alphabet = str_split('qwertyuiopasdfghjklzxcvbnm');
$lowest = 99999;
foreach ($alphabet as $letter) {
	$inputs = str_split(preg_replace("/[".$letter.strtoupper($letter)."]/", '', $input));
	$did_something = true;
while ($did_something) {
	$did_something = false;
	$inputs = array_values($inputs);
	for ($k = 0; $k < count($inputs); $k++) {
		$i = $inputs[$k];
		if (preg_match("/[A-Z]/",$i)) {
			if (@$inputs[$k+1] == strtolower($i)) {
				unset($inputs[$k]);
				unset($inputs[$k+1]);
				$did_something = true;
				//$k--;
			}
		} else {
			if ($inputs[$k+1] == strtoupper($i)) {
				unset($inputs[$k]);
				unset($inputs[$k+1]);
				$did_something = true;
				//$k--;
			}
		}
		$inputs = array_values($inputs);
	}
}
}
if (count($inputs) < $lowest) {
	$lowest = count($inputs);
}
//$count_of_letter = [];
/*
foreach ($inputs as $i) {
	if (!isset($count_of_letter[strtolower($i)])) {$count_of_letter[strtolower($i)]=0;}
	$count_of_letter[strtolower($i)]++;
}
$bestcount = 0;
foreach ($count_of_letter as $count) {
	if ($count > $bestcount) {
		$bestcount = $count;
	}
}
*/
//var_dump($inputs);
//$answer = implode('', $inputs);
//echo (strlen($answer)-$bestcount);
echo $lowest;
