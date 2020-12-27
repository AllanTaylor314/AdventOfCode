<?php
error_reporting(E_ERROR | E_PARSE);
$input=file_get_contents("3.txt");
$inputs=explode("\n",$input,-1);
$width=strlen($inputs[0]);
$trees=0;
$x=0;
foreach ($inputs as $i) {
	echo $x.",".$i[$x%$width]."\n";
	if ($i[$x%$width]=="#") {
		$trees++;
	}
	$x+=3;
}
echo $trees."\n";
//Answer:
?>
