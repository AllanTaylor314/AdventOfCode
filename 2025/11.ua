# Part 2 example, with extra top line
# so Part 1 doesn't crash
$ you: svr
$ svr: aaa bbb
$ aaa: fft
$ fft: ccc
$ bbb: tty
$ tty: ccc
$ ccc: ddd eee
$ ddd: hub
$ hub: fff
$ eee: dac
$ dac: fff
$ fff: ggg hhh
$ ggg: out
$ hhh: out
⍣(&fras"../inputs/2025/11.txt"◌|∘)
⊜□⊸≠@\n
⍚(⊜∘¬⊸∊": ")
map≡◇(⊃(⊢|□↘₁))
Map ←
F   ← |1 memo(⨬(/+◇≡F ˜get Map|1)⊸≍"out")
F "you"

G ← |3 memo(⨬(/+◇≡G⊃(˜get Map|↥≍"dac"|↥≍"fft"⊙⋅∘)|⋅×)⊸≍"out") # loc seen_dac seen_fft
G "svr" 0 0
