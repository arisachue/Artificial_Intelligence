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
    size = 2**bits
    bn = addZerosFront(size, bn)
    table = dict()
    for r in range(0, size):
        num = addZerosFront(bits, decimalToBinary(size-1-r))
        inputs = tuple([i for i in num])
        table[inputs] = int(bn[r:r+1])
    return table

def pretty_print_tt(table):
    string = ""
    for inp in table:
        string += " ".join(str(i) for i in inp) + "\t" + str(table[inp]) + "\n"
    return string
        
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
    for i in table:
        p_val = perceptron(step, w, b, i)
        if int(p_val) == int(table[i]):
            correct += 1
    return correct/(2**len(w))

# =============================================================================
# XOR HAPPENS HERE
# =============================================================================
def XOR():
    table = {(1, 1): "0", (1, 0): "0", (0, 1): "0", (0, 0): "0"}
    
    for r in table:
        p3 = perceptron(step, (1, 1), 0, r)
        p4 = perceptron(step, (-1, -2), 3, r)
        p5 = perceptron(step, (1, 2), -2, (p3, p4))
        table[r] = p5
    
    return table

# =============================================================================
# RUN CODE
# =============================================================================
XOR_table = XOR()
run_i = ast.literal_eval(sys.argv[1])     
print(XOR_table[run_i])
    

    
