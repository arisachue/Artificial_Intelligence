# -*- coding: utf-8 -*-

import sys

x = str(sys.argv[1])

if x == "A":
    print(sum([int(sys.argv[2]),int(sys.argv[3]),int(sys.argv[4])]))
    
elif x == "B":
    sum = 0
    for num in sys.argv[2:]:
        sum += int(num)
    print(sum)
    
elif x == "C":
    for num in sys.argv[2:]:
        if int(num)%3==0:
            print(num)
            
elif x == "D":
    def fib(num):
        if num <= 1:
            return num
        else:
            return(fib(num-1)+fib(num-2))
    n = int(sys.argv[2])
    if n <= 0:
        print("invalid number")
    else:
        for item in range(1,n+1):
            print(fib(item))
        
elif x == "E":
    for num in range(int(sys.argv[2]), int(sys.argv[3])+1):
        print((num**2)-(3*num)+2)
        
elif x == "F":
    a = float(sys.argv[2])
    b = float(sys.argv[3])
    c = float(sys.argv[4])
    if a+b<=c or a+c<=b or b+c<=a:
        print("error: invalid side lengths")
    else:
        p = (a+b+c)/2.0
        print((p*(p-a)*(p-b)*(p-c))**(1/2))
        
elif x == "G":
    l = {"a": 0, "e": 0, "i": 0, "o": 0, "u": 0}
    for item in str(sys.argv[2:]):
        if item.lower() == "a":
            l["a"]+=1
        elif item.lower() == "e":
            l["e"]+=1
        elif item.lower() == "i":
            l["i"]+=1
        elif item.lower() == "o":
            l["o"]+=1
        elif item.lower() == "u":
            l["u"]+=1
    for key, val in l.items():
        print(key, val)
    
else:
    print("error: invalid letter input")
    