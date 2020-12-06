<?php
error_reporting(E_ERROR | E_PARSE);
$input=file_get_contents("8.txt");
$inputs=explode("\n",$input,-1);
$n=0;
foreach ($inputs as $i) {
	//echo $i;
	//eval('$x='.$i.";");
	$x='"'.addslashes($i).'"';
	echo $x."\n";
	$n+=strlen($x)-strlen($i);
}

echo $n."\n";
//Answer:
?>
