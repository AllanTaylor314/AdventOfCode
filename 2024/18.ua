Directions ← [¯.⇌.¯.1_0]
12 7
$ 5,4
$ 4,2
$ 4,5
$ 3,0
$ 2,1
$ 6,3
$ 2,4
$ 1,5
$ 0,6
$ 3,3
$ 2,6
$ 5,1
$ 1,2
$ 5,5
$ 2,5
$ 6,5
$ 1,4
$ 0,4
$ 6,4
$ 1,1
$ 6,1
$ 1,0
$ 0,5
$ 1,6
$ 2,0
⍣(&fras"../inputs/2024/18.txt"1024 70⋅⋅◌)
:⊜([∩⋕]°$"_,_")⊸≠@\n
Simulate ← (
  ⟜(⬚1↯+1)[.]:¬°⊚↙
  0_0
  ◌path(↯:1⊸⧻⊙◌▽◡⬚0⊡⊙⋅∘+Directions¤|≍)
)
BinSearch ← |4.4 (
  +1⌊÷2◡+
  ◡(Simulate ⊙⋅⋅∘)
  =∞
  ⨬(⊙⋅∘|⊙⊙◌:-1)
)
⊃(/$"_,_"⊡⋅⊙⊙◌⍢(BinSearch|≠)0-1⊸⋅⧻|Simulate)
