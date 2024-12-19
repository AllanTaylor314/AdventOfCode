$ r, wr, b, g, bwu, rb, gb, br
$ 
$ brwrr
$ bggr
$ gbbr
$ rrbgbr
$ ubwu
$ bwurrg
$ brgr
$ bbrgwb
⍣(&fras"../inputs/2024/19.txt"◌)
⊜□⊸≠@\n
◇°/$"_, _"°⊂
⊸(/↥≡◇⧻)
LongestPattern ←
Patterns       ←
NumPatterns ← |1 memo(
  =0⊸⧻
  ⨬(⇌+1⇡↧+1LongestPattern⊃⧻¤
    /+≡(⨬(⋅0|NumPatterns)∊Patterns□⊃↙↘)
  | ⋅1
  )
)
# ◌⊸≡(/+≡(NumPatterns↘)⇌⇡◇⊃⧻¤) # Recursion Hack (for Pad)
≡◇NumPatterns
∩/+⟜≠₀
