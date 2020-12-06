<?php
error_reporting(E_ERROR | E_PARSE);
$input=file_get_contents("3.txt");
$inputs=str_split($input);
$houses;
$x=0;
$y=0;
$houses[$x][$y]++;
foreach ($inputs as $i) {
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
}
//echo array_sum($houses)."\n";
print_r($houses);
//echo count(array_filter($houses,"nonzero"))."\n";
foreach ($houses as $street) {
	$count+=count($street);
}
echo $count."\n";
//Answer:
function nonzero($val) {
	return $val != 0;
}
?>
