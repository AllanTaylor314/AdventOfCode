from Intcode import Intcode, load_intcode

ic9_code = load_intcode('09.txt')
ic9=Intcode(ic9_code)
ic9.input(1)
ic9.run()
print('9.1 - diagnostic test')
while ic9.has_output(): # Should only be one code
    print(ic9.output())

ic9=Intcode(ic9_code)
ic9.input(2)
ic9.run()
print('9.2 - Coordinates:',ic9.output())