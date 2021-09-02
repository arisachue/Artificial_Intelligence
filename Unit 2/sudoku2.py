# -*- coding: utf-8 -*-

import sys
import time
# from texttable import Texttable

# puzzles = []
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

# def print_dict(dboard):
#     # count=1
#     # temp=""
#     # for i in dboard:
#     #     temp+=dboard[i]+"\t"
#     #     if i%subblock_width == 0:
#     #         temp+="\t"
#     #     if i != 0 and (n**2)%i == 0:
#     #         temp+="\n"
#     #         count+=1
#     #     if count%subblock_height == 0:
#     #         temp+="\n"
#     # print(temp)
#     count=1
#     t = []
#     for col in range(0, n**2, n):
#         l = []
#         for row in range(0, n):
#             index = col+row
#             if (index)%subblock_width == 0 and row !=0:
#                 l.append(" ")
#             l.append(dboard[index])
#         t.append(l)
#         l = []
#         if count%subblock_height == 0:
#             for row in range(0, n+2):
#                 l.append(" ")
#         if len(l) > 0:
#             t.append(l)
#         count+=1
#     # print(t)
#     table = Texttable()
#     temp=[]
#     for row in range(0, n+2):
#         temp.append("t")
#     table.set_cols_dtype(temp) 
#     temp=[]
#     for row in range(0, n+2):
#         temp.append(len(symbol_set))
#     table.set_cols_width(temp)
#     table.add_rows(t)
#     print(table.draw())
            

def constraints():
    global n, subblock_height, subblock_width, gl_constraints 
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
    # global symbol_set
    # puzzle = ""
    # for i in dboard:
    #     puzzle += dboard[i]
    # for s in symbol_set:
    #     if puzzle.count(s) != n: 
    #         return False
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
                # new = [r for r in dboard[c] if r!=val]
                # new = "".join(new)
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
                # new = [r for r in dboard[c] if r!=val]
                # new = "".join(new)
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
    # solved = []
    # for c in gl_constraints:
    #     temp = ""
    #     for i in c:
    #         temp += dboard[i]
    #     singles = set()
    #     for s in symbol_set:
    #         num = temp.count(s)
    #         if num == 1:
    #             singles.add(s)
    #         if num == 0:
    #             print("zero")
    #             return None, None
    #     for i in c:
    #         if len(dboard[i]) > 1:
    #             for s in dboard[i]:
    #                 if s in singles:
    #                     solved.append(i)
    #                     dboard[i] = s
    # return dboard, solved
    solved = []
    # print("here")
    for gc in gl_constraints:
        # print(toString(dboard))
        # print("constraint set: %s" % (str(gc)))
        for s in symbol_set:
            # input()
            # print(s)
            index = None
            single = True
            for i in gc:
                if index is None and s in dboard[i]:
                    index = i
                elif index is not None and s in dboard[i]:
                    single = False
                    break;
            # print(index)
            # print(single)
            if index is None:
                return None, None
            if single:
                # print("here")
                if len(dboard[index]) > 1:
                    dboard[index] = s
                    solved.append(index)
                    # print("constraint set: %s, changed to %s at %s" % (gc, s, index))
                    # print("solved list: %s" (solved))
                    # print_dict(dboard)
                    # input()
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
    # count=0
    # start = time.perf_counter()
    for line in f:
        line = line.strip()
        stats(line)
        print("n: %s, h: %s, w: %s" % (n, subblock_height, subblock_width))
        print(symbol_set)
        print(gl_constraints)
        print(dpuzzle)
        print(con_dict)
        puzzle = forward_prog(dpuzzle)
        puzzle = csp_backtracking_const_prog(puzzle)
        print(toString(puzzle))
        # print(count)
        # count+=1
# end = time.perf_counter()
# print("time: %s" % (end-start))
        
# puzzle = "..3..1....4..2.."
# puzzle = "..275..B...14.3...79..2...5..2..7..8.6...5.1.7B..3.....41........C....698B....9........98.....A..1C.A.2...9.C..1..A..4...A..49...5.37...B..5A1.."
# puzzle = ".17369825632158947958724316825437169791586432346912758289643571573291684164875293"
# puzzle = "..3.2.6..9..3.5..1..18.64....81.29..7.......8..67.82....26.95..8..2.3..9..5.1.3.."
# puzzle = "..5.....8.EC3.27.8......A.5...1..C3..B1..D79E6.8E7.4.....213.G5D6..7C.539...D.F14....6...8.E7B3C..D...9..1.7A.....8....42..F.9....F.2..7E....3.....14.F..C...E..5DBE3.G...6....A8G.C...A15.4F..22A4.F18.....6.G3F.C3E46..A2..58..6...2.5......A.75.GB3.C.....1.."
# stats(puzzle)
# print("n: %s, h: %s, w: %s" % (n, subblock_height, subblock_width))
# print(symbol_set)
# print(gl_constraints)
# # print_puzzle(puzzle)
# print_dict(dpuzzle)
# puzzle = forward_looking(dpuzzle)
# print_dict(dpuzzle)
# puzzle, solve = const_prog(dpuzzle)
# print(puzzle)
# print(puzzle)
# print_dict(dpuzzle)
# # print(toString(puzzle))
# puzzle = forward_prog(dpuzzle)
# puzzle = csp_backtracking_const_prog(puzzle)
# print(toString(puzzle))

# print(len(symbol_set))
# print_puzzle(puzzle)
# dpuzzle = build_puzzle(puzzle)
# dpuzzle = forward_looking(dpuzzle)
# p = csp_backtracking(dpuzzle)
# print(toString(p))
# puzzle = csp_backtracking(puzzle)
# print(puzzle)
# print_puzzle(puzzle)
# con = build_constraint_dict()
# print("constraints")
# for c in con:
#     print(con[c])
