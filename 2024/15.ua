Directions ← [¯1_0 0_1 1_0 0_¯1]
Step₁ ← (
  ⊡:Directions
  ◡(∊:⊓+⋅⊚)
  ⨬(◡(⊡+)
    ⨬(+ # Neither wall nor block - simple step
    | ◡⊓+∘
      ⍢(+◡⋅⋅∘|⊡)
      ◡⊙⋅⋅⋅⋅∘
      ⊡
      ⨬(⊙⋅+
        ⊙⟜⍜⊡⋅0 # Toggle first block off
        ⊙⍜⊡⋅1: # and last block on
      | ⋅⋅◌    # Would push into wall - do nothing
      )
    )
  | ◌ # Bot hits wall - do nothing
  )
)

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
  ⍣(⨬(MoveUp|MoveRight|MoveDown|MoveLeft)
    °0 ◡HasHitWall
  | ◌)
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
⊓(⊗:"^>v<"▽⊸≠@\n
| ⊜∘⊸≠@\n
  °¤⊚°⊟₃⊞="@O#"
)
⊃(∧Step₂⊙⊓(×1_2|⍜(↙₂△°⍉)/×⊟⟜×₀|≡▽2)|∧Step₁)
∩(/+♭×[100_1]⊚⋅⊙◌)
