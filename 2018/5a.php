<?php
header('Content-Type: text/plain');
include('5in.php');
$inputs = str_split($input);
$did_something = true;
while ($did_something) {
	$did_something = false;
	$inputs = array_values($inputs);
	for ($k = 0; $k < count($inputs); $k++) {
		$i = $inputs[$k];
		if (preg_match("/[A-Z]/",$i)) {
			if ($inputs[$k+1] == strtolower($i)) {
				unset($inputs[$k]);
				unset($inputs[$k+1]);
				$did_something = true;
				$k--;
			}
		} else {
			if ($inputs[$k+1] == strtoupper($i)) {
				unset($inputs[$k]);
				unset($inputs[$k+1]);
				$did_something = true;
				$k--;
			}
		}
		$inputs = array_values($inputs);
	}
}
//var_dump($inputs);
$answer = implode('', $inputs);
echo $answer . "\n\n" . strlen($answer);
