a = int(input("a"))
k = 1
for i in range(1, 11):
    i*=a
    y=1/pow(a,3)*pow(k,2)
    print(y)


c = int(input("c"))
k = 1
for i in range(1, 11):
    i*=c
u=1/pow(c,2)*pow(k,3)
print(u)

b = int(input("b"))
k = 1
for i in range(1, 11):
    i*=b
u=pow(b,2)/pow(k,2/3)
print(u)

import math
d = int(input("d"))
k = 1
for i in range(1, 11):
    i*=d
u=pow((-1),k) / math.sqrt(abs(d))+pow(k,2)
print(u)


import math
e = int(input("e"))
k = 1
for i in range(1, 11):
    i*=e
u=math.sqrt(abs(pow(e,2)))/pow(k,3)
print(u)


import math
g = int(input("g"))
k = 1
for i in range(1, 11):
    i*=g
u=g/pow(k,3)+k*math.sqrt(abs(g))+1
print(u)