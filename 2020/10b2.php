<?php
//error_reporting(E_ERROR | E_PARSE);
$input=file_get_contents("10.txt");
$inputs=explode("\n",$input,-1);
sort($inputs, SORT_NUMERIC);
$out=max($inputs)+3;
echo "in: 0 out: ".$out."\n";
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

function generate(array $list): \Generator
    {
        // Generate even partial combinations.
        $list = array_values($list);
        $listCount = count($list);
        for ($a = 0; $a < $listCount; ++$a) {
            yield [$list[$a]];
        }

        if ($listCount > 2) {
            for ($i = 0; $i < count($list); $i++) {
                $listCopy = $list;

                $entry = array_splice($listCopy, $i, 1);
                foreach (generate($listCopy) as $combination) {
                    yield array_merge($entry, $combination);
                }
            }
        } elseif (count($list) > 0) {
            yield $list;

            if (count($list) > 1) {
                yield array_reverse($list);
            }
        }
    }
//var_dump($inputs);
//pc_permute($inputs);
//echo "Start generate\n";
//$pc_permute=generate($inputs);
//var_dump($pc_permute);
//echo count($pc_permute);
//echo "End generate\n";
//foreach ($inputs as $key => $in) {}
$tested=0;
foreach (generate($inputs) as $chain) {
	$chain[]=$out;
	//echo implode(", ",$chain)."\n";
	$tested++;
	if (test_chain($chain)) {$total++;echo "good chain ".$total."/".$tested."\n";} //else {echo "bad chain\n";}
}
echo $total."\n";
//Answer:
?>
