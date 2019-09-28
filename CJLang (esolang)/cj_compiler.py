# Usage: python cj_compiler.py hello_world.cj

import sys

opcode = {
    'ah': 0,
    'shit': 1,
    'here': 2,
    'we': 3,
    'go': 4,
    'again': 5
}

filename = sys.argv[1]

f = open(filename, 'r')
r = f.read().strip()
data = r.split('cj')
dec_ops = []
for codes in data:
    codes = list(filter(lambda c: c != '', codes.split(' ')))
    codes_val = ''.join(list(map(lambda c: str(opcode[c]), codes)))
    rev_codes_val = codes_val[::-1]
    result = 0
    for i in range(len(rev_codes_val)):
        result += int(rev_codes_val[i]) * 6 ** i
    dec_ops += [result]

output = ''.join(list(map(lambda c: chr(c), dec_ops)))
print(output)
