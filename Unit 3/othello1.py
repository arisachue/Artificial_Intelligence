# -*- coding: utf-8 -*-

import sys

def index_to_coor(index):
    y = 7-(index//8)
    x = index%8
    return (x,y)

def coor_to_index(x, y):
    return 8*(7-y)+x

def print_board(board):
    for col in range(0, 64, 8):
        print(board[col:col+8])

# def validMove(board, token, index):
#     if board[index] != ".":
#         return False
#     opp = "x"
#     if token == "x":
#         opp = "o"
#     x, y = index_to_coor(index)
#     spaces = []
#     added = False
#     if x > 0 and board[coor_to_index(x-1, y)] == opp:
#         tempx = x
#         tempy = y
#         while tempx > 0 and board[coor_to_index(tempx-1, y)] == opp: # keep going left
#             tempx -= 1
#         new_index = coor_to_index(tempx, y)
#         if board[new_index] == token:
#             added = True
#             spaces.append(index)
 
def in_range(x, y):
    if x > -1 and x < 8 and y > -1 and y < 8:
        return True
    return False

def possibleMoves(board, token):
    spaces = []
    opp = "x"
    if token == "x":
        opp = "o"
    for i in range(len(board)):
        if board[i] != ".":
            continue
        x, y = index_to_coor(i)
        if x > 1 and board[coor_to_index(x-1, y)] == opp: # left
            tempx = x
            while tempx > 0 and board[coor_to_index(tempx-1, y)] == opp: # keep going left
                tempx -= 1
            new_index = coor_to_index(tempx-1, y)
            if in_range(tempx-1, y) and board[new_index] == token:
                spaces.append(i)
                continue
        if x < 6 and board[coor_to_index(x+1, y)] == opp: # right
            tempx = x
            while tempx < 7 and board[coor_to_index(tempx+1, y)] == opp: # keep going right
                tempx += 1
            new_index = coor_to_index(tempx+1, y)
            if in_range(tempx+1, y) and board[new_index] == token:
                spaces.append(i)
                continue
        if y > 1 and board[coor_to_index(x, y-1)] == opp: # down
            tempy = y
            while tempy > 0 and board[coor_to_index(x, tempy-1)] == opp: # keep going down
                tempy -= 1
            new_index = coor_to_index(x, tempy-1)
            if in_range(x, tempy-1) and board[new_index] == token:
                spaces.append(i)
                continue
        if y < 6 and board[coor_to_index(x, y+1)] == opp: # up
            tempy = y
            while tempy < 7 and board[coor_to_index(x, tempy+1)] == opp: # keep going up
                tempy += 1
            new_index = coor_to_index(x, tempy+1)
            if in_range(x, tempy+1) and board[new_index] == token:
                spaces.append(i)
                continue
        if x > 1 and y > 1 and board[coor_to_index(x-1, y-1)] == opp: # diagonal left down
            tempx = x    
            tempy = y
            while tempx > 0 and tempy > 0 and board[coor_to_index(tempx-1, tempy-1)] == opp: # keep going left+down
                tempx -= 1
                tempy -= 1
            new_index = coor_to_index(tempx-1, tempy-1)
            if in_range(tempx-1, tempy-1) and board[new_index] == token:
                spaces.append(i)
                continue
        if x > 1 and y < 6 and board[coor_to_index(x-1, y+1)] == opp: # diagonal left up
            tempx = x    
            tempy = y
            while tempx > 0 and tempy < 7 and board[coor_to_index(tempx-1, tempy+1)] == opp: # keep going left+up
                tempx -= 1
                tempy += 1
            new_index = coor_to_index(tempx-1, tempy+1)
            if in_range(tempx-1, tempy+1) and board[new_index] == token:
                spaces.append(i)
                continue
        if x < 6 and y > 1 and board[coor_to_index(x+1, y-1)] == opp: # diagonal right down
            tempx = x    
            tempy = y
            while tempx < 7 and tempy > 0 and board[coor_to_index(tempx+1, tempy-1)] == opp: # keep going right+down
                tempx += 1
                tempy -= 1
            new_index = coor_to_index(tempx+1, tempy-1)
            if in_range(tempx+1, tempy-1) and board[new_index] == token:
                spaces.append(i)
                continue
        if x < 6 and y < 6 and board[coor_to_index(x+1, y+1)] == opp: # diagonal right up
            tempx = x    
            tempy = y
            while tempx < 7 and tempy < 7 and board[coor_to_index(tempx+1, tempy+1)] == opp: # keep going right+up
                tempx += 1
                tempy += 1
            new_index = coor_to_index(tempx+1, tempy+1)
            if in_range(tempx+1, tempy+1) and board[new_index] == token:
                spaces.append(i)
                continue
    return spaces

def move(board, token, position):
    board = list(board)
    board[position] = token
    opp = "x"
    if token == "x":
        opp = "o"
    x, y = index_to_coor(position)
    if x > 1 and board[coor_to_index(x-1, y)] == opp:
        tempx = x
        while tempx > 0 and board[coor_to_index(tempx-1, y)] == opp: # keep going left
            tempx -= 1
        new_index = coor_to_index(tempx-1, y)
        if in_range(tempx-1, y) and board[new_index] == token:
            for i in range(new_index+1, position):
                board[i] = token
    if x < 6 and board[coor_to_index(x+1, y)] == opp: # right
        tempx = x
        while tempx < 7 and board[coor_to_index(tempx+1, y)] == opp: # keep going right
            tempx += 1
        new_index = coor_to_index(tempx+1, y)
        if in_range(tempx+1, y) and board[new_index] == token:
            for i in range(position+1, new_index):
                board[i] = token
    if y > 1 and board[coor_to_index(x, y-1)] == opp: # down
        tempy = y
        while tempy > 0 and board[coor_to_index(x, tempy-1)] == opp: # keep going down
            tempy -= 1
        new_index = coor_to_index(x, tempy-1)
        if in_range(x, tempy-1) and board[new_index] == token:
            for i in range(position, new_index, 8):
                board[i] = token
    if y < 6 and board[coor_to_index(x, y+1)] == opp: # up
        tempy = y
        while tempy < 7 and board[coor_to_index(x, tempy+1)] == opp: # keep going up
            tempy += 1
        new_index = coor_to_index(x, tempy+1)
        if in_range(x, tempy+1) and board[new_index] == token:
            for i in range(new_index, position, 8):
                board[i] = token
    if x > 1 and y > 1 and board[coor_to_index(x-1, y-1)] == opp: # diagonal left down
        tempx = x    
        tempy = y
        while tempx > 0 and tempy > 0 and board[coor_to_index(tempx-1, tempy-1)] == opp: # keep going left+down
            tempx -= 1
            tempy -= 1
        new_index = coor_to_index(tempx-1, tempy-1)
        if in_range(tempx-1, tempy-1) and board[new_index] == token:
            for i in range(0, abs(x-(tempx-1))):
                newx = (tempx-1) + i
                newy = (tempy-1) + i
                board[coor_to_index(newx, newy)] = token
    if x > 1 and y < 6 and board[coor_to_index(x-1, y+1)] == opp: # diagonal left up
        tempx = x    
        tempy = y
        while tempx > 0 and tempy < 7 and board[coor_to_index(tempx-1, tempy+1)] == opp: # keep going left+up
            tempx -= 1
            tempy += 1
        new_index = coor_to_index(tempx-1, tempy+1)
        if in_range(tempx-1, tempy+1) and board[new_index] == token:
            for i in range(0, abs(x-(tempx-1))):
                newx = (tempx-1) + i
                newy = (tempy+1) - i
                board[coor_to_index(newx, newy)] = token
    if x < 6 and y > 1 and board[coor_to_index(x+1, y-1)] == opp: # diagonal right down
        tempx = x    
        tempy = y
        while tempx < 7 and tempy > 0 and board[coor_to_index(tempx+1, tempy-1)] == opp: # keep going right+down
            tempx += 1
            tempy -= 1
        new_index = coor_to_index(tempx+1, tempy-1)
        if in_range(tempx+1, tempy-1) and board[new_index] == token:
            for i in range(0, abs((tempx+1)-x)):
                newx = (tempx+1) - i
                newy = (tempy-1) + i
                board[coor_to_index(newx, newy)] = token
    if x < 6 and y < 6 and board[coor_to_index(x+1, y+1)] == opp: # diagonal right up
        tempx = x    
        tempy = y
        while tempx < 7 and tempy < 7 and board[coor_to_index(tempx+1, tempy+1)] == opp: # keep going right+up
            tempx += 1
            tempy += 1
        new_index = coor_to_index(tempx+1, tempy+1)
        if in_range(tempx+1, tempy+1) and board[new_index] == token:
            for i in range(0, abs((tempx+1)-x)):
                newx = (tempx+1) - i
                newy = (tempy+1) - i
                board[coor_to_index(newx, newy)] = token
    return "".join(board)

board = sys.argv[1] # grab the board
token = sys.argv[2] # grab the token
indexes = possibleMoves(board, token)
print(indexes)
for i in indexes:
    print(move(board, token, i))
 

# board = ""
# board = "...xo.oo......oo.......o........x..............................."
# for i in range(64):
#     x, y = index_to_coor(i)
#     add = False
#     if x == 6:
#         if y == 2:
#             add = True
#             board += "x"
#     if x == 5:
#         if y == 3:
#             add = True
#             board += "o"
#     if x == 4:
#         if y == 4:
#             add = True
#             board += "o"
#     # if x == 0:
#     #     if y == 6:
#     #         add = True
#     #         board += "o"
#     # if x == 1:
#     #     if y == 6:
#     #         add = True
#     #         board += "x"
#     if add == False:
#         board += "."
# print_board(board)
# print()
# for i in possibleMoves(board, "x"):
#     if i == 19:
#         print(index_to_coor(i))
#         print_board(board)
#         print()
#         print_board(move(board, "x", i))
#         print()
#         print_board("xox.ooxxxoo.....xo.x....ooxxo..oo.xxo..oo..xxx.xo...xooxxox.....")
    # print(index_to_coor(i))
    # print_board(board)
    # print()
    # print_board(move(board, "x", i))
