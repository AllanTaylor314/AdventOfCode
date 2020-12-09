<?php
//error_reporting(E_ERROR | E_PARSE);
$input=file_get_contents("9.txt");
$inputs=explode("\n",$input,-1);
$pre=25;
foreach ($inputs as $key => $i) {
	if ($key<$pre) {continue;}
	$isgood=false;
	for ($j=$key-$pre;$j<$key;$j++) {
		//echo $j."\n";
		for ($k=$key-$pre;$k<$key;$k++) {
			if ($j==$k) {continue;}
			if ($inputs[$j]+$inputs[$k]==$i) {
				//echo "good\n";
				$isgood=true;
			}
		}
	}
	if (!$isgood) {echo $i." is invalid\n"; exit();}
}
echo "\n";
//Answer:
?>
