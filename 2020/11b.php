<?php
error_reporting(E_ERROR | E_PARSE);
$input=file_get_contents("11.txt");
$inputs=explode("\n",$input,-1);
$buffer="";
function new_state($x,$y) {
	$oldseats=$GLOBALS['oldseats'];
	$currentstate=$oldseats[$y][$x];
	//echo $currentstate;
	$count_occ=0;
/*$count_occ+=(($oldseats[$y-1][$x-1]=='#')?1:0);
	$count_occ+=(($oldseats[$y-1][$x]=='#')?1:0);
	$count_occ+=(($oldseats[$y-1][$x+1]=='#')?1:0);
	$count_occ+=(($oldseats[$y][$x-1]=='#')?1:0);
	$count_occ+=(($oldseats[$y][$x+1]=='#')?1:0);
	$count_occ+=(($oldseats[$y+1][$x-1]=='#')?1:0);
	$count_occ+=(($oldseats[$y+1][$x]=='#')?1:0);
	$count_occ+=(($oldseats[$y+1][$x+1]=='#')?1:0);*/
	for ($xd=-1;$xd<2;$xd++) {
		for ($yd=-1;$yd<2;$yd++) {
			if ($xd==0 && $yd==0) {$yd++;}
			$hitseat=false;
			for ($d=1;!$hitseat;$d++) {
				if (!isset($oldseats[$y+($yd*$d)][$x+($xd*$d)])) {
					$hitseat=true;
					continue;
				}
				if ($oldseats[$y+($yd*$d)][$x+($xd*$d)]=='.') {
					//echo "cont\n";
					//$hitseat=true;
					continue;
				}
				if ($oldseats[$y+($yd*$d)][$x+($xd*$d)]=='L') {
					$hitseat=true;
					//echo "hit L\n";
				}
				if ($oldseats[$y+($yd*$d)][$x+($xd*$d)]=='#') {
					$hitseat=true;
					$count_occ++;
					//echo "hit #\n";
				}
			}
		}
	}
	//var_dump($test_seats);
	//$count_occ=array_count_values($test_seats)['#'];
	//echo $count_occ;
	//$GLOBALS['buffer']=$GLOBALS['buffer']. $x.",".$y." sees ".$count_occ." occupied seats\n";
	if ($count_occ==0) {
		return "#";
	} elseif($count_occ>4) { //at least 5
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
//		echo implode("",$row)."\n";
	}
	//echo "\n";
	//echo $buffer;
	//$buffer="";
}

//var_dump($seats);
foreach ($seats as $row) {
	$export=$export.implode("",$row)."\n";
}
echo $export;
echo substr_count($export, "#")."\n";
//Answer:
?>
