import sys, codecs
from random import randint as r
sys.stdout = codecs.getwriter('utf_16')(sys.stdout.buffer, 'strict')

h = 13
o = chr(128308), chr(9898)
t = chr(127876)
s = chr(127775)
f = ' ', chr(10052)
g = chr(127776)
p = chr(127873), ' ', ' ', chr(128717)
w = 32, 32, 32, 32, 0x1f13C, 0x1f134, 0x1f141, 0x1f141, 0x1f148, 32, 0x1f132, 0x1f137, 0x1f141, 0x1f138, 0x1f142, 0x1f143, 0x1f13C, 0x1f130, 0x1f142, 10, 32, 32, 32, 32, 32, 0x1f143, 0x1f13E, 32, 0x1f13C, 0x1f148, 32, 0x1f135, 0x1f13E, 0x1f13B, 0x1f13B, 0x1f13E, 0x1f146, 0x1f134, 0x1f141, 0x1f142, 10, 0x1f130, 0x1f13D, 0x1f133, 32, 0x1f130, 0x1f13B, 0x1f13B, 32, 0x1f142, 0x1f13E, 0x1f13B, 0x1f13E, 0x1f13B, 0x1f134, 0x1f130, 0x1f141, 0x1f13D, 0x1f134, 0x1f141, 0x1f142

for i in w:
    print(chr(i), end='')
print('\n'*2)
print(' '*h+s+r(5,10)*' '+g)
for i in range(1, h):
    print(' '*(h-i)+t*(i+1), end='')
    for j in range(20-i):
        print(f[r(0,20)//20], end='')
    print()
    print(' '*(h-i)+o[1-i%2]*(i+1))
print()
print('  ', end='')
for i in range(h):
    print(p[r(0,3)], end='')
