<?php
header('Content-Type: text/plain');
include("4in.php");
$inputs = explode("\n", $input);
$a = [];
foreach ($inputs as $key => $in) {
	if (preg_match("/Guard #(.*?) begins/", $in, $m)) {
		$guard = (int)$m[1];
//		$a[$guard] = [];
//		$zzz = 0;
//		var_dump($m);
	} else {
		if ($in[19] == 'f') {
//		$t = (int)($in[15].$in[16]);
			$waketime = (int)($inputs[$key+1][15].$inputs[$key+1][16]);
			for ($t = (int)($in[15].$in[16]); $t < $waketime; $t++) {
				if (!isset($a[$guard][$t])) {
					$a[$guard][$t] = 0;
				}
				$a[$guard][$t]++;
			}
		}

	}
//	$a[$guard][$t]++;
//	var_dump($guard);
}
var_dump($a);
$totals = [];
foreach ($a as $guardid => $sleep) {
	$totals[$guardid] = 0;
	foreach ($sleep as $s) {
		$totals[$guardid] += $s;
	}
}
var_dump($totals);
$mostsleeps = 0;
$sleepy_guard = 0;
foreach ($totals as $gid => $totalsleeps) {
	if ($totalsleeps > $mostsleeps) {
		$mostsleeps = $totalsleeps;
		$sleepy_guard = $gid;
	}
}
var_dump($mostsleeps);
var_dump($sleepy_guard);
$sleepy_count = 0;
$sleepy_minute = 0;
foreach ($a[$sleepy_guard] as $time => $count) {
	if ($count > $sleepy_count) {
		$sleepy_count = $count;
		$sleepy_minute = $time;
	}
}
var_dump($sleepy_count);
var_dump($sleepy_minute);
echo "\n\n".$sleepy_minute*$sleepy_guard;
