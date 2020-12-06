<?php
error_reporting(E_ERROR | E_PARSE);
$input=file_get_contents("6.txt");
$inputs=explode("\n\n",$input."\n",-1);
foreach ($inputs as $i) {
	//$c=count( array_unique( str_split(str_replace("\n","",$i))));
	//echo $c."\n";
	//$sum+=$c;
	$list=explode("\n",$i);
	$answersum=[];
	foreach ($list as $key => $answerlist) {
		$person=str_split($answerlist);
		foreach ($person as $key => $value) {
			$answersum[$value]++;
		}
	}
	$count=array_count_values($answersum);
	$sum+=$count[count($list)];
	var_dump($count);
	echo count($list)." ".$count[count($list)]."\n";
}
echo $sum."\n";
//Answer:
?>
