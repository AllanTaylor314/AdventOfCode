<?php
error_reporting(E_ERROR | E_PARSE);
$input=file_get_contents("2.txt");
$inputs=explode("\r\n",$input,-1); //-1 to remove empty last
$n=0;
foreach ($inputs as $i) {
  $j=explode(" ",$i);
//	$k=substr_count($j[2],$j[1][0]);
	if ($j[2][explode("-",$j[0])[0]-1]==$j[1][0] xor $j[2][explode("-",$j[0])[1]-1]==$j[1][0]) {
		$n++;
	}
}
echo $n;
//Answer:
?>
