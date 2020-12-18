<?php
//error_reporting(E_ERROR | E_PARSE);
$input=file_get_contents("18.txt");
$inputs=explode("\n",$input,-1);
$total=0;
foreach ($inputs as $i) {
	echo $i."\n";
	$curr=calc(str_replace(" ","",$i));
	echo $curr."\n\n";
	$total+=$curr;
}
echo $total."\n";
//Answer: 145575710203332

function calc($expression) {
	$split=str_split($expression);
	$opp="+";
	$c=count($split);
	$running_total=0;

	$key=array_search("(",$split);
	while($key!==false) {
		$emex="";
		$still_searching=true;
		$depth=1;
		$j=$key;
		while ($still_searching&&$j<$c) {
			$j++;
			switch ($split[$j]) {
				case '(':
					$depth++;
					$emex=$emex.'(';
					break;
				case ')':
					$depth--;
					if ($depth==0) {
						$still_searching=false;
					} else {
						$emex=$emex.')';
					}
					break;
				default:
					$emex=$emex.$split[$j];
					break;
			}
			unset($split[$j]);
		}
		$split[$key]=calc($emex);
		$split=array_values($split);
		var_dump($split[$key]);
		$key=array_search("(",$split);
	}

	$key=array_search("+",$split);
	while($key!==false) {
		$split[$key]=$split[$key-1]+$split[$key+1];
		unset($split[$key-1]);
		unset($split[$key+1]);
		$split=array_values($split);
		$key=array_search("+",$split);
	}
	//echo "return ".implode("",$split).";\n";
	return eval("return ".implode("",$split).';');;
}

?>
