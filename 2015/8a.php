<?php
error_reporting(E_ERROR | E_PARSE);
$input=file_get_contents("8.txt");
$inputs=explode("\n",$input,-1);
$n=0;
foreach ($inputs as $i) {
	//echo $i;
	eval('$x='.$i.";");
	echo $x."\n";
	$n+=strlen($i)-strlen($x);
}

echo $n."\n";
//Answer:
?>
