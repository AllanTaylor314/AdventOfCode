<?php
//error_reporting(E_ERROR | E_PARSE);
$input=file_get_contents("20.txt");
$inputs=explode("\n\n",$input,-1);
$tiles=[];
$sides=[];
$matches=[];
foreach ($inputs as $i) {
	$tmp=explode("\n",$i);
	$tiles[(int)str_replace("Tile ","",array_shift($tmp))]=$tmp;
}
foreach ($tiles as $id => $tile) {
	$left="";
	$right="";
	foreach ($tile as $line) {
		$left=$left.$line[0];
		$right=$right.$line[9];
	}
	$sides[$id]= [$tile[0],strrev($tile[0]),
								$tile[9],strrev($tile[9]),
								$left,strrev($left),
								$right,strrev($right)];
}
//var_dump($tiles);
//var_dump($sides);

foreach ($sides as $id => $tile_sides) {
	foreach ($tile_sides as $single_side) {
		foreach ($sides as $test_id => $test_sides) {
			if ($test_id==$id) {continue;}
			if (in_array($single_side,$test_sides)) {
				$matches[$id][]=$test_id;
			}
		}
	}
}
var_dump($matches);
$answer=1;
foreach ($matches as $id => $other_ids) {
	if (count($other_ids)==4) {echo "$id\n";$answer*=$id;}
}
echo "$answer\n";
//Answer:
?>
