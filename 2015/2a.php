<?php
error_reporting(E_ERROR | E_PARSE);
$input=file_get_contents("2.txt");
$inputs=explode("\n",$input,-1);
$area=0;
foreach ($inputs as $i) {
	$j=explode("x",$i);
	$sa=2*($j[0]*$j[1]+$j[0]*$j[2]+$j[1]*$j[2]);
	//echo $sa."\n";
	$sa+=$j[0]*$j[1]*$j[2]/max($j);
	//echo $sa."\n";
	$area+=$sa;
	//echo $sa."\n";
}
echo "${area}\n";
//Answer:
?>
