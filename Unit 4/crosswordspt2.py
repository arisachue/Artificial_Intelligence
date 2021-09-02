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
    

def valid_connected_board(board):
    if board.count("-") == 0:
        return True
    i = board.index("-")
    x, y = index_to_coor(i)
    v = set()
    blanks = connected(board, x, y, v)
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
    else:
        s = s[pos+1:]
        for i in range(len(s)):
                g_board[coor_to_index(xcoor, ycoor+i)] = s[i]

if g_board.count("#") > 1:
    temp = [ s for s in g_board]
    for i in range(len(temp)):
        if temp[i] == "#":
            x, y = index_to_coor(i)
            if three_block_valid(g_board, i) == False:
                fill_three_blocks(g_board, i)
            g_board[rotate(x, y)] = "#"
            if three_block_valid(g_board, rotate(x, y)) == False:
                fill_three_blocks(g_board, rotate(x, y))

if valid_connected_board(g_board) == False:
    blanks = connected(g_board, 0, 0, set())
    if blanks < g_block_num:
        blanks = start_connected(g_board, 0, 0)
        for i in g_visited_connected:
            g_board[i] = "#"
            x, y = index_to_coor(i)
            g_board[rotate(x, y)] = "#"
        g_visited_connected = set()
    elif connected(g_board, g_col-1, 0, set()) < g_block_num:
        blanks = start_connected(g_board, g_col-1, 0)
        print(g_visited_connected)
        for i in g_visited_connected:
            g_board[i] = "#"
            x, y = index_to_coor(i)
            g_board[rotate(x, y)] = "#"
        g_visited_connected = set()
    elif connected(g_board, 0, g_row-1, set()) < g_block_num:
        start_connected(g_board, 0, g_row-1)
        for i in g_visited_connected:
            g_board[i] = "#"
            x, y = index_to_coor(i)
            g_board[rotate(x, y)] = "#"
        g_visited_connected = set()
    elif connected(g_board, g_col-1, g_row-1, set()) < g_block_num:
        start_connected(g_board, g_col-1, g_row-1)
        for i in g_visited_connected:
            g_board[i] = "#"
            x, y = index_to_coor(i)
            g_board[rotate(x, y)] = "#"
        g_visited_connected = set()
        
