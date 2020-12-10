<?php
//error_reporting(E_ERROR | E_PARSE);
$input=file_get_contents("10.txt");
$inputs=explode("\n",$input,-1);
sort($inputs, SORT_NUMERIC);
var_dump($inputs);
$inputs[]=max($inputs)+3;
$j=0;
foreach ($inputs as $i) {
	switch ($i-$j) {
		case 1:
			$c1++;
			break;
		case 2:
			$c2++;
			break;
		case 3:
			$c3++;
			break;
		default:
			echo "invalid";
			exit();
			break;
	}
	$j=$i;
}
echo ($c1*$c3)."\n";
//Answer:
?>
