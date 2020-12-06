<?php
error_reporting(E_ERROR | E_PARSE);
$input=file_get_contents("5.txt");
$inputs=explode("\n",$input,-1);
foreach ($inputs as $i) {
	$bin=bindec('0b'.str_replace(["F","B","L","R"],[0,1,0,1],$i));
	echo $bin."\n";
	if ($bin>$out) {
		$out=$bin;
	}
}
echo $out."\n";
//Answer:
?>
