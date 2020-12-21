<?php
//error_reporting(E_ERROR | E_PARSE);
$input=file_get_contents("21.txt");
$inputs=explode("\n",$input,-1);
$foodstuffs=[]; //[0 => ingredients, 1 => allergens]
foreach ($inputs as $i) {
	$tmp=explode(" (contains ",$i);
	$foodstuffs[]=[explode(" ",$tmp[0]),explode(", ",str_replace(")","",$tmp[1]))];
}
var_dump($foodstuffs);
$could_be_allergen=[];
$allergen_status=[];
foreach ($foodstuffs as $food) {
	foreach ($food[1] as $allergen) {
		//$allergens[]=$allergen;
		$allergen_status[$allergen]=[];
		foreach ($food[0] as $ingredient) {
			$could_be_allergen[$ingredient]=false;
			$allergen_status[$allergen][$ingredient]=true;
		}
	}
}
//$allergens=array_unique($allergens);
//var_dump($allergen_status);
foreach ($foodstuffs as $food) {
	$ingredients=$food[0];
	$allergens=$food[1];
	foreach ($allergens as $allergen) {
		foreach ($allergen_status[$allergen] as $ingredient => $status) {
			$allergen_status[$allergen][$ingredient]=(in_array($ingredient,$ingredients)) && $allergen_status[$allergen][$ingredient];
		}
	}
}
var_dump($allergen_status);
foreach ($allergen_status as $ingredients) {
	foreach ($ingredients as $ingredient => $status) {
		$could_be_allergen[$ingredient]=$status||$could_be_allergen[$ingredient];
	}
}

var_dump($allergen_status);
$out=[];

$new_in=" ".str_replace("\n"," ",$input);
/*/
foreach ($allergen_status as $allergen => $ingredients) {
	foreach ($ingredients as $ingredient => $status) {
		if (!$status && !isset($out[$ingredient])) {
			echo substr_count($new_in," ".$ingredient." ")."*$ingredient\n";
			$out[$ingredient]=substr_count($new_in," ".$ingredient." ");
		}
	}
}//*/

foreach ($could_be_allergen as $ingredient => $status) {
	if (!$status) {
		echo substr_count($new_in," ".$ingredient." ")."*$ingredient\n";
		$out[$ingredient]=substr_count($new_in," ".$ingredient." ");
	}
}
var_dump($could_be_allergen);
var_dump($out);
echo array_sum($out)."\n";
//Answer:
?>
