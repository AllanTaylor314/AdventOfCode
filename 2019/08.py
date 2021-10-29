with open('08.txt') as file:
    data = file.read()

WIDTH = 25
HEIGHT = 6
layers = []
image_size = WIDTH * HEIGHT
for i in range(len(data) // image_size):
    offset = i * image_size
    layers.append(data[offset:offset + image_size])
num_zeros, mul12 = [], []
for layer in layers:
    num_zeros.append(layer.count('0'))
    mul12.append(layer.count('1') * layer.count('2'))
print('Part 1:', mul12[num_zeros.index(min(num_zeros))])
# 1755 too high
# 1742

master = list('2' * image_size)
for layer in layers[::-1]:
    for i, c in enumerate(layer):
        if c == '2':
            continue
        else:
            master[i] = c
master = "".join(master).replace('0', ' ').replace('1', 'O')
print('Part 2:')
for i in range(HEIGHT):
    print(master[i * WIDTH:(i + 1) * WIDTH])
# Part 2: GJYEA
