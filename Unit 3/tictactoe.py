# -*- coding: utf-8 -*-

import sys
from collections import deque
from heapq import heappush, heappop, heapify

constraints = []

def build_constraints(): # eat set has indices of each col, row, diagonal
    global constraints
    con = []
    for r in range(0, 9, 3):
        row = []
        for c in range(3):
            row.append(c+r)
        con.append(row)
    for c in range(3):
        col = []
        for r in range(0, 9, 3):
            col.append(c+r)
        con.append(col)
    dia = [0, 4, 8]
    con.append(dia)
    dia = [2, 4, 6]
    con.append(dia)
    constraints = con
    return con

def print_board(board):
    print("Current board:")
    for n in range(0, 9, 3):
        print(board[n:n+3] + "\t" + str(n)+str(n+1)+str(n+2))
    print()

def win(board): 
    for c in constraints: # go through each col, row, diagonal
        if board[c[0]] != "." and board[c[0]] == board[c[1]] and board[c[0]] == board[c[2]]:
            return board[c[0]] # return X or O win
    return None # no win

def game_over(board):
    if win(board) is not None: # X or O
        return True
    if "." not in board: # tie
        return True
    return False

def next_board(board):
    # moves = deque() # used for pt1
    moves = []
    if board.count(".")%2 == 0: # O move
        for i in range(len(board)):
            if board[i] == ".":
                temp = board[:i]+"O"+board[i+1:]
                moves.append((temp, i))
    else: # X move
        for i in range(len(board)):
            if board[i] == ".":
                temp = board[:i]+"X"+board[i+1:]
                moves.append((temp, i))
    return moves

def pos_moves(board): # return possible moves
    moves = next_board(board)
    temp = ""
    for b, m in moves:
       temp += str(m) + ", " 
    temp = temp[:-2]
    return temp

# def print_moves(board, player):
#     moves = []
#     if player == "X":
#         val = max_move(board)
#         for m, v in val:
#             temp = "loss"
#             if v == 1: temp = "win"
#             if v == 0: temp = "tie"
#             print("Moving at %s results in a %s" % (m, temp))
#             moves.append(m)
#         print()
#         return max(moves)
#     else:
#         val = min_move(board)
#         for m, v in val:
#             temp = "loss"
#             if v == -1: temp = "win"
#             if v == 0: temp = "tie"
#             print("Moving at %s results in a %s" % (m, temp))
#             moves.append(m)
#         print()
#         return min(moves)

def total(board): # return total sequences of games and total possible outcomes
    moves = next_board(board) # moves is a queue
    total_games = []
    final_boards = set()
    while len(moves) > 0:
        b, i = moves.popleft() # take left most child/next move
        if game_over(b):
            total_games.append(b)
            final_boards.add(b) # avoids duplicates (diff seq but same outcome)
        else:
            for m, i in next_board(b):
                moves.append(m) # adds the next moves to moves
    return total_games, final_boards

def stats(final_boards): # counts how many steps for win
    countX5 = 0
    countX7 = 0
    countX9 = 0
    countO6 = 0
    countO8 = 0
    countDraws = 0
    for b in final_boards:
        count = b.count(".")
        if win(b) is None:
            countDraws +=1 
        elif count == 4:
            countX5+= 1
        elif count == 2:
            countX7 += 1
        elif count == 0:
            countX9 += 1
        elif count == 3:
            countO6 +=1
        else:
            countO8 +=1
    return countX5, countX7, countX9, countO6, countO8, countDraws

def score(board): # returns weight of board
    if win(board) is None: # tie
        return 0
    if win(board) == "X":
        return 1
    return -1

def max_step(board): # return max weight of future outcome
    if game_over(board):
        return score(board)
    results = []
    for next_b, m in next_board(board):
        results.append(min_step(next_b))
    return max(results)

def min_step(board): # return min weight of future outcome
    if game_over(board):
        return score(board)
    results = []
    for next_b, m in next_board(board):
        results.append(max_step(next_b))
    return min(results)

