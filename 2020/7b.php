<?php
error_reporting(E_ERROR | E_PARSE);
$input=file_get_contents("7.txt");
$search="shiny gold";
$inputs=explode("\n",$input,-1);
foreach ($inputs as $i) {
	$temp=explode(" bags contain ", $i);
	$contents=explode(", ",$temp[1]);
	//$rules[$temp[0]]=[];
	foreach ($contents as $value) {
		$bag=explode(" ",$value);
		$rules[$temp[0]][$bag[1]." ".$bag[2]]=(int)$bag[0];
	}
	//var_dump($temp);
}


//var_dump($rules);
//var_dump($rules["shiny green"]);
//var_dump($bagscontaininggold);
echo number_in_bag($search)."\n";
//Answer:
function number_in_bag($bagname) {
	$output=0;
	if ($bagname=="other bags.") {return 0;}
	echo $bagname."\n";
	var_dump($GLOBALS['rules'][$bagname]);
	foreach ($GLOBALS['rules'][$bagname] as $subname => $numberofsubbags) {
		$output+=$numberofsubbags*(number_in_bag($subname)+1);
	}
	return $output;
}
?>
