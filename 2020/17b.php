<?php
//error_reporting(E_ERROR | E_PARSE);
$input=file_get_contents("17.txt");
$inputs=explode("\n",$input,-1);
$pd=[];
//$pd[x][y][z][w]
$x=0;
$y=0;
$z=0;
$w=0;
//Initialise Grid
foreach ($inputs as $y => $i) {
	foreach (str_split($i) as $x => $state) {
		if ($state=="#") {
			$pd[$x][$y][$z][$w]=true;
		}
	}
}
//var_dump($pd);
for ($c=0;$c<6;$c++) {
	$sg=$pd;
	for ($x=-8;$x<16;$x++) {
		for ($y=-8;$y<16;$y++) {
			for ($z=-8;$z<8;$z++) {
				for ($w=-8;$w<8;$w++) {
					$count=0;
					for ($xd=-1;$xd<2;$xd++) {
						for ($yd=-1;$yd<2;$yd++) {
							for ($zd=-1;$zd<2;$zd++) {
								for ($wd=-1;$wd<2;$wd++) {
									if ($xd==0 && $yd==0 && $zd==0 && $wd==0) {continue;}
									if (isset($sg[$x+$xd][$y+$yd][$z+$zd][$w+$wd]) && $sg[$x+$xd][$y+$yd][$z+$zd][$w+$wd]) {$count++;}
								}
							}
						}
					}
					if ($count==3) {$pd[$x][$y][$z][$w]=true;}
					elseif ($count==2 && isset($pd[$x][$y][$z][$w]) && $pd[$x][$y][$z][$w]) {} //No change
					else {unset($pd[$x][$y][$z][$w]);}
				}
			}
		}
	}
}
$total=0;
foreach ($pd as $x => $yz) {
	foreach ($yz as $y => $z) {
		foreach ($z as $w) {
			$total+=count($w);
		}
	}
}

//var_dump($pd);
echo "$total\n";
//Answer: 2136
?>
