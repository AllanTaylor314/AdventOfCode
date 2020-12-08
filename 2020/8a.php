<?php
error_reporting(E_ERROR | E_PARSE);
$input=file_get_contents("8.txt");
$inputs=explode("\n",$input,-1);
foreach ($inputs as $i) {
	$instructions[]=explode(" ", $i);
}
$index=0;
$acc=0;
//echo isset($instructions[$index][2])?"t":"f";
while (!isset($instructions[$index][2])) {
	echo "b".$index.",".$acc.",".$instructions[$index][2]."\n";
	$instructions[$index][2]=1;
	exec_ins($instructions[$index]);
	echo "a".$index.",".$acc.",".$instructions[$index][2]."\n";
}
//var_dump($instructions);
echo $acc."\n";
//Answer:
function exec_ins($instruction) {
	switch ($instruction[0]) {
		case 'nop':
			$GLOBALS['index']++;
			break;
		case 'acc':
			$GLOBALS['acc']+=(int)$instruction[1];
			$GLOBALS['index']++;
			break;
		case 'jmp':
			$GLOBALS['index']+=(int)$instruction[1];
			break;
	}
	echo $GLOBALS['index'].",".$GLOBALS['acc'];
}
?>
