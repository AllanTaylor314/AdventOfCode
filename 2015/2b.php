<?php
error_reporting(E_ERROR | E_PARSE);
$input=file_get_contents("2.txt");
$inputs=explode("\n",$input,-1);
$area=0;
foreach ($inputs as $i) {
	$j=explode("x",$i);
	$sa=$j[0]*$j[1]*$j[2];
	$sa+=2*($j[0]+$j[1]+$j[2]-max($j));
	$area+=$sa;
}
echo "${area}\n";
//Answer:
?>
