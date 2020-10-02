import numpy as np
from pwn import *

r = remote("localhost", 1337)
hehe = np.random.randint(10,size=1)
print(hehe)
