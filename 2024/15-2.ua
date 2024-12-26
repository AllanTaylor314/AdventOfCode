Directions ← [¯1_0 0_1 1_0 0_¯1]
MoveUp ← (
  ,
  ⊸×₀
  ◡⋅⋅∘
  ⊸×/↥[⊸≡↻₁↻₁]⍜⊡⋅1      # Blocks affected by robot
  ⍥(⊸×/↥[⊸≡⊃↻₋₁↻₁⊸↻₁])∞ # Blocks by blocks
  ++⊃¯↻₁                # Move
  ⊃⋅⊙◌∘
  +¯1_0
)
MoveRight ← (
  +0_1
  ⟜(⍜(↘⊙⊡)(⍜(°□⊢⊜□)↻₁⊸(+1±⦷1_0)):°⊟)
)
MoveDown ← (
  ,
  ⊸×₀
  ◡⋅⋅∘
  ⊸×/↥[⊸≡↻₁↻₋₁]⍜⊡⋅1      # Blocks affected by robot
  ⍥(⊸×/↥[⊸≡⊃↻₋₁↻₁⊸↻₋₁])∞ # Blocks by blocks
  ++⊃¯↻₋₁                # Move
  ⊃⋅⊙◌∘
  +1_0
)
MoveLeft ← (
  +0_¯1
  ⟜(⍜(↙⊙⊡)(⍜(°□⊣⊜□)↻₁⊸(+1±⦷0_1)):°⊟)
)
WholeBoxes ← +⊸≡↻¯1
HasHitWall ← ↥⊃(⊡⊙⋅∘|/↥♭×WholeBoxes⋅⊙∘)
Step₂ ← (
  ⊗:Directions
  ⍣(⨬(MoveUp|MoveRight|MoveDown|MoveLeft)
    °0 ◡HasHitWall
  | ◌)
  °0◡(⊡⊙WholeBoxes) # Validate: Location doesn't collide with box
)
Display ← (
  ⊙⊙×₃₅
  ⊙(+⊓×₉₃×₉₁⊸≡↻¯1)
  ⊙(+×₄₆⊸=0+)
  ⍜⊡⋅64
  ≡°utf₈
  ≡&p
)
$ ##########
$ #..O..O.O#
$ #......O.#
$ #.OO..O.O#
$ #..O@..O.#
$ #O#..O...#
$ #O..O..O.#
$ #.OO.O.OO#
$ #....O...#
$ ##########
$ 
$ <vv>^<v^>v>^vv^v>v<>v^v<v<^vv<<<^><<><>>v<vvv<>^v^>^<<<><<v<<<v^vv^v>^
$ vvv<<^>^v^^><<>>><>^<<><^vv^^<>vvv<>><^^v>^>vv<>v<<<<v<^v>^<^^>>>^<v<v
$ ><>vv>v^v^<>><>>>><^^>vv>v<^^^>>v^v^<^^>v^^>v^<^v>v<>>v^v^<v>v^^<^^vv<
$ <<v<^>>^^^^>>>v^<>vvv^><v<<<>^^^vv^<vvv>^>v<^^^^v<>^>vvvv><>>v^<<^^^^^
$ ^><^><>>><>^^<<^^v>>><^<v>^<vv>>v>>>^v><>^v><<<<v>>v<v<v>vvv>^<><<>^><
$ ^>><>^v<><^vvv<^^<><v<<<<<><^v<<<><<<^^<v<^^^><^>>^<v^><<<^>>^v<v^v<v^
$ >^>>^v>vv>^<<^v<>><<><<v<<v><>v<^vv<<<>^^v^>^^>>><<^v>>v^v><^^>>^<>vv^
$ <><^^>^^^<><vvvvv^v<v<<>^v<v>v<<^><<><<><<<^^<<<^<<>><<><^^^>^^<>^>v<>
$ ^^>vv<^v^v<vv>^<><v<^v>^^^>>>^^vvv^>vvv<>>>^<^>>>>>^<<^v>^vvv<>^<><<v>
$ v^^>>><<^^<>>^v^<v^vv<>v^<<>^<^v^v><^<<<><<^<v><v<>vv>>v><v^<vv<>v^<<^
⍣(&fras"../inputs/2024/15.txt"◌)
:°$"_\n\n_"
⊓(⊏:Directions⊗:"^>v<"▽⊸≠@\n
| ⊜∘⊸≠@\n
  °¤⊚°⊟₃⊞="@O#"
)
⊓(∘|$Location₂×1_2|$Blocks₂⍜°⍉⍜△⍜↙₂/×⊟⟜×₀|$Walls₂≡▽2)
∧Step₂
⋅⊙◌
/+♭×[100_1]⊚
