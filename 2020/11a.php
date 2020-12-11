<?php
error_reporting(E_ERROR | E_PARSE);
$input=file_get_contents("11.txt");
$inputs=explode("\n",$input,-1);

function new_state($x,$y) {
	$oldseats=$GLOBALS['oldseats'];
	$currentstate=$oldseats[$y][$x];
	//echo $currentstate;
	$count_occ=0;
	$count_occ+=(($oldseats[$y-1][$x-1]=='#')?1:0);
	$count_occ+=(($oldseats[$y-1][$x]=='#')?1:0);
	$count_occ+=(($oldseats[$y-1][$x+1]=='#')?1:0);
	$count_occ+=(($oldseats[$y][$x-1]=='#')?1:0);
	$count_occ+=(($oldseats[$y][$x+1]=='#')?1:0);
	$count_occ+=(($oldseats[$y+1][$x-1]=='#')?1:0);
	$count_occ+=(($oldseats[$y+1][$x]=='#')?1:0);
	$count_occ+=(($oldseats[$y+1][$x+1]=='#')?1:0);
	//var_dump($test_seats);
	//$count_occ=array_count_values($test_seats)['#'];
	//echo $count_occ;
	if ($count_occ==0) {
		return "#";
	} elseif($count_occ>3) {
		return "L"; //Empty
	}
	return $currentstate;
}

//$seats[row y][column x]
// L empty
// . floor (no change)
// # occupied
foreach ($inputs as $key => $i) {
	$seats[$key]=str_split($i);
}
$oldseats=[];
while ($seats!=$oldseats) {
	$oldseats=$seats;
	foreach ($seats as $y => $row) {
		foreach ($row as $x => $state) {
			if ($state=='.') {continue;} //no change - always .
		 	//echo $state." to ";
			$seats[$y][$x]=new_state($x,$y);
			//echo $seats[$y][$x]."\n";
		}
	}
}

//var_dump($seats);
foreach ($seats as $row) {
	$export=$export.implode("",$row)."\n";
}
echo $export;
echo substr_count($export, "#")."\n";
//Answer:
?>
