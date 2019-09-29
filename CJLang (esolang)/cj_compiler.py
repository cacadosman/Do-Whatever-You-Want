# Usage: python cj_compiler.py <filename>

import sys
from functools import reduce

opcode = {
    'ah': 0,
    'shit': 1,
    'here': 2,
    'we': 3,
    'go': 4,
    'again': 5
}
dec_ops = []

filename = sys.argv[1]

f = open(filename, 'r')
data = f.read().strip().split('cj')

for codes in data:
    codes = list(
        filter(lambda c: c != '', codes.split(' '))
    )
    codes_val = ''.join(list(
        map(lambda c: str(opcode[c]), codes)
    ))
    rev_codes_val = codes_val[::-1]
    do_sum = lambda x,y: x + y

    dec_ops += [
        reduce(
            do_sum, [
                int(rev_codes_val[i]) * 6 ** i 
                for i in range(len(rev_codes_val))
            ]
        )
    ]

out = ''.join(list(map(lambda c: chr(c), dec_ops)))
print(out)
