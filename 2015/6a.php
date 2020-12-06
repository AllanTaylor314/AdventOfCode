<?php
error_reporting(E_ERROR | E_PARSE);
$input=str_replace("turn ","turn",file_get_contents("6.txt"));
$inputs=explode("\n",$input,-1);
$lights=[];
foreach ($inputs as $i) {
	$j=explode(" ",$i); //0: Instruction; 1 and 3: locations
	$startx=explode(",",$j[1])[0];
	$starty=explode(",",$j[1])[1];
	$endx=explode(",",$j[3])[0];
	$endy=explode(",",$j[3])[1];
	for ($x=$startx; $x<=$endx; $x++) {
		for ($y=$starty; $y<=$endy; $y++) {
			switch ($j[0]) {
				case 'turnon':
					$lights[$x][$y]=true;
					break;
				case 'turnoff':
					$lights[$x][$y]=false;
					break;
				case 'toggle':
					$lights[$x][$y]=!$lights[$x][$y];
					break;
			}
		}
	}
}
foreach ($lights as $string) {
	$count+=array_sum($string);
}
echo $count."\n";
//Answer:
?>
