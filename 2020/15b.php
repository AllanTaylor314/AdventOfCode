<?php
//error_reporting(E_ERROR | E_PARSE);
$input=file_get_contents("15.txt");
//$input="0,3,6";
//This is a php implementation of https://www.reddit.com/r/adventofcode/comments/kdf85p/2020_day_15_solutions/gg4ls55?utm_source=share&utm_medium=web2x&context=3
$seq=explode(",",str_replace("\n","",$input));
$init=array_pop($seq);
echo $init;
$lastpos=array_flip($seq);
var_dump($lastpos);
for ($i=count($seq); $i<30000000-1; $i++) {
	if (isset($lastpos[$init])) {
		$new=$i-$lastpos[$init];
	} else {
		$new=0;
	}
	$lastpos[$init]=$i;
	$init=$new;
	//echo ",$init";
}
//var_dump($lastpos);
/*/echo $input;
$curr=array_pop($seq);
for ($i=count($seq);$i<30000000;$i++) {
	//echo "$i\r";
	if (in_array($curr, $seq)) {
		$n=array_flip($seq)[$curr];
		unset($seq[$n]);
		$seq[$i]=$curr;
		$curr=$i-$n;
	} else {
		$seq[$i]=$curr;
		$curr=0;
		echo "$i\r"; //make this less often
	}
	//echo ",$curr";

	//$curr=$new;
}//*/
/*/
for ($i=count($seq);$i<30000000;$i++) {
	echo "$i\r";
	$prev=array_pop($seq);
	if (in_array($prev, $seq)) {
		$n=array_search($prev,array_reverse($seq));
		$new=$i-$n-1;
		//unset($seq[$n]);
	} else {
		$new=0;
	}
	//echo ",$new";
	$seq[]=$prev;
	$seq[]=$new;
}//*/
echo "\n$init\n";
//Answer:
?>
