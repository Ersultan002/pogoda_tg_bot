q = []
for x in range(1500, 2701):
    if (x % 7 == 0) and (x % 5 == 0):
        q.append(str(x))
print(', '.join(q))

w = input("Túrlendirgińiz keletin temperatýrany engizińiz? ( 45F nemese 102C ) : ")
e = int(w[:-1])
r = w[-1]
if r.upper() =="C":
  t = int(round((9 * e) / 5 + 32))
  y ="Fahrenheit"
elif r.upper() =="F":
  t = int(round((e - 32) * 5 / 9))
  y ="Celsius"
else:
  print("Durys kelisimdi engizińiz.")
  quit()
print("Temperatýra", y, "is", t, "dárejeler.")

import random
u, i = random.randint(1, 10), 0
while u != i:
    i = int(input('Durys tapqansha 1-den 10-ǵa deiingi sandy boljańyz :'))
print('Durys!')

print("* ")
print("* *  ")
print("* * *  ")
print("* * * *  ")
print("* * *  ")
print("* *  ")
print("* ")

o = input("Soz Engiziniz: ")
p = o[::-1]
print( p )

d = input("Bos oryndarmen bólingen sandar qataryn engizińiz: ")
d = list(map(int, d.split()))
a = 0
s = 0
for f in d:
    if f % 2 == 0:
        a += 1
    else:
        s += 1
print("Jup sandar sany:", a)
print("Taq sandar sany:", s)

g = [1452, 11.23, 1 + 2j, True, 'w3resource', (0, -1), [5, 12], {"class": 'V', "section": 'A'}]
for item in g:
    print(f"Элемент: {item}, Тип: {type(item)}")

for x in range(7):
    if x == 3 or x == 6:
        continue
    print(x, end=' ')


n1, n2 = 0, 1
while n1 < 50:
    print(n1, end=' ')
    n1, n2 = n2, n1 + n2

for num in range(1, 51):
    if num % 3 == 0 and num % 5 == 0:
        print('FizzBuzz')
    elif num % 3 == 0:
        print('Fizz')
    elif num % 5 == 0:
        print('Buzz')
    else:
        print(num)

m = int(input("Joldar sanyn engizińiz: "))
n = int(input("Baǵandar sanyn engizińiz: "))
array = [[0 for col in range(n)] for row in range(m)]
for i in range(m):
    for j in range(n):
        array[i][j] = i*j
for row in array:
    print(row)

while True:
    string = input("Joldy engizińiz (aiaqtaý úshin bos jol): ")
    if string == "":
        break
    print(string.lower())

k = input("Joldy engizińiz: ")
l = z = 0
for c in k:
    if c.isdigit():
        l = l + 1
    elif c.isalpha():
        z = z + 1
print("Письма", z)
print("Цифры", l)

import re
password = input("Введите пароль: ")
if len(password) < 6 or len(password) > 16:
    print("Недопустимая длина пароля")
elif not re.search("[a-z]", password):
    print("Пароль должен содержать как минимум 1 букву в нижнем регистре")
elif not re.search("[A-Z]", password):
    print("Пароль должен содержать как минимум 1 букву в верхнем регистре")
elif not re.search("[0-9]", password):
    print("Пароль должен содержать как минимум 1 цифру")
elif not re.search("[$#@]", password):
    print("Пароль должен содержать как минимум 1 символ из $, #, @")
else:
    print("Пароль прошел проверку")

result = []
for i in range(100, 401):
    s = str(i)
    if (int(s[0])%2==0) and (int(s[1])%2==0) and (int(s[2])%2==0):
        result.append(s)
print(",".join(result))

print(" *** ")
print("*   *")
print("*   *")
print("*****")
print("*   *")
print("*   *")
print("*   *")

print("****")
print("*   *")
print("*   *")
print("*   *")
print("*   *")
print("*   *")
print("****")

print("*****")
print("*")
print("*")
print("****")
print("*")
print("*")
print("*****")

print(" *** ")
print("*   *")
print("*")
print("* ***")
print("*   *")
print("*   *")
print(" *** ")

import math
import numpy as np

x = 1
y = 2
r = math.sqrt(x*y*math.sin(2*x) + (np.exp(2*x)*(x+y)/(x**2+y**2)))
print(r)
