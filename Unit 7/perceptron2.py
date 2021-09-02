# -*- coding: utf-8 -*-

import ast
import sys

NUM_OF_EPOCHS = 100

def addZerosFront(length, bn):
    while length > len(bn):
        bn = "0" + bn
    return bn

def truth_table(bits, n):
    bn = bin(n)[2:]
    size = 2**bits
    bn = addZerosFront(size, bn)
    table = dict()
    for r in range(0, size):
        num = addZerosFront(bits, bin(size-1-r)[2:])
        inputs = tuple([i for i in num])
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

def multiply(s, tup):
    return tuple(i*s for i in tup)

def add(tup1, tup2):
    return tuple(map(sum, zip(tup1, tup2)))

def perceptron(A, w, b, x):
    t = dot_product(w, x) + b
    return A(t)

# def check(n, w, b):
#     correct = 0
#     table = truth_table(len(w), n)
#     for i in table:
#         p_val = perceptron(step, w, b, i)
#         if int(p_val) == int(table[i]):
#             correct += 1
#     return correct/(2**len(w))

def check(table, w, b):
    correct = 0
    for i in table:
        p_val = perceptron(step, w, b, i)
        if int(p_val) == int(table[i]):
            correct += 1
    return correct/(2**len(w))
    

def train_p(table, bits):
    w = tuple(0 for i in range(bits))
    b = 0
    last = ((float('inf'), float('inf')), float('inf'))
    for epoch in range(NUM_OF_EPOCHS):
        for r in table:
            p = perceptron(step, w, b, r)
            tr = tuple([int(i) for i in r])
            w = add(w, multiply((int(table[r]) - p), tr))
            b = b + (int(table[r]) - p)
        if last[0] == w and last[1] == b:
            break;
        last = (w, b)
    return w, b
        
def generate(bits):
    all_tables = []
    for i in range(0, 2**(2**bits)):
        table = truth_table(bits, i)
        all_tables.append(table)
    accurate = 0
    for t in all_tables:
        w, b = train_p(t, bits)
        accuracy = check(t, w, b)
        if accuracy == float(1):
            accurate += 1
    return len(all_tables), accurate

# =============================================================================
# RUN CODE PT 1
# =============================================================================
# print(generate(2))   

# =============================================================================
# RUN CODE PT 2   
# =============================================================================
run_bits = int(sys.argv[1])
run_n = int(sys.argv[2])
run_table = truth_table(run_bits, run_n)
run_w, run_b = train_p(run_table, run_bits)
run_acc = check(run_table, run_w, run_b)
print("weight: " + str(run_w))
print("bias: " + str(run_b))
print("accuracy: " + str(run_acc))