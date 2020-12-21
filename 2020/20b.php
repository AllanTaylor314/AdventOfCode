<?php
//error_reporting(E_ERROR | E_PARSE);
// INPUT PROCESSING
$input=file_get_contents("20.txt");
$inputs=explode("\n\n",$input,-1);
$tiles=[];
$sides=[];
$matches=[];
foreach ($inputs as $i) {
	$tmp=explode("\n",$i);
	$tiles[(int)str_replace("Tile ","",array_shift($tmp))]=$tmp;
}

// CREATE LIST OF EDGES (INCLUDING FLIPS)
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
// CREATE ARRAY OF SURROUNDING TILES
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
//REMOVE DUPLICATE MATCHES
foreach ($matches as $id => $values) {
	$matches[$id]=array_unique($values);
}
/*/var_dump($matches);
$test=trim_tile($tiles[1217]);
var_dump($test);
$test=rotate_tile($test);
var_dump($test);
$test=flip_tile_horiz($test);
var_dump($test);
$test=flip_tile_vert($test);
var_dump($test);//*/
//$answer=1;

//SORT CORNER/EDGE PIECES - just like a puzzle
$tiles_corner=[];
$tiles_side=[];
$tiles_centre=[];
$arrangement=[]; //[x][y]
foreach ($matches as $id => $other_ids) {
	if (count($other_ids)==2) {
	//	echo "$id\n";
	//	$answer*=$id;
	//	var_dump($tiles[$id]);
	}
	switch (count($other_ids)) {
		case 2:
//			echo "$id\n";
//			$answer*=$id;
			$tiles_corner[]=$id;
			break;
		case 3:
			$tiles_side[]=$id;
			break;
		default:
			$tiles_centre[]=$id;
			break;
	}
}
//var_dump($tiles_corner);
//var_dump($tiles_side);
//var_dump($tiles_centre);
//$x=0;
//$y=0;

//ARRANGE PIECES (ignore orientation)
// TOP ROW
$arrangement[0][0]=array_shift($tiles_corner);
for ($y=1;$y<11;$y++) {
	foreach ($tiles_side as $index => $id) {
		if (in_array($id,$matches[$arrangement[0][$y-1]])) {
			$arrangement[0][$y]=$id;
			$tiles_side[$index]=false;
			unset($tiles_side[$index]);
			break;
		}
	}
}
foreach ($tiles_corner as $index => $id) {
	if (in_array($id,$matches[$arrangement[0][$y-1]])) {
		$arrangement[0][$y]=$id;
		unset($tiles_corner[$index]);
		break;
	}
}
// MIDDLE ROWS
for ($x=1;$x<11;$x++) {
	$arrangement[$x]=[];
	//echo "x=$x\n";
	foreach ($tiles_side as $index => $id) {
		if (in_array($id,$matches[$arrangement[$x-1][0]])) {
			$arrangement[$x][0]=$id;
			unset($tiles_side[$index]);
			break;
		}
	}
	for ($y=1;$y<11;$y++) {
		//$arrangement[$x][$y]=false;
		//echo "y=$y\n";
		//var_dump($arrangement);
		//echo "$x,$y:".$arrangement[$x][$y-1].",".$arrangement[$x-1][$y]."\n" || exit();
		foreach ($tiles_centre as $index => $id) {
			if (in_array($id,$matches[$arrangement[$x][$y-1]]) && in_array($id,$matches[$arrangement[$x-1][$y]])) {
				$arrangement[$x][$y]=$id;
				unset($tiles_centre[$index]);
				break;
			}
		}
	}
	foreach ($tiles_side as $index => $id) {
		if (in_array($id,$matches[$arrangement[$x][$y-1]]) && in_array($id,$matches[$arrangement[$x-1][$y]])) {
			$arrangement[$x][11]=$id;
			unset($tiles_side[$index]);
			break;
		}
	}
}
// BOTTOM ROW
foreach ($tiles_corner as $index => $id) {
	if (in_array($id,$matches[$arrangement[10][0]])) {
		$arrangement[11][0]=$id;
		unset($tiles_corner[$index]);
		break;
	}
}
for ($y=1;$y<11;$y++) {
	//$arrangement[$x][$y]=false;
	//echo "y=$y\n";
	//var_dump($arrangement);
	//echo "$x,$y:".$arrangement[$x][$y-1].",".$arrangement[$x-1][$y]."\n" || exit();
	foreach ($tiles_side as $index => $id) {
		if (in_array($id,$matches[$arrangement[11][$y-1]]) && in_array($id,$matches[$arrangement[10][$y]])) {
			$arrangement[11][$y]=$id;
			unset($tiles_side[$index]);
			break;
		}
	}
}
foreach ($tiles_corner as $index => $id) {
	if (in_array($id,$matches[$arrangement[11][10]]) && in_array($id,$matches[$arrangement[10][11]])) {
		$arrangement[11][11]=$id;
		unset($tiles_corner[$index]);
		break;
	}
}

