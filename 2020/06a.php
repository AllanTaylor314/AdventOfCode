<?php
error_reporting(E_ERROR | E_PARSE);
$input=file_get_contents("6.txt");
$inputs=explode("\n\n",$input);
foreach ($inputs as $i) {
	$c=count( array_unique( str_split(str_replace("\n","",$i))));
	echo $c."\n";
	$sum+=$c;
}
echo $sum."\n";
//Answer:
?>
