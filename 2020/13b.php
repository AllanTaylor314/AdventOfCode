<?php
error_reporting(E_ERROR | E_PARSE);
$input=file_get_contents("13.txt");
//$input="\n17,x,13,19\n";
//$input="\n67,7,59,61\n";
$inputs=explode("\n",$input,-1);
$timestamp=$inputs[0];
$buses=explode(",",$inputs[1]);
//$buses=explode(",",str_replace("x","1",$inputs[1]));
function isnotx($x) {return $x!="x";}
$buses=array_filter($buses,"isnotx");
var_dump($buses);
$components=[];
$lcm=1;
foreach ($buses as $frequency) {
	$lcm*=$frequency;
}
echo "$lcm\n";
foreach ($buses as $offset => $frequency) {
	$components[$offset]=$lcm/$frequency;
	$small_mod=$components[$offset];
	$target=(100*$frequency-$offset)%$frequency;
	//$target=;
	if ($target>$frequency) {echo "Your target is too high\n";exit;}
	echo "O:$offset,M:$small_mod,T:$target\n";
	for ($multiplier=1;true;$multiplier++) {
		$result=($small_mod*$multiplier)%$frequency;
		if ($result==$target) {break;}
		echo "$result\r";
	}
	echo "($small_mod*$multiplier)%$frequency=".($small_mod*$multiplier)%$frequency."\n";
	$components[$offset]*=$multiplier;
	var_dump($components);
}

// https://www.youtube.com/watch?v=ru7mWZJlRQg
//echo ($bestid*$bestwait)." id:$bestid ($bestwait min)\n";
$answer=array_sum($components);
echo "\n".$answer."\n".($answer%$lcm)."\n";
foreach ($buses as $offset => $frequency) {
	echo $frequency.":".($answer%$frequency)."\n";
}
//Answer: 539746751134958
?>
