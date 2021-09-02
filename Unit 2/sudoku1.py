# -*- coding: utf-8 -*-

import sys

puzzles = []
n = 0
subblock_height = 0
subblock_width = 0
symbol_set = set()
con_dict = dict()

symbols = "123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        
def stats(puzzle):
    global n, subblock_height, subblock_width, symbol_set, symbols
    n = int(len(puzzle) ** (1/2))
    sqrt = int(n**(1/2))
    if (sqrt**2 == n):
        subblock_height = sqrt
        subblock_width = sqrt
    else:
        while(sqrt > 1):
            if n%sqrt == 0:
                break
            sqrt = sqrt-1
        subblock_height = sqrt
        subblock_width = int(n/sqrt)
    symbol_set = set(symbols[:n])
    build_constraint_dict()
    
def print_puzzle(puzzle):
    global n, subblock_height, subblock_width 
    puzzle = "".join(puzzle)
    count=1
    for col in range(0,n**2,n):
        row = puzzle[col:col+n]
        temp = []
        for i in range(0, n, subblock_width):
            temp+= row[i:i+subblock_width] + " "
        print(" ".join(temp))
        if count%subblock_height == 0: print()
        count+=1

def constraints():
    global n, subblock_height, subblock_width 
    # row_con = set()
    # col_con = set()
    # block_con = set()
    con = []
    for r in range(0, n**2, n):
        row = set()
        for c in range(n):
            row.add(c+r)
        con.append(row)
    for c in range(n):
        col = set()
        for r in range(0, n**2, n):
            col.add(c+r)
        con.append(col)
    for wb in range(0, n, subblock_width):
        for hb in range(0, n, subblock_height):
            block = set()
            for w in range(subblock_width):
                for h in range(subblock_height):
                    block.add(wb+(hb*n)+w+(h*n))
            con.append(block)
    return con

def build_constraint_dict():
    global n, subblock_height, subblock_width, con_dict
    con = constraints()
    
    for s in range(n**2):
        con_dict[s] = set()
        for c in con:
            if s in c:
                con_dict[s].update(c)
                con_dict[s].remove(s)
    return con_dict
    

def check(puzzle):
    global symbol_set
    for s in symbol_set:
        if puzzle.count(s) != n: 
            return False
    return True

def get_next_unassigned_var(puzzle):
    for i in range(len(puzzle)):
        if puzzle[i] == ".": 
            return i

def get_sorted_values(state, var):
    cant = set()
    values = []
    for i in con_dict[var]:
        cant.add(state[i])
    for s in symbol_set:
        if s not in cant:
            values.append(s)
    return values


def csp_backtracking(state):
    if check(state): return state
    var = get_next_unassigned_var(state)
    for val in get_sorted_values(state, var):
        new_state = [ r for r in state]
        new_state[var] = val
        result = csp_backtracking(new_state)
        if result is not None:
            return result
    return None
        
# s = sys.argv[1]  

# with open(s) as f:
#     count=0
#     for line in f:
#         line = line.strip()
#         stats(line)
#         puzzle = csp_backtracking(line)
#         print("".join(puzzle))
#         # print(count)
#         # count+=1
        
# puzzle = "..275..B...14.3...79..2...5..2..7..8.6...5.1.7B..3.....41........C....698B....9........98.....A..1C.A.2...9.C..1..A..4...A..49...5.37...B..5A1.."
# puzzle = ".17369825632158947958724316825437169791586432346912758289643571573291684164875293"
puzzle = "..3.2.6..9..3.5..1..18.64....81.29..7.......8..67.82....26.95..8..2.3..9..5.1.3.."
stats(puzzle)
# print("n: %s, h: %s, w: %s" % (n, subblock_height, subblock_width))
# print(len(symbol_set))
# print_puzzle(puzzle)
puzzle = csp_backtracking(puzzle)
print("".join(puzzle))
# print_puzzle(puzzle)
# con = build_constraint_dict()
# print("constraints")
# for c in con:
#     print(con[c])
