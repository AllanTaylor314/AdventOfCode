<?php
error_reporting(E_ERROR | E_PARSE);
$input=file_get_contents("2.txt");
$inputs=explode("\r\n",$input,-1); //-1 to remove empty last
$n=0;
foreach ($inputs as $i) {
  $j=explode(" ",$i);
	$k=substr_count($j[2],$j[1][0]);
	if ($k >= explode("-",$j[0])[0] && $k <= explode("-",$j[0])[1]) {
		$n++;
	}
}
echo $n;
//Answer:
?>
