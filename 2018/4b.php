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

$most_sleep_for_each = [];
$time_of_most_sleep_for_each = [];
foreach ($a as $gid => $b) {
	$sleepy_count = 0;
	$sleepy_minute = 0;
	foreach ($b as $time => $count) {
		if ($count > $sleepy_count) {
			$sleepy_count = $count;
			$sleepy_minute = $time;
		}
	}
	$most_sleep_for_each[$gid] = $sleepy_count;
	$time_of_most_sleep_for_each[$gid] = $sleepy_minute;

}
$most_times_asleep = 0;
$guard_with_most_sleep = 0;
foreach ($most_sleep_for_each as $gid => $count) {
	if ($count > $most_times_asleep) {
		$most_times_asleep = $count;
		$guard_with_most_sleep = $gid;
	}
}
echo $guard_with_most_sleep*$time_of_most_sleep_for_each[$guard_with_most_sleep];
