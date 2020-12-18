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
//Answer:

function calc($expression) {
	$split=str_split($expression);
	$opp="+";
	$c=count($split);
	$running_total=0;
	for ($j=0;$j<$c;$j++) {
		$value=$split[$j];
		//if (isset($j)&&$j<$key) {continue;}
		switch ($value) {
			case '+':
				$opp="+";
				break;
			case '*':
				$opp="*";
				break;
			case '(':
				$emex="";
				$still_searching=true;
				$depth=1;
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
				}
				echo $emex."\n";
				$calc=calc($emex);
				//var_dump($calc);
				//echo $running_total.$opp.$calc.";\n";
				//var_dump($running_total);
				$running_total=eval("return ".$running_total.$opp.$calc.';');
				break;
			case ')':
				return $running_total;
				break;
			default:
				$code=$running_total.$opp.$value.";\n";
				//echo "#".$code;
				var_dump($running_total);
				$running_total=eval("return ".$code);
				break;
		}
	}
	//$running_total=$expression[0]; //Nope (
	return $running_total;
}

?>
