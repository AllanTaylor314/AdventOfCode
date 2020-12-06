<?php
error_reporting(E_ERROR | E_PARSE);
$input=file_get_contents("5.txt");
$inputs=explode("\n",$input,-1);
$n=0;
foreach ($inputs as $i) {
	//echo preg_match_all('/[aeiou]/i',$i)."\n";
	//echo preg_match_all('/(.)\1/',$i)."\n";
	if (preg_match_all('/[aeiou]/i',$i)>2 && preg_match('/(.)\1/',$i) &&
	strpos($i,"ab")===false &&
	strpos($i,"cd")===false &&
	strpos($i,"pq")===false &&
	strpos($i,"xy")===false ) {
		$n++;
	}
}
echo $n."\n";
//Answer:
?>