def max_move(board): # return max move location, play X
    values = []
    for next_b, m in next_board(board):
        res = min_step(next_b)
        if res == 1:
            print("Moving at %s results in a win." % (m))
        elif res == 0: 
            print("Moving at %s results in a tie." % (m))
        else:
            print("Moving at %s results in a loss." % (m))
        values.append((m, res))
    print()
    maxm, maxv = values[0]
    for move, val in values:
        if val > maxv: 
            maxv = val
            maxm = move
    return maxm

def min_move(board): # return min move location, play O
    values = []
    for next_b, m in next_board(board):
        res = max_step(next_b)
        if res == 1:
            print("Moving at %s results in a loss." % (m))
        elif res == 0: 
            print("Moving at %s results in a tie." % (m))
        else:
            print("Moving at %s results in a win." % (m))
        values.append((m, res))
    print()
    minm, minv = values[0]
    for move, val in values:
        if val < minv: 
            minv = val
            minm = move
    return minm
    
def computer_X(board): # computer play X first (either board empty or next turn is X)
    while game_over(board) == False:
        print_board(board)
        move = max_move(board)
        print("I choose space %s" % (move))
        board = board[:move]+"X"+board[move+1:]
        print()
        if game_over(board):
            print_board(board)
            w = win(board)
            if w == "X":
                print("I win!")
            elif w == "O":
                print("You win!")
            else:
                print("We tied!")
            break;
        print_board(board)
        print("You can move to any of these spaces: %s." % (pos_moves(board)))
        move = int(input("Your choice? "))
        print()
        board = board[:move]+"O"+board[move+1:]
        if game_over(board):
            print_board(board)
            w = win(board)
            if w == "X":
                print("I win!")
            elif w == "O":
                print("You win!")
            else:
                print("We tied!")
            break;

def player_X(board): # board empty and player play first
    while game_over(board) == False:
        print_board(board)
        print("You can move to any of these spaces: %s." % (pos_moves(board)))
        move = int(input("Your choice? "))
        print()
        board = board[:move]+"X"+board[move+1:]
        if game_over(board):
            print_board(board)
            w = win(board)
            if w == "X":
                print("You win!")
            elif w == "O":
                print("I win!")
            else:
                print("We tied!")
            break;
        print_board(board)
        move = min_move(board)
        print("I choose space %s" % (move))
        board = board[:move]+"O"+board[move+1:]
        print()
        if game_over(board):
            print_board(board)
            w = win(board)
            if w == "X":
                print("You win!")
            elif w == "O":
                print("I win!")
            else:
                print("We tied!")
            break;

def computer_O(board): # board not empty, computer play O first
    while game_over(board) == False:
        print_board(board)
        move = min_move(board)
        print("I choose space %s" % (move))
        board = board[:move]+"O"+board[move+1:]
        print()
        if game_over(board):
            print_board(board)
            w = win(board)
            if w == "O":
                print("I win!")
            elif w == "X":
                print("You win!")
            else:
                print("We tied!")
            break;
        print_board(board)
        print("You can move to any of these spaces: %s." % (pos_moves(board)))
        move = int(input("Your choice? "))
        print()
        board = board[:move]+"X"+board[move+1:]
        if game_over(board):
            print_board(board)
            w = win(board)
            if w == "O":
                print("I win!")
            elif w == "X":
                print("You win!")
            else:
                print("We tied!")
            break;

build_constraints()
board = sys.argv[1] # grab the board
if game_over(board):
    print()
    print_board(board)
    print("%s victory!" % (win(board)))
else:
    cnt = board.count(".")
    if cnt == 9: # board is empty
        computer = input("Should I be X or O? ")
        print()
        if computer == "O": 
            player_X(board)
        else:
            computer_X(board)
    else:
        if cnt%2 == 0:
            computer = "O"
            print()
            computer_O(board)
        else:
            computer = "X"
            print()
            computer_X(board)
