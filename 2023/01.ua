$ 1abc2
$ pqr3stu8vwx
$ a1b2c3d4e5f
$ treb7uchet

# &fras"../inputs/2023/01.txt";
Words ← {"zero""one""two""three""four""five""six""seven""eight""nine"}
⊜□≠,@\n
⊃(
  ≡(⋕⊢⊢regex "\\d"°□)
| ≡(⋕⊢⊢regex "\\d"⇌°□)
| ≡(⍣⋕(⊗:Words;:)⊢⊢regex ⊂"\\d|"⊐/(⊂⊂:"|")Words°□)
| ≡(⍣⋕(⊗:Words;:)⇌⊢⊢regex ⊂"\\d|"⇌⊐/(⊂⊂:"|")Words⇌°□)
)
:∩(/++×10)
