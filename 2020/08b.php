<?php
//error_reporting(E_ERROR | E_PARSE);
$input=file_get_contents("8.txt");
$inputs=explode("\n",$input,-1);
foreach ($inputs as $i) {
	$rawinstructions[]=explode(" ", $i);
}
$inscount=count($rawinstructions);
for ($replindex=$inscount-1; $replindex>-1;$replindex--) {
	$instructions=$rawinstructions;
	//echo $instructions[$replindex][0];
	if ($instructions[$replindex][0]=="jmp") {
		$instructions[$replindex][0]="nop";
		//echo "replaced jmp on line ".$replindex."\n";
	} elseif ($instructions[$replindex][0]=="nop") {
		$instructions[$replindex][0]="jmp";
		//echo "replaced nop on line ".$replindex."\n";
	} else {
		//echo "continue";
		continue;
	}
	$index=0;
	$acc=0;
	while (!isset($instructions[$index][2])) {
		//echo "b".$index.",".$acc.",".$instructions[$index][2]."\n";
		$instructions[$index][2]=1;
		exec_ins($instructions[$index]);
		//echo "a".$index.",".$acc.",".$instructions[$index][2]."\n";
		if ($index==$inscount) {
			echo $acc."\n";
			exit();
		}
	}
}

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
	//echo $GLOBALS['index'].",".$GLOBALS['acc'];
}
?>
