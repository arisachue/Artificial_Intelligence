# -*- coding: utf-8 -*-

# =============================================================================
# problem 11
# =============================================================================
grid =  "08 02 22 97 38 15 00 40 00 75 04 05 07 78 52 12 50 77 91 08 " +\
        "49 49 99 40 17 81 18 57 60 87 17 40 98 43 69 48 04 56 62 00 " +\
        "81 49 31 73 55 79 14 29 93 71 40 67 53 88 30 03 49 13 36 65 " +\
        "52 70 95 23 04 60 11 42 69 24 68 56 01 32 56 71 37 02 36 91 " +\
        "22 31 16 71 51 67 63 89 41 92 36 54 22 40 40 28 66 33 13 80 " +\
        "24 47 32 60 99 03 45 02 44 75 33 53 78 36 84 20 35 17 12 50 " +\
        "32 98 81 28 64 23 67 10 26 38 40 67 59 54 70 66 18 38 64 70 " +\
        "67 26 20 68 02 62 12 20 95 63 94 39 63 08 40 91 66 49 94 21 " +\
        "24 55 58 05 66 73 99 26 97 17 78 78 96 83 14 88 34 89 63 72 " +\
        "21 36 23 09 75 00 76 44 20 45 35 14 00 61 33 97 34 31 33 95 " +\
        "78 17 53 28 22 75 31 67 15 94 03 80 04 62 16 14 09 53 56 92 " +\
        "16 39 05 42 96 35 31 47 55 58 88 24 00 17 54 24 36 29 85 57 " +\
        "86 56 00 48 35 71 89 07 05 44 44 37 44 60 21 58 51 54 17 58 " +\
        "19 80 81 68 05 94 47 69 28 73 92 13 86 52 17 77 04 89 55 40 " +\
        "04 52 08 83 97 35 99 16 07 97 57 32 16 26 26 79 33 27 98 66 " +\
        "88 36 68 87 57 62 20 72 03 46 33 67 46 55 12 32 63 93 53 69 " +\
        "04 42 16 73 38 25 39 11 24 94 72 18 08 46 29 32 40 62 76 36 " +\
        "20 69 36 41 72 30 23 88 34 62 99 69 82 67 59 85 74 04 36 16 " +\
        "20 73 35 29 78 31 90 01 74 31 49 71 48 86 81 16 23 57 05 54 " +\
        "01 70 54 71 83 51 54 69 16 92 33 48 61 43 52 01 89 19 67 48 "
