# -*- coding: utf-8 -*-

import sys

g_board = []
g_visited_connected = set()

size = sys.argv[1]
g_row = int(size[:size.index("x")])
g_col = int(size[size.index("x")+1:])

def index_to_coor(index):
    y = (index//g_col)
    x = index%g_col
    return (x,y)

def coor_to_index(x, y):
    return (g_col*(y))+x

def print_board(brd):
    for c in range(0, g_row*g_col, g_col):
        print(brd[c:c+g_col])

g_block_num = int(sys.argv[2]) # GLOBAL VAR num of blocks
if g_block_num == g_row*g_col:
    for i in range(g_row*g_col):            # fill board completely
        g_board.append("#")
else:
    for i in range(g_row*g_col):            # create empty board
        g_board.append("-")
    if g_block_num %2 != 0:
        g_board[coor_to_index(int(g_col/2), int(g_row/2))] = "#"
    

file = sys.argv[3]              # text file for word list

def find_last_num(string):
    temp = string[::-1]
    pos = 0
    for i in range(len(temp)):
        if temp[i].isdigit(): 
            pos = i
            break
    return len(temp) - pos -1

def rotate(x, y):
    newx = g_col-x-1
    newy = g_row-y-1
    # return (newx, newy)   
    return coor_to_index(newx, newy)

def not_in_range(x, y):
    if x > -1 and x < g_col and y > -1 and y < g_row:
        return False
    return True

def in_range(x, y):
    if x > -1 and x < g_col and y > -1 and y < g_row:
        return True
    return False

def three_block_valid(board, i):
    x, y = index_to_coor(i)
    if in_range(x-1, y) and board[coor_to_index(x-1, y)] != "#":
        if not_in_range(x-2, y) or not_in_range(x-3, y) or board[coor_to_index(x-2, y)] == "#" or board[coor_to_index(x-3, y)] == "#":
            return False
    if in_range(x+1, y) and board[coor_to_index(x+1, y)] != "#":
        if not_in_range(x+2, y) or not_in_range(x+3, y) or board[coor_to_index(x+2, y)] == "#" or board[coor_to_index(x+3, y)] == "#":
            return False
    if in_range(x, y-1) and board[coor_to_index(x, y-1)] != "#":
        if not_in_range(x, y-2) or not_in_range(x, y-3) or board[coor_to_index(x, y-2)] == "#" or board[coor_to_index(x, y-3)] == "#":
            return False
    if in_range(x, y+1) and board[coor_to_index(x, y+1)] != "#":
        if not_in_range(x, y+2) or not_in_range(x, y+3) or board[coor_to_index(x, y+2)] == "#" or board[coor_to_index(x, y+3)] == "#":
            return False
    return True

def fill_three_blocks(board, i):
    x, y = index_to_coor(i)
    if in_range(x-1, y) and board[coor_to_index(x-1, y)] != "#":
        if not_in_range(x-2, y) or not_in_range(x-3, y) or board[coor_to_index(x-2, y)] == "#" or board[coor_to_index(x-3, y)] == "#":
            for n in range(1, 4):
                if in_range(x-n, y) and board[coor_to_index(x-n, y)] == "-":
                    board[coor_to_index(x-n, y)] = "#"
    if in_range(x+1, y) and board[coor_to_index(x+1, y)] != "#":
        if not_in_range(x+2, y) or not_in_range(x+3, y) or board[coor_to_index(x+2, y)] == "#" or board[coor_to_index(x+3, y)] == "#":
            for n in range(1, 4):
                if in_range(x+n, y) and board[coor_to_index(x+n, y)] == "-":
                    board[coor_to_index(x+n, y)] = "#"
    if in_range(x, y-1) and board[coor_to_index(x, y-1)] != "#":
        if not_in_range(x, y-2) or not_in_range(x, y-3) or board[coor_to_index(x, y-2)] == "#" or board[coor_to_index(x, y-3)] == "#":
            for n in range(1, 4):
                if in_range(x, y-n) and board[coor_to_index(x, y-n)] == "-":
                    board[coor_to_index(x, y-n)] = "#"
    if in_range(x, y+1) and board[coor_to_index(x, y+1)] != "#":
        if not_in_range(x, y+2) or not_in_range(x, y+3) or board[coor_to_index(x, y+2)] == "#" or board[coor_to_index(x, y+3)] == "#":
            for n in range(1, 4):
                if in_range(x, y+n) and board[coor_to_index(x, y+n)] == "-":
                    board[coor_to_index(x, y+n)] = "#"

def connected(board, x, y, visited):
    # x, y = index_to_coor(i)
    if not_in_range(x, y):
        return 0
    i = coor_to_index(x, y)
    # if board[i] != "-" or i in visited:
    #     return 0
    if board[i] == "#" or i in visited:
        return 0
    visited.add(i)
    return 1 + connected(board, x-1, y, visited) + connected(board, x+1, y, visited) + connected(board, x, y-1, visited) + connected(board, x, y+1, visited)
    # return 1 + connected(board, coor_to_index(x-1, y), visited) + connected(board, coor_to_index(x+1, y), visited) + connected(board, coor_to_index(x, y-1), visited) + connected(board, coor_to_index(x, y+1), visited)
    

def valid_connected_board(board):
    if board.count("-") == 0:
        return True
    i = board.index("-")
    x, y = index_to_coor(i)
    v = set()
    blanks = connected(board, x, y, v)
    # blanks = connected(board, x, y)
    # print(blanks)
    # if blanks == (board.count("-")):
    #     return True
    if blanks == (g_row*g_col) - board.count("#"):
        return True
    return False

def start_connected(board, x, y):
    global g_visited_connected
    if not_in_range(x, y):
        return 0
    i = coor_to_index(x, y)
    if board[i] == "#" or i in g_visited_connected:
        return 0
    g_visited_connected.add(i)
    return 1 + start_connected(board, x-1, y) + start_connected(board, x+1, y) + start_connected(board, x, y-1) + start_connected(board, x, y+1)

g_seedstring = sys.argv[4:]        # fills in board with starting seedstring
for s in g_seedstring:
    pos = find_last_num(s)
    ycoor = int(s[1:s.index("x")])
    xcoor = int(s[s.index("x")+1:pos+1])
    if s[0].upper() == "H":
        s = s[pos+1:]
        for i in range(len(s)):
                g_board[coor_to_index(xcoor+i, ycoor)] = s[i]
        # if s == "#":
        #     g_board[coor_to_index(xcoor, ycoor)] = s
        #     if three_block_valid(g_board, coor_to_index(xcoor, ycoor)) == False:
        #         fill_three_blocks(g_board, coor_to_index(xcoor, ycoor))
        #     g_board[rotate(xcoor, ycoor)] = s
        #     if three_block_valid(g_board, rotate(xcoor, ycoor)) == False:
        #         fill_three_blocks(g_board, rotate(xcoor, ycoor))
        # else:
        #     for i in range(len(s)):
        #         g_board[coor_to_index(xcoor+i, ycoor)] = s[i]
    else:
        s = s[pos+1:]
        for i in range(len(s)):
                g_board[coor_to_index(xcoor, ycoor+i)] = s[i]
        # if s == "#":
        #     g_board[coor_to_index(xcoor, ycoor)] = s
        #     if three_block_valid(g_board, coor_to_index(xcoor, ycoor)) == False:
        #         fill_three_blocks(g_board, coor_to_index(xcoor, ycoor))
        #     g_board[rotate(xcoor, ycoor)] = s
        #     if three_block_valid(g_board, rotate(xcoor, ycoor)) == False:
        #         fill_three_blocks(g_board, rotate(xcoor, ycoor))
        # else:
        #     for i in range(len(s)):
        #         g_board[coor_to_index(xcoor, ycoor+i)] = s[i]

# print_board(g_board)
# print()

if g_board.count("#") > 1:
    temp = [ s for s in g_board]
    for i in range(len(temp)):
        if temp[i] == "#":
            # input()
            x, y = index_to_coor(i)
            # print("ogx: %s ogy: %s" % (x, y))
            if three_block_valid(g_board, i) == False:
                fill_three_blocks(g_board, i)
            g_board[rotate(x, y)] = "#"
            # print("x: %s y: %s" % index_to_coor(rotate(x, y)))
            if three_block_valid(g_board, rotate(x, y)) == False:
                fill_three_blocks(g_board, rotate(x, y))
            # print_board(g_board)

# print_board(g_board)
# print()
# print(g_board)

if valid_connected_board(g_board) == False:
    blanks = connected(g_board, 0, 0, set())
    if blanks < g_block_num:
        blanks = start_connected(g_board, 0, 0)
        print("left up")
        for i in g_visited_connected:
            g_board[i] = "#"
            x, y = index_to_coor(i)
            g_board[rotate(x, y)] = "#"
        g_visited_connected = set()
    elif connected(g_board, g_col-1, 0, set()) < g_block_num:
        blanks = start_connected(g_board, g_col-1, 0)
        print("right up")
        print(g_visited_connected)
        for i in g_visited_connected:
            g_board[i] = "#"
            x, y = index_to_coor(i)
            g_board[rotate(x, y)] = "#"
        g_visited_connected = set()
    elif connected(g_board, 0, g_row-1, set()) < g_block_num:
        start_connected(g_board, 0, g_row-1)
        print("left down")
        for i in g_visited_connected:
            g_board[i] = "#"
            x, y = index_to_coor(i)
            g_board[rotate(x, y)] = "#"
        g_visited_connected = set()
    elif connected(g_board, g_col-1, g_row-1, set()) < g_block_num:
        start_connected(g_board, g_col-1, g_row-1)
        print("right down")
        for i in g_visited_connected:
            g_board[i] = "#"
            x, y = index_to_coor(i)
            g_board[rotate(x, y)] = "#"
        g_visited_connected = set()
    

# g_block_num -= g_board.count("#")
# print(g_block_num)

def goal_test(board):
    if board.count("#") == g_block_num:
        return True
    return False

# def connected(board, i):
#     x, y = index_to_coor(i)
#     if not_in_range(x, y):
#         return 0
#     if board[i] != "-" or board[i] == "*":
#         return 0
#     board[i] = "*"
#     return 1 + connected(board, coor_to_index(x-1, y)) + connected(board, coor_to_index(x+1, y)) + connected(board, coor_to_index(x, y-1)) + connected(board, coor_to_index(x, y+1))
    
    

def get_next_unassigned_var(board):
    for i in range(len(board)):
        if board[i] == "-":
            return i
        
def add_block_valid(board, i):
    temp = [ s for s in board]
    x, y = index_to_coor(i)
    if temp[i] != "-" or temp[rotate(x, y)] != "-":
        return False
    temp[i] = "#"
    temp[rotate(x, y)] = "#"
    if three_block_valid(temp, i) == False:
        return False
    if three_block_valid(temp, rotate(x, y)) == False:
        return False
    return valid_connected_board(temp)
    
        
def csp_backtracking(board):
    input()
    if goal_test(board): 
        return board
    for i in range(len(board)):
        if board[i] == "-":
            new_board = [ s for s in board]
            if add_block_valid(new_board, i):
                x, y = index_to_coor(i)
                print("index: %s" % (i))
                print(index_to_coor(i))
                new_board[i] = "#"
                new_board[rotate(x, y)] = "#"
                print_board(new_board)
                # print(new_board.count("#"))
                print()
                # print(new_board)
                # print()
                result = csp_backtracking(new_board)
                if result is not None:
                    return result
    return None

print_board(g_board)
print()
print(g_board.count("#"))
print_board(csp_backtracking(g_board))
# print("".join(csp_backtracking(g_board)))
        