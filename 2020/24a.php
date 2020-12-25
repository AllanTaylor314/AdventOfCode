<?php
//error_reporting(E_ERROR | E_PARSE);
$input=file_get_contents("24.txt");
$input=str_replace("nw","a",$input);
$input=str_replace("ne","f",$input);
$input=str_replace("se","d",$input);
$input=str_replace("sw","c",$input);
$input=str_replace("w","b",$input);
$inputs=explode("\n",$input,-1);
$instructions=[];
$tiles=[];
foreach ($inputs as $i) {
	$instructions[]=str_split($i);
}
foreach ($instructions as $i) {
	$x=0;
	$y=0;
	foreach ($i as $step) {
		switch ($step) {
			case 'a':
				--$y;
				break;
			case 'b':
				--$x;
				break;
			case 'c':
				--$x;
				++$y;
				break;
			case 'd':
				++$y;
				break;
			case 'e':
				++$x;
				break;
			case 'f':
				++$x;
				--$y;
				break;
		}
	}
	$tiles[$x][$y]=!isset($tiles[$x][$y]) || !$tiles[$x][$y];
	echo "($x,$y) set to ".($tiles[$x][$y]?"black\n":"white\n");
}
//var_dump($tiles);
$answer=0;
foreach ($tiles as $row) {
	$answer+=array_sum($row);
}
echo "$answer\n";
//Answer: 450
?>