array = grid.split()
def index_to_coor(index):
    y = 19-(index//20)
    x = index%20
    return (x,y)
def coor_to_index(x, y):
    return 20*(19-y)+x
pmax = 0
for i in range(len(array)):
    x, y = index_to_coor(i)
    if x>=3:
        left = int(array[coor_to_index(x-1, y)])*int(array[coor_to_index(x-2, y)])*int(array[coor_to_index(x-3,y)])*int(array[i])
        if left > pmax: pmax = left 
    if x<=16:
        right = int(array[coor_to_index(x+1, y)])*int(array[coor_to_index(x+2, y)])*int(array[coor_to_index(x+3,y)])*int(array[i])
        if right > pmax: pmax = right 
    if y>=3:
        down = int(array[coor_to_index(x, y-1)])*int(array[coor_to_index(x, y-2)])*int(array[coor_to_index(x,y-3)])*int(array[i])
        if down > pmax: pmax = down 
    if y<=16:
        up = int(array[coor_to_index(x, y+1)])*int(array[coor_to_index(x, y+2)])*int(array[coor_to_index(x,y+3)])*int(array[i])
        if up > pmax: pmax = up  
    if x>= 3 and y<=16:
        upleft = int(array[coor_to_index(x-1, y+1)])*int(array[coor_to_index(x-2, y+2)])*int(array[coor_to_index(x-3,y+3)])*int(array[i])
        if upleft > pmax: pmax = upleft
    if x>= 3 and y>=3:
        downleft = int(array[coor_to_index(x-1, y-1)])*int(array[coor_to_index(x-2, y-2)])*int(array[coor_to_index(x-3,y-3)])*int(array[i])
        if downleft > pmax: pmax = downleft
    if x<= 16 and y<=16:
        upright = int(array[coor_to_index(x+1, y+1)])*int(array[coor_to_index(x+2, y+2)])*int(array[coor_to_index(x+3,y+3)])*int(array[i])
        if upright > pmax: pmax = upright
    if x<= 16 and y>=3:
        downright = int(array[coor_to_index(x+1, y-1)])*int(array[coor_to_index(x+2, y-2)])*int(array[coor_to_index(x+3,y-3)])*int(array[i])
        if downright > pmax: pmax = downright
print("problem 11: %s" % (pmax))

# =============================================================================
# problem 12
# =============================================================================
n = 28
ntri = 0
while True:
    divnum = 0
    n+=1
    ntri = sum([i for i in range(1, n + 1)])
    factor = 1
    while factor <= (ntri)**0.5:
        if ntri % factor == 0:
            divnum+=1
        factor+=1
    divnum *= 2
    if divnum > 500:
        break   
print("problem 12: %s" % (ntri))

# =============================================================================
# problem 14
# =============================================================================
lengthmax = 10
nmax = 13
for n in range(1000000, 14, -1):
    count = 0
    tempn = n
    while tempn > 1:
        count += 1
        if tempn % 2 == 0:
            tempn = tempn/2
        else:
            tempn = 3*tempn +1
    if count > lengthmax:
        lengthmax = count
        nmax = n
print("problem 14: %s" % (nmax))

# =============================================================================
# problem 17
# =============================================================================
numbers = {1: "one",
            2: "two",
            3: "three",
            4: "four",
            5: "five",
            6: "six",
            7: "seven",
            8: "eight",
            9: "nine",
            10: "ten",
            11: "eleven",
            12: "twelve",
            13: "thirteen",
            14: "fourteen",
            15: "fifteen",
            16: "sixteen",
            17: "seventeen",
            18: "eighteen",
            19: "nineteen",
            20: "twenty",
            30: "thirty",
            40: "forty",
            50: "fifty",
            60: "sixty",
            70: "seventy",
            80: "eighty",
            90: "ninety"}
for n in range(21, 100):
    if n%10 != 0:
        ten = int(n/10)*10
        one = n - ten
        numbers[n] = numbers[ten]+numbers[one]
for n in range(100, 1000):
    hundred = int(n/100)
    if n % 100 == 0:
        numbers[n] = numbers[hundred]+"hundred"
    else:
        ten = n - hundred*100
        numbers[n] = numbers[hundred]+"hundredand"+numbers[ten]
numbers[1000] = "onethousand"
totalsum = 0
for n in numbers:
    totalsum += len(numbers[n])
print("problem 17: %s" % (totalsum))

# =============================================================================
# problem 18
# =============================================================================
pyramid = {0: "75",
            1: "95 64",
            2: "17 47 82",
            3: "18 35 87 10",
            4: "20 04 82 47 65",
            5: "19 01 23 75 03 34",
            6: "88 02 77 73 07 63 67",
            7: "99 65 04 28 06 16 70 92",
            8: "41 41 26 56 83 40 80 70 33",
            9: "41 48 72 33 47 32 37 16 94 29",
            10: "53 71 44 65 25 43 91 52 97 51 14",
            11: "70 11 33 28 77 73 17 78 39 68 17 57",
            12: "91 71 52 38 17 14 91 43 58 50 27 29 48",
            13: "63 66 04 68 89 53 67 30 73 16 69 87 40 31",
            14: "04 62 98 27 23 09 70 98 73 93 38 53 60 04 23"}
for d in pyramid:
    temp = pyramid[d]
    pyramid[d] = temp.split()
def pyramidsum(i, depth):
    if depth > 14:
        return 0
    left = pyramidsum(i, depth+1)
    right = pyramidsum(i+1, depth+1)
    if left > right:
        return left + int(pyramid[depth][i])
    else:
        return right + int(pyramid[depth][i])
print("problem 18: %s" % (pyramidsum(0, 0)))

# =============================================================================
# problem 21
# =============================================================================
def divisors_sum(n):
    l = set()
    for i in range(1, int(n**0.5)+1):
        if n%i == 0:
            l.add(i)
            if int(n/i) < n:
                l.add(int(n/i))
    return sum(l)
sums = set()
amicable = 0
for n in range(2, 10000):
    asum = divisors_sum(n)
    bsum = divisors_sum(asum)
    if n == bsum and asum != bsum:
        amicable += n
print("problem 21: %s" % (amicable))
        
        