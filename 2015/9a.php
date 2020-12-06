<?php
error_reporting(E_ERROR | E_PARSE);
$pc_permute="";
function pc_permute($items, $perms = array()) {
    if (empty($items)) {
        //echo join(' ', $perms) . "\n";
        $GLOBALS['pc_permute']=$GLOBALS['pc_permute'].join(' ', $perms) . "\n";
				//var_dump($perms);
    } else {
        for ($i = count($items) - 1; $i >= 0; --$i) {
             $newitems = $items;
             $newperms = $perms;
             list($foo) = array_splice($newitems, $i, 1);
             array_unshift($newperms, $foo);
             pc_permute($newitems, $newperms);
         }
    }
}

//$arr = array('peter', 'paul', 'mary');

//pc_permute($arr);

$input=file_get_contents("9.txt");
$inputs=explode("\n",$input,-1);
$map=[];
foreach ($inputs as $i) {
	$x=explode(" ",$i);
	$map[$x[0]][$x[2]]=$x[4];
	$map[$x[2]][$x[0]]=$x[4];
}
pc_permute(array_keys($map));
$permutations=explode("\n",$pc_permute,-1);
//var_dump($pc_permute);
//var_dump($permutations);
$mindist=99999999999999999999;
foreach ($permutations as $perm) {
	$dist=0;
	$order=explode(" ",$perm);
	//var_dump($order);
	for ($j=count($order)-1;$j>=0;$j--) {
		//echo $map[$order[$j]][$order[$j+1]]."\n";
		$dist+=(int)$map[$order[$j]][$order[$j+1]];
	}
	//echo $dist."\n";
	if ($dist<$mindist && $dist>0) {
		$mindist=$dist;
		$route=$perm;
	}
}
//echo $pc_permute;
//var_dump($map);
echo $route." - ".$mindist."\n";
//Answer: 251
?>
