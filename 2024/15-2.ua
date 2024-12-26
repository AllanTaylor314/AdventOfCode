Directions ← [¯1_0 0_1 1_0 0_¯1]
MoveUp ← (
  +¯1_0                 # Move the robot
  ,                     # Grab a copy of the blocks
  ⊸×₀                   # and make an array of zeros the same size
  ⊸×/↥[⊸≡↻₁]⍜⊡⋅1◡⋅⋅∘    # Blocks affected by robot
  ⍥(⊸×/↥[⊸≡⊃↻₋₁↻₁⊸↻₁])∞ # Blocks affected by blocks
  ++⊃¯↻₁                # Move all the blocks
  ⊃⋅⊙◌∘                 # Rearrange the stack
)
MoveRight ← (
  +0_1
  ⟜(⍜(↘⊙⊡)(⍜(°□⊢⊜□)↻₁⊸(+1±⦷1_0)):°⊟)
)
MoveDown ← (
  +1_0
  ⊸×/↥[⊸≡↻₁]⍜⊡⋅1◡⋅⋅∘⊸×₀,
  ⍥(⊸×/↥[⊸≡⊃↻₋₁↻₁⊸↻₋₁])∞
  ⊃⋅⊙◌∘++⊃¯↻₋₁
)
MoveLeft ← (
  +0_¯1
  ⟜(⍜(↙⊙⊡)(⍜(°□⊣⊜□)↻₁⊸(+1±⦷0_1)):°⊟)
)
WholeBoxes ← +⊸≡↻¯1
HasHitWall ← ↥⊃(⊡⊙⋅∘|/↥♭×WholeBoxes⋅⊙∘)
Step₂ ← (
  ⊗:"^>v<"
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
⊓(▽⊸≠@\n
| ⊜∘⊸≠@\n
  °¤⊚°⊟₃⊞="@O#"
)
⊓(∘|$Location₂×1_2|$Blocks₂⍜°⍉⍜△⍜↙₂/×⊟⟜×₀|$Walls₂≡▽2)
∧Step₂
⋅⊙◌
/+♭×[100_1]⊚
