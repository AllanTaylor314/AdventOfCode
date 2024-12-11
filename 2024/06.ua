Step ← (
  ◡+°⊟
  ⊙⊙(×[1 ¯1]⇌),
  ◡(⊡⋅⊙⋅⋅∘)
  ⨬⊙◌⋅∘↥0⊙∩⊟)
SaveLoc       ← ⊃(⊙∘|⍜(⊡)(⋅1)◌°⊟⊙⋅∘)
InRange       ← ≥0⊡◌°⊟
RotationIndex ← ⌊÷2/+×1_3+1
SaveLocRot    ← ⊃(⊙∘|⍜(⊡)(+1)⊂:RotationIndex°⊟⊙⋅∘)
HasNotVisited ← ¬⊡⊂:RotationIndex°⊟⊙⋅∘
$ ....#.....
$ .........#
$ ..........
$ ..#.......
$ .......#..
$ ..........
$ .#..^.....
$ ........#.
$ #.........
$ ......#...
⍣(&fras"../inputs/2024/06.txt"◌)
⌝↘¯[1 1]⌝↘[1 1]⊜∘⊸≠@\n
,,⊃(⊟[¯1 0]°¤⊚=@^|-⊃(=@ |=@#))
Start ←
Grid  ←
⊙⟜(×0)
⍢(Step SaveLoc|InRange)
⋅⋅⟜(/+♭)
⍜⊡⋅0◌°⊟Start
⊚
wait≡spawn(
  :Grid
  ⍜⊡⋅1
  Start
  ⊙⟜(↯:0⊂:4△)
  ⍢(Step SaveLocRot|×⊃InRange HasNotVisited)
  ¬HasNotVisited
)
/+
