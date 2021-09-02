# -*- coding: utf-8 -*-

import ast
import sys

def decimalToBinary(n):
    if n == 0:
        return ""
    if n >= 1:
        return decimalToBinary(n // 2) + str(n%2)

def addZerosFront(length, bn):
    while length > len(bn):
        bn = "0" + bn
    return bn

def truth_table(bits, n):
    bn = decimalToBinary(n)
    # print(bn)
    size = 2**bits
    bn = addZerosFront(size, bn)
    table = dict()
    for r in range(0, size):
        num = addZerosFront(bits, decimalToBinary(size-1-r))
        inputs = tuple([i for i in num])
        # print(inputs)
        # print(bn[r:r+1])
        table[inputs] = int(bn[r:r+1])
    return table

def pretty_print_tt(table):
    for inp in table:
        print("".join(inp) + "\t" + str(table[inp]))
        
def step(num):
    num = float(num)
    if num > 0:
        return 1
    return 0

def dot_product(x, y):
    dot_p = 0
    for i in range(0, len(x)):
        dot_p += int(x[i])*int(y[i])
    return dot_p

def perceptron(A, w, b, x):
    t = dot_product(w, x) + b
    return A(t)

def check(n, w, b):
    correct = 0
    table = truth_table(len(w), n)
    # print(table)
    for i in table:
        p_val = perceptron(step, w, b, i)
        # print(p_val)
        if int(p_val) == int(table[i]):
            correct += 1
    return correct/(2**len(w))

# =============================================================================
# RUN CODE
# =============================================================================
run_n = int(sys.argv[1])
run_w = ast.literal_eval(sys.argv[2])
run_b = float(sys.argv[3])
print(check(run_n, run_w, run_b))
    
