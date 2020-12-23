<?php
//error_reporting(E_ERROR | E_PARSE);
$input=file_get_contents("23.txt");
//$input="389125467";
//$inputs=explode("\n",$input,-1);
$cups=str_split(str_replace("\n","",$input));
//foreach ($cups as $c) {}
$count=count($cups);
for ($i=0;$i<100;$i++) {
	/*/
	$current=$i%$count;
	echo "$current\n";
	$curr_val=$cups[$current];
	$lifted=[];
	switch ($current) {
		case $count:
			$lifted=array_splice($cups,0,3);
			break;
		case $count-1:
			$lifted[]=array_pop($cups);
			array_push($lifted,array_splice($cups,0,2));
			break;
		case $count-2:
			array_push($lifted,array_splice($cups,$count-1,2));
			$lifted[]=array_shift($cups);
			break;
		default:
			$lifted=array_splice($cups,$current+1,3);
			break;
	}
	$spuc=array_flip($cups);
	for ($search=$curr_val-1; true; --$search) {
		if (isset($spuc[$search])) {array_splice($cups,$spuc[$search],0,$lifted);break;}
		if ($search==0) {$search=10;}
	}
	var_dump($lifted);
	//*/
	echo implode("",$cups);
	$current=array_shift($cups);
	$lifted=array_splice($cups,0,3);
	$cups[]=$current;
	echo " ".implode("",$cups);
	$spuc=array_flip($cups);
	for ($search=$current-1; true; --$search) {
		if (isset($spuc[$search])) {array_splice($cups,$spuc[$search]+1,0,$lifted);echo " $search,$spuc[$search]";break;}
		if ($search==0) {$search=10;}
	}
	echo "\n";
}
$out=explode("1",implode("",$cups));
echo $out[1].$out[0]."\n";
//Answer: 45798623
?>
