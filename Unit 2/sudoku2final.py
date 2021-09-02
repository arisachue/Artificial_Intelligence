# -*- coding: utf-8 -*-

import sys

puzzles = []
n = 0
subblock_height = 0
subblock_width = 0
symbol_set = set()
con_dict = dict()
dpuzzle = dict()
gl_constraints = []

symbols = "123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        
def stats(puzzle):
    global n, subblock_height, subblock_width, symbol_set, symbols, con_dict, dpuzzle, gl_constraints
    n = 0
    subblock_height = 0
    subblock_width = 0
    symbol_set = set()
    con_dict = dict()
    dpuzzle = dict()
    gl_constraints = []
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
    build_puzzle(puzzle)
    
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
    global n, subblock_height, subblock_width, gl_constraints 
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
    gl_constraints = con
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
    

def check(dboard):
    for i in dboard:
        if len(dboard[i]) > 1:
            return False
    return True

def get_next_unassigned_var(dboard):
    min_index = 0
    min_len = n
    for i in dboard:
        cur_len = len(dboard[i])
        if cur_len > 1 and cur_len < min_len:
            min_index = i
            min_len = cur_len
    return min_index

def get_sorted_values(state, var):
    cant = set()
    values = []
    for i in con_dict[var]:
        constraints = state[i]
        if len(constraints) == 1:
            cant.add(constraints)
    for s in symbol_set:
        if s not in cant:
            values.append(s)
    return values

def build_puzzle(puzzle):
    global dpuzzle
    for s in range(n**2):
        if puzzle[s] == ".":
            dpuzzle[s] = symbols[:n]
        else:
            dpuzzle[s] = puzzle[s]
    return dpuzzle

def forward_looking(dboard):
    solved = []
    for s in dboard:
        if len(dboard[s]) == 1:
            solved.append(s)
    while len(solved) > 0:
        index = solved.pop()
        constraints = con_dict[index]
        val = dboard[index]
        for c in constraints:
            if val in dboard[c]:
                string = dboard[c]
                i = string.index(val)
                new = string[:i]+string[i+1:]
                dboard[c] = new
                if len(new) == 1:
                    solved.append(c)
                if len(new) == 0:
                    return None
    return dboard

def forward_looking_prog(dboard, solved):
    while len(solved) > 0:
        index = solved.pop()
        constraints = con_dict[index]
        val = dboard[index]
        for c in constraints:
            if val in dboard[c]:
                string = dboard[c]
                i = string.index(val)
                new = string[:i]+string[i+1:]
                dboard[c] = new
                if len(new) == 1:
                    solved.append(c)
                if len(new) == 0:
                    return None
    return dboard

def assign(board, var, val):
    new_board = dict()
    for i in range(n**2):
        if i == var:
            new_board[i] = val
        else:
            new_board[i] = board[i]
    return new_board

def toString(dboard):
    puzzle = ""
    for i in dboard:
        puzzle += dboard[i]
    return puzzle

def const_prog(dboard):
    solved = []
    for gc in gl_constraints:
        for s in symbol_set:
            index = None
            single = True
            for i in gc:
                if index is None and s in dboard[i]:
                    index = i
                elif index is not None and s in dboard[i]:
                    single = False
                    break;
            if index is None:
                return None, None
            if single:
                if len(dboard[index]) > 1:
                    dboard[index] = s
                    solved.append(index)
    return dboard, solved
            

def forward_prog(dboard):
    dboard = forward_looking(dboard)
    if dboard is None:
        return None
    dboard, solved = const_prog(dboard)
    if solved is None:
        return None
    while len(solved) > 0:
        dboard = forward_looking_prog(dboard, solved)
        if dboard is None:
            return None
        dboard, solved = const_prog(dboard)
        if solved is None:
            return None
    return dboard
        
        
def csp_backtracking_forward_looking(state):
    if check(state): 
        return state
    var = get_next_unassigned_var(state)
    for val in get_sorted_values(state, var):
        new_board = assign(state, var, val)
        checked_board = forward_looking(new_board)
        if checked_board is not None:
            result = csp_backtracking_forward_looking(checked_board)
            if result is not None:
                return result
    return None

def csp_backtracking_const_prog(state):
    if check(state): 
        return state
    var = get_next_unassigned_var(state)
    for val in get_sorted_values(state, var):
        new_board = assign(state, var, val)
        checked_board = forward_prog(new_board)
        if checked_board is not None:
            result = csp_backtracking_const_prog(checked_board)
            if result is not None:
                return result
    return None

# =============================================================================
# SUDOKU PT2 FORWARD LOOKING        
# =============================================================================
# s = sys.argv[1]  

# with open(s) as f:
#     # count=0
#     for line in f:
#         line = line.strip()
#         stats(line)
#         puzzle = forward_looking(dpuzzle)
#         puzzle = csp_backtracking_forward_looking(puzzle)
#         print(toString(puzzle))
#         # print(count)
#         # count+=1

# =============================================================================
# SUDOKU PT2 CONSTRAINT PROPAGATION
# =============================================================================
s = sys.argv[1]  

with open(s) as f:
    for line in f:
        line = line.strip()
        stats(line)
        puzzle = forward_prog(dpuzzle)
        puzzle = csp_backtracking_const_prog(puzzle)
        print(toString(puzzle))