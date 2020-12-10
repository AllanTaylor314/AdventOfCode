<?php
//error_reporting(E_ERROR | E_PARSE);
$input=file_get_contents("10.txt");
$inputs=explode("\n","0\n".$input,-1);
sort($inputs, SORT_NUMERIC);
$out=max($inputs)+3;
$inputs[]=$out;
//echo "in: 0 out: ".$out."\n";
$total=0;
function test_chain($chain) {
	$j=0;
	foreach ($chain as $i) {
		switch ($i-$j) {
			case 1:
			case 2:
			case 3:
				break;
			default:
				return false;
		}
		$j=$i;
	}
	return true;
}

function generate_chain($startkey) {
	$inputs=$GLOBALS['inputs'];
	//$map=array_keys($inputs);
	//$len=count($inputs);
	//foreach ($map as $index => $key) {}
	foreach ($GLOBALS['possible_nexts'][$startkey] as $next) {
		if (isset($GLOBALS['possible_nexts'][$next])) {
			foreach (generate_chain($next) as $chain) {
				//var_dump($chain);
				array_unshift($chain, $next);
				yield $chain;
			}
		} else {
			yield [$next];
		}
	}
}

function generate_all_chains($key) {
	$inputs=$GLOBALS['inputs'];
	//$map=array_keys($inputs);
	$len=count($inputs);
	//foreach ($map as $index => $key) {}
	//$index=0;
	//$key=0;
	//echo $index."\n";
	//$index++;
	//yield $chain;
}

$possible_nexts=[];
foreach ($inputs as $key => $value) {
	for ($newkey=$key+1; ($inputs[$newkey]-$value)<4 && $newkey<($key+4); $newkey++) {
		if (isset($inputs[$newkey]) && ($inputs[$newkey]-$value)<4) {
			$possible_nexts[$value][]=(int)$inputs[$newkey];
		}
	}
}
var_dump($possible_nexts);
$tested=0;
foreach (generate_chain(0) as $chain) {
	//$chain[]=$out;
	//echo implode(", ",$chain)."\n";
	$total++;
	echo $total."\r";
	//echo $total."\n";
	//if (test_chain($chain)) {$total++;echo "good chain ".$total."/".$tested."\n";} //else {echo "bad chain\n";}
}
echo $total."\n";
//Answer: 7^8*2^(6+2*7)
//1 Break into sets of consecutive numbers
//2 Count size of sets as follows:
//  5 - *7
//  4 - *4
//  3 - *2
//Answer: 6044831973376, so this code was never going to get there. ever.
?>
