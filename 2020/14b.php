<?php
//error_reporting(E_ERROR | E_PARSE);
$input=file_get_contents("14.txt");
$inputs=explode("\n",$input,-1);
$steps=[];
$mem=[];
foreach ($inputs as $i) {
	if ($i[1]=="a") { //as in MaSK
		$mask=str_replace("mask = ","",$i);
	} else {
		$parsed=explode("] = ",str_replace("mem[","",$i));
		//$mem[$parsed[0]]=apply_mask((int)$parsed[1],$mask);
		update_mem($parsed[0],$mask,$parsed[1]);
	}
}
/*/
foreach ($steps as $key => $step) {
	$mask=array_shift($step);
	foreach ($step as $instruction) {
		$parsed=explode("] = ",str_replace("mem[","",$instruction));
		var_dump($parsed);
	}
}//*/
echo array_sum($mem)."\n";
//var_dump($mem);
//Answer: 4795970362286
function apply_mask($init,$mask)
{
	//echo "$mask\n";
	$bin=sprintf( "%036b",$init);
	//var_dump($bin);
	foreach (str_split($mask) as $index => $m) {
		if ($m=="X") {
			// Do nothing
		} else {
			$bin[$index]=$m;
		}
	}
	//var_dump($mask);
	//var_dump($bin);
	return bindec($bin);
}

function update_mem($address, $mask, $value) {
	// 1 overwrites with 1
	// 0 no change
	// X float - all values


	//apply ones:
	//var_dump($address);
	//echo sprintf( "%036b",decbin($address))."\n";
	//echo $mask."\n";
	//echo str_replace("X","0",$mask)."\n";
	//$numask=bindec(str_replace("X","0",$mask));
	//var_dump($numask);
	//echo sprintf( "%036b",decbin($numask))."\n";
	//echo bindec(str_replace("X","0",$mask))."\n";
	//echo decbin($mask)."\n";
	//$address=$address|$numask;
	//echo sprintf( "%036b",decbin($address))."\n\n";
	//echo "63-".sprintf("%036b",decbin($address))."\n";
	//$newaddresses=get_address(sprintf("%036b",decbin($address)), $mask);
	foreach (get_address(sprintf("%036b",$address), $mask) as $newaddress) {
		//echo bindec($newaddress)."\n";
		$GLOBALS['mem'][bindec($newaddress)]=(int)$value;
	//	echo "N:".$newaddress." (".bindec($newaddress).")\n";
	}
	//echo "A:".sprintf("%036b",$address)." (".bindec(sprintf("%036b",$address)).")\nM:".$mask."\n";
}

function get_address($address,$mask,$index=0) {
	//echo $address;
	if ($index==36) {
		yield "";
	} else {
		$no_change=str_split($address)[$index];
		//echo "L:".strlen($address)." i:".$index." c:".$no_change."\n";
		foreach (get_address($address,$mask,$index+1) as $suffix) {
			//echo "S:$suffix\n";
			//var_dump($suffix);
			switch ($mask[$index]) {
				case 'X':
			//		echo "0:$suffix\n";
					yield '0'.$suffix;
			//		echo "1:$suffix\n";
					yield '1'.$suffix;
					break;
				case '1':
			//		echo "1-$suffix\n";
					yield '1'.$suffix;
					break;
				case '0':
			//		echo $no_change."/$suffix\n";
					//var_dump($address);
					yield $no_change.$suffix;
					break;
			}
		}
	}
}
?>
