<?php
//error_reporting(E_ERROR | E_PARSE);
$input=file_get_contents("21.txt");
$inputs=explode("\n",$input,-1);
$foodstuffs=[]; //[0 => ingredients, 1 => allergens]
foreach ($inputs as $i) {
	$tmp=explode(" (contains ",$i);
	$foodstuffs[]=[explode(" ",$tmp[0]),explode(", ",str_replace(")","",$tmp[1]))];
}
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
foreach ($foodstuffs as $food) {
	$ingredients=$food[0];
	$allergens=$food[1];
	foreach ($allergens as $allergen) {
		foreach ($allergen_status[$allergen] as $ingredient => $status) {
			$allergen_status[$allergen][$ingredient]=(in_array($ingredient,$ingredients)) && $allergen_status[$allergen][$ingredient];
		}
	}
}

//PART 2

foreach ($allergen_status as $allergen => $ingredients) {
	foreach ($ingredients as $ingredient => $status) {
		if (!$status) {
			unset($allergen_status[$allergen][$ingredient]);
		}
	}
}
$still_searching=true;
while ($still_searching) {
	$still_searching=false;
	foreach ($allergen_status as $allergen => $ingredients) {
		$c=count($ingredients);
		if ($c>0) {
			$still_searching=true;
		}
		if ($c==1) {
			$bout[$allergen]=array_keys($ingredients)[0];
			foreach ($allergen_status as $allergen2 => $ingredients2) {
				unset($allergen_status[$allergen2][$bout[$allergen]]);
			}
		}
	}
}
ksort($bout);
var_dump($bout);
echo implode(",",$bout)."\n";
//Answer:
?>
