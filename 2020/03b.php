<?php
error_reporting(E_ERROR | E_PARSE);
$input=file_get_contents("3.txt");
$inputs=explode("\n",$input,-1);
$width=strlen($inputs[0]);
$answer=1;
for ($slope=1; $slope<8; $slope+=2) {//{1,3,5,7}R1D Slope
	$trees=0;
	$x=0;
	foreach ($inputs as $i) {
		if ($i[$x%$width]=="#") {
			$trees++;
		}
		$x+=$slope;
	}
	echo $trees."\n";
	$answer=$answer*$trees;
}
$trees=0;
$x=0;
foreach ($inputs as $n => $i) {
	if ($n%2==0) { //1R2D Slope - skip every second line
		if ($i[$x%$width]=="#") {
			$trees++;
		}
		$x++;
	}
}
echo $trees."\n";
$answer=$answer*$trees;
echo $answer."\n";
//Answer:
?>
