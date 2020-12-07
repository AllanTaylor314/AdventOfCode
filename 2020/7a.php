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
$oldcount=-1;
while ($oldcount!=count(array_unique($bagscontaininggold))) {
	$oldcount=count(array_unique($bagscontaininggold));
	foreach ($rules as $key => $value) {
		foreach ($bagscontaininggold as $bagcolour) {
			if(isset($value[$bagcolour])) {
				$bagscontaininggold[]=$key;
			}
		}
		if(isset($value[$search])) {
			$bagscontaininggold[]=$key;
		}
	}
	$bagscontaininggold=array_unique($bagscontaininggold);
}

//var_dump($rules);
//var_dump($rules["shiny green"]);
var_dump($bagscontaininggold);
echo count(array_unique($bagscontaininggold))."\n";
//Answer:
?>
