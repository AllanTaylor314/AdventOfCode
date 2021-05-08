import re

with open('09.txt', encoding='utf-8') as file:
    raw_data = file.read()

# ! cancels (removes) the next char
# Replace ! and the next char with nothing
escaped = re.sub(r'!.', '', raw_data)

# Replace open <, any non closing >, and > with nothing
filtered = re.sub(r'<[^>]*>', '', escaped)

score = 0
depth = 0
for c in filtered:
    if c == '{':
        depth += 1
    elif c == '}':
        score += depth
        depth -= 1
print('Part 1:', score)

# Part 2 - number of garbage letters removed, except cancelled letters and <>
#                    Get the diff of letters   cancel the <> (twice the >)
print('Part 2:', len(escaped) - len(filtered) - 2 * escaped.count('>'))
