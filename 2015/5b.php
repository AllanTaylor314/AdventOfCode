<?php
error_reporting(E_ERROR | E_PARSE);
$input=file_get_contents("5.txt");
$inputs=explode("\n",$input,-1);
$n=0;
foreach ($inputs as $i) {
	echo preg_match_all('/(..).*\1/i',$i)."\n";
	echo preg_match('/(.).\1/',$i)."\n";
	if (
		preg_match_all('/(..).*\1/i',$i) &&
		preg_match('/(.).\1/',$i)
	) {
		$n++;
	}
}
echo $n."\n";
//Answer:
?>
