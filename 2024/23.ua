SetIntersect ← ▽⊸∊
$ kh-tc
$ qp-kh
$ de-cg
$ ka-co
$ yn-aq
$ qp-ub
$ cg-tb
$ vc-aq
$ tb-ka
$ wh-tc
$ yn-cg
$ kh-ub
$ ta-co
$ de-co
$ tc-td
$ tb-wq
$ wh-td
$ ta-ka
$ td-qp
$ aq-cg
$ wq-ub
$ ub-vc
$ de-ta
$ wq-aq
$ wq-vc
$ wh-yn
$ ka-de
$ kh-ta
$ co-tc
$ wh-qp
$ tb-vc
$ td-yn
⍣(&fras"../inputs/2024/23.txt"◌)
⊜[°$"_-_"]⊸≠@\n
⊂≡⇌.
⊙(map[][])
≡≡□
∧(⍜(°□⬚{}get)⊂⊙:°⊟)
Adjacency ←
IsClique ← (
  /↧♭⊞(↥⊃(=|∊°□get:Adjacency)).
)
⊙◌°mapAdjacency
⊸▽=@t⊸≡◇⊢
⊞(□≡[⊙⊙∘]◡(◇SetIntersect∩(get:Adjacency)))
/◇⊂♭
◴≡⍆
▽⊸(=3≡(/+◰))
/+≡IsClique
BronKerbosch ← |4.2 (
  ⊓($R|$P|$X)
  ×∩(=0⧻)◡⋅⊙∘
  ⨬($Maximal[]
    ⍥(
      ⊙(
        $V⊢,
        ◡⊃(⊂|◇SetIntersect ⊙⋅◌ get:Adjacency|◇SetIntersect ⊙⋅⋅◌ get:Adjacency)
        BronKerbosch
      )
      ⨬(⋅∘|⊙◌)<◡∩⧻
      ⊙(
        ⊃(⋅∘|▽≠,⊙⋅∘|⊂⊙⋅⋅∘)
      )
    )◡⋅⋅⧻
    ⊙⋅⋅◌
  | ⊙⋅◌
  )
)
BronKerbosch [] ⊙◌°mapAdjacency []
/$"_,_"⍆
