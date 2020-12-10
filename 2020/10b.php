<?php
//error_reporting(E_ERROR | E_PARSE);
$input=file_get_contents("10.txt");
$inputs=explode("\n","0\n".$input,-1);
sort($inputs, SORT_NUMERIC);
$out=max($inputs)+3;
$inputs[]=$out;
//echo "in: 0 out: ".$out."\n";
$total=1; //Multiplying
/*
$possible_nexts=[];
foreach ($inputs as $key => $value) {
	for ($newkey=$key+1; ($inputs[$newkey]-$value)<4 && $newkey<($key+4); $newkey++) {
		if (isset($inputs[$newkey]) && ($inputs[$newkey]-$value)<4) {
			$possible_nexts[$value][]=(int)$inputs[$newkey];
		}
	}
}*/
//var_dump($possible_nexts);
$currgrouplen=0;
//$loops=count($inputs)+3;
$g3=0;$g4=0;$g5=0;
for ($index=0;$index<$out;$index++) {
	if (in_array($index, $inputs)) {
		$currgrouplen++;
		echo $index.",";
	} else {
		switch ($currgrouplen) {
			case 5:
				$total*=7; //2^(n-2)-1
				$g5++;
				break;
			case 4:
				$total*=4; //2^(n-2)
				$g4++;
				break;
			case 3:
				$total*=2; //2^(n-2)
				$g3++;
				break;
			default:
				// code...
				break;
		}
		echo "(".$currgrouplen.")\n";
		$currgrouplen=0;
	}
}

echo "((7**".$g5.")*(2**(2*".$g4."+".$g3.")))=".$total."\n";
//Answer: 7^8*2^(6+2*7)
//1 Break into sets of consecutive numbers
//2 Count size of sets as follows:
//  5 - *7
//  4 - *4
//  3 - *2
//Answer: 6044831973376, so this code was never going to get there. ever.
?>
