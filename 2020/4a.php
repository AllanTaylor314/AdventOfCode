<?php
error_reporting(E_ERROR | E_PARSE);
$input=file_get_contents("4.txt");
$inputs=explode("\n\n",$input);
$n=0;
foreach ($inputs as $i) {
	if (preg_match('/byr:/',$i) &&
	preg_match('/iyr:/',$i) &&
	preg_match('/eyr:/',$i) &&
	preg_match('/hgt:/',$i) &&
	preg_match('/hcl:/',$i) &&
	preg_match('/ecl:/',$i) &&
	preg_match('/pid:/',$i)) {
		$n++;
	}
}
echo $n."\n";
//Answer:
?>