//var_dump($arrangement);
// ORIENT PIECES
$puzzle=[];
foreach ($arrangement as $x => $line) {
	$puzzle[$x]=[];
	foreach ($line as $y => $id) {
		if ($x==0 && $y==0) {
			$puzzle[$x][$y]=rotate_tile(rotate_tile($tiles[$id])); //Brute forced - meh
			continue;
		}
		//var_dump($puzzle);
		$left_target=($x==0?true:get_tile_right($puzzle[$x-1][$y]));
		//var_dump($left_target);
		$top_target=($y==0?true:get_tile_bottom($puzzle[$x][$y-1]));
		foreach (gen_tile_iterations($tiles[$id]) as $tile) {
			//var_dump($tile);
			//echo "T:$top_target\nT?".get_tile_top($tile)."\nL:$left_target\nL?".get_tile_left($tile)."\n";
			$test=(($y==0 || $top_target==get_tile_top($tile)) && ($x==0 || $left_target==get_tile_left($tile)));
			//var_dump($test);
			if ($test) {
				$puzzle[$x][$y]=$tile;
				break;
			}
			//echo implode("\n",$tile)."\n\n";
		}
	}
}

//var_dump($puzzle);
$new_puzzle=[];
foreach ($puzzle as $x => $p) {
	foreach ($p as $y => $tile) {
		$new_puzzle[$x][$y]=rotate_tile(flip_tile_vert($tile));
	}
}//*/
/*/ PRINT PUZZLE
foreach ($new_puzzle as $ka => $a) {
	$out=[];
	foreach ($a as $kb => $b) {
		foreach ($b as $kc => $c) {
			//echo "$c ";
			@$out[$kc]=$out[$kc].$c." ";
		}
		//echo "\n";
	}
	echo implode("\n",$out);
	echo "\n\n";
}//*/

// PUZZLE TO NEW INPUT
$export="";
foreach ($new_puzzle as $ka => $a) {
	$out=[];
	foreach ($a as $kb => $b) {
		$bt=trim_tile($b);
		foreach ($bt as $kc => $c) {
			//echo "$c ";
			@$out[$kc]=$out[$kc].$c;
		}
		//echo "\n";
	}
	//echo implode("\n",$out)."\n";
	$export.=implode("\n",$out)."\n";
}
/*$export=".#.#..#.##...#.##..#####
###....#.#....#..#......
##.##.###.#.#..######...
###.#####...#.#####.#..#
##.#....#.##.####...#.##
...########.#....#####.#
....#..#...##..#.#.###..
.####...#..#.....#......
#..#.##..#..###.#.##....
#.####..#.####.#.#.###..
###.#.#...#.######.#..##
#.####....##..########.#
##..##.#...#...#.#.#.#..
...#..#..#.#.##..###.###
.#.#....#.##.#...###.##.
###.#...#..#.##.######..
.#.#.###.##.##.#..#.##..
.####.###.#...###.#..#.#
..#.#..#..#.#.#.####.###
#..####...#.#.#.###.###.
#####..#####...###....##
#.##..#..#...#..####...#
.#.###..##..##..####.##.
...###...##...#...#..###";//*/
//echo $export;
//$regex_monster='/#(.|\n){78}(#.{4}#){3}##(.|\n){77}(.#.){6}/';
//$regex_monster='/(#)(?:.|\n){78}(?:(#).{4}(#)){3}(#)(#)(?:.|\n){77}(?:.(#).){6}/'; //Doesn't count the 8 overlaps
$regex_monster='/#(?=(?:.|\n){78}(?:(#).{4}(#)){3}(#)(#)(?:.|\n){77}(?:.(#).){6})/'; //Look ahead - don't eat the chars!
//$regex_monster='/#(.|\n){6}(#.{4}#){3}##(.|\n){5}(.#.){6}/';
//echo "$answer\n";
foreach (gen_tile_iterations(explode("\n",$export)) as $boardsplosion) {
	$board=implode("\n",$boardsplosion);
	$count=preg_match_all($regex_monster,$board);
	//echo "C:$count\n";
	if ($count>0) {echo $board."\n".(substr_count($board,"#")-(15*$count))."\n"; break;}
}
//                    #
//  #    ##    ##    ###
//   #  #  #  #  #  #

function trim_tile($tile) {
	array_pop($tile);
	array_shift($tile);
	foreach ($tile as $key => $row) {
		$tile[$key]=substr($row,1,8);
	}
	return $tile;
}

function rotate_tile($tile) {
	$new_tile=[];
	foreach ($tile as $row => $line) {
		foreach (str_split($line) as $column => $char) {
			@$new_tile[$column]=$char.$new_tile[$column];
		}
	}
	return $new_tile;
}

function flip_tile_vert($tile) {
	return array_reverse($tile);
}

function flip_tile_horiz($tile) {
	foreach ($tile as $id => $line) {
		$tile[$id]=strrev($line);
	}
	return $tile;
}

function get_tile_top($tile) {
	return $tile[0];
}

function get_tile_bottom($tile) {
	return $tile[9];
}

function get_tile_left($tile) {
	$left="";
	//$right="";
	foreach ($tile as $line) {
		$left=$left.$line[0];
		//$right=$right.$line[9];
	}
	return $left;
}

function get_tile_right($tile) {
	//$left="";
	$right="";
	foreach ($tile as $line) {
		//$left=$left.$line[0];
		$right=$right.$line[9];
	}
	return $right;
}

function gen_tile_iterations($tile) {
	$new_tile=$tile;
	yield $new_tile;
	yield $new_tile=rotate_tile($new_tile);
	yield $new_tile=rotate_tile($new_tile);
	yield $new_tile=rotate_tile($new_tile);
	yield $new_tile=flip_tile_vert(rotate_tile($new_tile));
	yield $new_tile=rotate_tile($new_tile);
	yield $new_tile=rotate_tile($new_tile);
	yield $new_tile=rotate_tile($new_tile);
}
//Answer:
?>
