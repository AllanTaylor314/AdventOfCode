<?php
error_reporting(E_ERROR | E_PARSE);
$input=file_get_contents("3.txt");
$inputs=str_split($input);
$houses;
$x=0;
$y=0;
$xr=0;
$yr=0;
$houses[$x][$y]++;
$houses[$xr][$yr]++;
foreach ($inputs as $key => $i) {
	if ($key%2) {
	if ($i==">") {
		$x++;
		$houses[$x][$y]++;
	} elseif ($i=="<") {
		$x--;
		$houses[$x][$y]++;
	} elseif ($i=="^") {
		$y++;
		$houses[$x][$y]++;
	} elseif ($i=="v") {
		$y--;
		$houses[$x][$y]++;
	}
} else {
	if ($i==">") {
		$xr++;
		$houses[$xr][$yr]++;
	} elseif ($i=="<") {
		$xr--;
		$houses[$xr][$yr]++;
	} elseif ($i=="^") {
		$yr++;
		$houses[$xr][$yr]++;
	} elseif ($i=="v") {
		$yr--;
		$houses[$xr][$yr]++;
	}
}
}
//echo array_sum($houses)."\n";
print_r($houses);
//echo count(array_filter($houses,"nonzero"))."\n";
foreach ($houses as $street) {
	$count+=count($street);
}
echo $count."\n";
//Answer:
?>
