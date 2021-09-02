# -*- coding: utf-8 -*-

import sys

# required task #2
def is_prime(x):
    if x == 2:
        return True
    elif x%2==0:
        return False
    else:
        for a in range(2, int(x**(1/2))+1):
            if x%a==0:
                return False
        return True

# problem 7
num=2
count=0
while(count<10001):
    if is_prime(num):
        count+=1
    num+=1
        
print("problem 7: %s" % (num-1))

# problem 1
print("problem 1: %s" % sum(x for x in range(1000) if x%3==0 or x%5==0))

# problem 2  
def fib(a):
     x, y = 0, 1
     sum=0
     while y < a:
         x,y = y, x+y
         if y%2==0:
             sum+= y
     return sum
print("problem 2: %s" % fib(4000000))

# problem 3
def primeLarge(a):
    factor=1
    temp = a
    for x in range(2, int(a**(1/2))+1):
        while(temp%x==0):
            factor = x
            temp = temp/x
    return factor
print("problem 3: %s" % primeLarge(600851475143))

# problem 4
max=0
for x in range(999, 99, -1):
    for y in range(999, 99, -1):
        if str(x*y)==str(x*y)[::-1]:
            if max < (x*y):
                max=(x*y)
print("problem 4: %s" % max)

# problem 8
num = list("731671765313306249192251196744265747423553491949349698352031277450632623957831801698480186947885184385861560789112949495459501737958331952853208805511125406987471585238630507156932909632952274430435576689664895044524452316173185640309871112172238311362229893423380308135336276614282806444486645238749035890729629049156044077239071381051585930796086670172427121883998797908792274921901699720888093776657273330010533678812202354218097512545405947522435258490771167055601360483958644670632441572215539753697817977846174064955149290862569321978468622482839722413756570560574902614079729686524145351004748216637048440319989000889524345065854122758866688116427171479924442928230863465674813919123162824586178664583591245665294765456828489128831426076900422421902267105562632111110937054421750694165896040807198403850962455444362981230987879927244284909188845801561660979191338754992005240636899125607176060588611646710940507754100225698315520005593572972571636269561882670428252483600823257530420752963450")
max=0
prod=1
for x in range((len(num))-12):
    for a in num[x:x+13]:
        prod= prod*int(a)
    if max < prod:
        max = prod
    prod=1
print("problem 8: %s" % max)

# problem 9
def pytha():
    for a in range(500):
        for b in range(500):
            c=((a**2)+(b**2))**(1/2)
            if (a+b+c)==1000:
                return a*b*c
print("problem 9: %s" % int(pytha()))

    