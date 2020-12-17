<?php
//error_reporting(E_ERROR | E_PARSE);
$input=file_get_contents("15.txt");
//$input="0,3,6";
$seq=explode(",",str_replace("\n","",$input));
echo $input;
for ($i=count($seq);$i<2020;$i++) {
	$prev=array_pop($seq);
	if (in_array($prev, $seq)) {
		$new=$i-array_flip($seq)[$prev]-1;
	} else {
		$new=0;
	}
	echo ",$new";
	$seq[]=$prev;
	$seq[]=$new;
}
echo "\n";
//Answer: 517
?>
