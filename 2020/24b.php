<?php
//error_reporting(E_ERROR | E_PARSE);
$input=file_get_contents("24.txt");
$input=str_replace("nw","a",$input);
$input=str_replace("ne","f",$input);
$input=str_replace("se","d",$input);
$input=str_replace("sw","c",$input);
$input=str_replace("w","b",$input);
$inputs=explode("\n",$input,-1);
$instructions=[];
$tiles=[];
$xmin=0;//-15;
$xmax=0;//15;
$ymin=0;//-15;
$ymax=0;//15;
foreach ($inputs as $i) {
	$instructions[]=str_split($i);
}
foreach ($instructions as $i) {
	$x=0;
	$y=0;
	foreach ($i as $step) {
		switch ($step) {
			case 'a':
				--$y;
				break;
			case 'b':
				--$x;
				break;
			case 'c':
				--$x;
				++$y;
				break;
			case 'd':
				++$y;
				break;
			case 'e':
				++$x;
				break;
			case 'f':
				++$x;
				--$y;
				break;
		}
	}
	if ($x<$xmin) {$xmin=$x;}
	if ($x>$xmax) {$xmax=$x;}
	if ($y<$ymin) {$ymin=$y;}
	if ($y>$ymax) {$ymax=$y;}
	//$tiles[$x][$y]=!isset($tiles[$x][$y]) || !$tiles[$x][$y];
	$tiles[$x][$y]=!($tiles[$x][$y]??false);
	echo "($x,$y) set to ".($tiles[$x][$y]?"black\n":"white\n");
}
//var_dump($tiles);
$answer=0;
foreach ($tiles as $row) {
	$answer+=array_sum($row);
}

printpattern($tiles);

echo "Day 0: $answer\n";
//var_dump($tiles);
for ($day=1;$day<=100;++$day) {
	$planned_tiles=$tiles;
	/*foreach ($tiles as $x => $row) {
		foreach ($row as $y => $value) {
			if ($value) {}
		}
	}*/
	for ($x=$xmin-2;$x<($xmax+3);++$x) {
		for ($y=$ymin-2;$y<($ymax+3);++$y) {
			$colour=$tiles[$x][$y]??false;
			$b=0;
			if ($tiles[$x][$y-1]??false) {++$b;}
			if ($tiles[$x-1][$y]??false) {++$b;}
			if ($tiles[$x-1][$y+1]??false) {++$b;}
			if ($tiles[$x][$y+1]??false) {++$b;}
			if ($tiles[$x+1][$y]??false) {++$b;}
			if ($tiles[$x+1][$y-1]??false) {++$b;}
			//$w=6-$b;
			//echo "B:$b\n";
			if ($colour) { //black
				if ($b==0||$b>2) {// issue was that I was checking $w not $b
					$planned_tiles[$x][$y]=false; //white
					if ($x<$xmin) {$xmin=$x;}
					if ($x>$xmax) {$xmax=$x;}
					if ($y<$ymin) {$ymin=$y;}
					if ($y>$ymax) {$ymax=$y;}
				}
			} else { //white
				if ($b==2) {
					$planned_tiles[$x][$y]=true; //black
					if ($x<$xmin) {$xmin=$x;}
					if ($x>$xmax) {$xmax=$x;}
					if ($y<$ymin) {$ymin=$y;}
					if ($y>$ymax) {$ymax=$y;}
				}
			}
		}
	}
	$tiles=$planned_tiles;
	//printpattern($tiles);
	$answer=0;
	foreach ($tiles as $row) {
		$answer+=array_sum($row);
	}
	echo "Day $day: $answer ($xmin,$ymin)-($xmax,$ymax)\n";
	//printpattern($tiles);
	//var_dump($tiles);
}
$answer=0;
foreach ($tiles as $row) {
	$answer+=array_sum($row);
}
echo "Day 100: $answer\n";
//Answer: 4059
function printpattern($tiles) {
	for ($y=$GLOBALS['ymin'];$y<=$GLOBALS['ymax'];++$y) {
		for ($i=($y-$GLOBALS['ymin']);$i>0;--$i) {
			echo " ";
		}
		for ($x=$GLOBALS['xmin'];$x<=$GLOBALS['xmax'];++$x) {
			if ($x==0&&$y==0) {
				echo (($tiles[$x][$y]??false)?"0 ":"H ");
			} else {
				echo (($tiles[$x][$y]??false)?"O ":"# ");
			}
		}
		echo "\n";
	}
}
?>
