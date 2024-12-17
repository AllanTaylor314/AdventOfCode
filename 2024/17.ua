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
$Output[]
$ Register A: 729
$ Register B: 0
$ Register C: 0
$ 
$ Program: 0,1,5,4,3,0
⍣(&fras"../inputs/2024/17.txt"◌)
⊜⋕×⊸⊃(≥@0|≤@9)
⊃↘₃↙₃
⊓$Program$Registers
$InstructionPointer0
⍢(Step|>⊙⧻)
⋅⋅⋅/$"_,_"
&pf⊂:@\n
