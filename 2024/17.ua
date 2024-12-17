GetOperand  ← ⊡+₁
GetCombo    ← ⨬(∘|⊡⊙⋅⋅∘-4)⊸≥₄◡GetOperand
SetRegister ← ⊃(⋅⋅⊙∘|⍜⊙⊡⊙◌:⊙⊙⋅⋅∘)
GetRegister ← ⊡⊙⋅⋅∘
Step ← (
  ◡⊡
  ⨬(◡⊃(GetCombo|GetRegister0)
    ⍜⊙⋯↘
    SetRegister0
    +2
  | ◡⊃(GetOperand|GetRegister1)
    °⋯/≠⬚0⊟∩⋯
    SetRegister1
    +2
  | ◡GetCombo
    ◿8
    SetRegister1
    +2
  | ◡(≠0GetRegister0)
    ⨬(+2|⊙◌◡GetOperand)
  | ◡⊃(GetRegister1|GetRegister2)
    °⋯/≠⬚0⊟∩⋯
    SetRegister1
    +2
  | ◡GetCombo
    ◿8
    ⊃(⋅⊙⊙∘|⊂:⊙⋅⋅⋅∘)
    +2
  | ◡⊃(GetCombo|GetRegister0)
    ⍜⊙⋯↘
    SetRegister1
    +2
  | ◡⊃(GetCombo|GetRegister0)
    ⍜⊙⋯↘
    SetRegister2
    +2
  )
)
$ Register A: 2024
$ Register B: 0
$ Register C: 0
$ 
$ Program: 0,3,5,4,3,0
⍣(&fras"../inputs/2024/17.txt"◌)
⊜⋕×⊸⊃(≥@0|≤@9)
⊃↘₃↙₃
Program   ←
Registers ←
RunProgram ← (
  0Program:[]
  ⍢(Step|>⊙⧻)
  ⋅⋅◌
)
RunProgram Registers
/$"_,_"
&pf⊂:@\n

0
⍥(
  ♭⊞+⇡8×8
  ▽⊸≡(
    RunProgram⇌[0 0 ∘]
    ≍↙:Program¯⊸⧻)
)⧻ Program
▽⊸≡(≍Program RunProgram⇌[0 0 ∘])
/↧
