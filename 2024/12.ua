RotR  ← ≡⬚0↻¯1
RotL  ← ≡⬚0↻1
RotU  ← ⬚0↻1
RotD  ← ⬚0↻¯1
Flood ← (
  ↥×⊙=⊸∩RotR,,
  ↥×⊙=⊸∩RotL,,
  ↥×⊙=⊸∩RotU,,
  ↥×⊙=⊸∩RotD,,
)
0
$ RRRRIICCFF
$ RRRRIICCCF
$ VVRRRCCFFF
$ VVRCCCJFFF
$ VVVVCJJCFE
$ VVIVCCJJEE
$ VVIIICJJEE
$ MIIIIIJJEE
$ MIIISIJEEE
$ MMMISSJEEE
⍣(&fras"../inputs/2024/12.txt"◌)
⊜∘⊸≠@\n
↯:0⊸△
⍢(⊙⊙+₁
  ⍜⊡⋅,⊢⊚⊸=0
  ⍥Flood∞
| ∈⊓♭0)
⊕⧻⊛.♭.
⌝↘¯[1 1]⌝↘[1 1],
⊃(⊃(∩⍉⊸RotR|∩⍉⊸RotL|⊸RotU|⊸RotD)
  /+[∩₄(↘1⊕⧻.♭⊜⊢.×⊸≠)]
| ⊃(⊸RotR|⊸RotL|⊸RotU|⊸RotD)
  /+[∩₄(↘1⊕⧻.♭×⊸≠)]
)
∩(/+×)⊙,
⊙⊙⋅⋅◌
