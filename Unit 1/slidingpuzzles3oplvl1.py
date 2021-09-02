# -*- coding: utf-8 -*-

from heapq import heappush, heappop, heapify
import time
import sys

goal = {"A":(1,4), "B":(2,4), "C":(3,4), "D":(4,4), "E":(1,3), "F":(2,3), "G":(3,3), "H":(4,3), "I":(1,2), "J":(2,2), "K":(3,2), "L":(4,2), "M":(1,1), "N":(2,1), "O":(3,1), ".":(4,1)}

# finds the goal state of the board (sorted string)
def find_goal(board):
    s = "".join(sorted(board))
    return s[1:]+s[0]

# converts index of a board into (x,y)
def index_to_coor(board, index):
    size = int(int(len(board))**(1/2))
    y = size - int(index/size)
    x = (index%size) + 1
    return x, y

# converts (x,y) to index
def coor_to_index(board, x, y):
    size = int(int(len(board))**(1/2))
    var = size-y
    return ((size*var) + x - 1)

# find the taxicab distance, bare min of moves each tile moves to correct pos
def taxicab_dis(board):
    goal = find_goal(board)
    count = 0
    for x in board:
        if x != ".":
            bx, by = index_to_coor(board, board.index(x))
            gx, gy = index_to_coor(goal, goal.index(x))
            count += abs(bx - gx) + abs(by - gy)
    return count

# finds number of unordered pairs
def unordered_pairs(board):
    if board.index(".") == len(board)-1:
        no_blank = board[:-1]
    else:
        no_blank = board[:board.index(".")]+board[board.index(".")+1:]
    l=[[no_blank[y],no_blank[x]] for x in range(len(no_blank)) for y in range(x+1, len(no_blank)) if no_blank[x] > no_blank[y]]
    return len(l)

# parity check to see if board is solvable
def parity_check(size, board):
    if size%2 != 0:
        return True if unordered_pairs(board)%2 == 0 else False
    else:
        x, y = index_to_coor(board, board.index("."))
        if y%2 == 0:
            return True if unordered_pairs(board)%2 != 0 else False
        else:
            return True if unordered_pairs(board)%2 == 0 else False

# returns all the possible moves
def get_children(board):
    size = int(int(len(board))**(1/2))
    space_index = board.index(".")              # where is the blank tile
    x, y = index_to_coor(board, space_index)    # find coordinates of the blank tile
    l = set()
    # blank tile goes to the right 
    if(x<size):
        index = int(coor_to_index(board, x+1, y))
        c = board[:index-1]+board[index]+board[index-1]+board[index+1:]
        gx, gy = goal[str(board[index])]
        dist_after = abs(x - gx) + abs(y - gy)
        dist_before = abs(x+1 - gx) + abs(y - gy)
        step = -1 if dist_before > dist_after else 1
        l.add((c,step))
    # blank tile goes to the left
    if(x>1):
        index = int(coor_to_index(board, x-1, y))
        c = board[:index]+board[index+1]+board[index]+board[index+2:]
        gx, gy = goal[str(board[index])]
        dist_after = abs(x - gx) + abs(y - gy)
        dist_before = abs(x-1 - gx) + abs(y - gy)
        step = -1 if dist_before > dist_after else 1
        l.add((c,step))
    # blank tile goes up
    if(y<size):
        index = int(coor_to_index(board, x, y+1))
        c = board[:index]+board[space_index]+board[index+1:space_index]+board[index]+board[space_index+1:]
        gx, gy = goal[str(board[index])]
        dist_after = abs(x - gx) + abs(y - gy)
        dist_before = abs(x - gx) + abs(y+1 - gy)
        step = -1 if dist_before > dist_after else 1
        l.add((c,step))
    # blank tile goes down
    if(y>1):
        index = int(coor_to_index(board, x, y-1))
        c = board[:space_index]+board[index]+board[space_index+1:index]+board[space_index]+board[index+1:]
        gx, gy = goal[str(board[index])]
        dist_after = abs(x - gx) + abs(y - gy)
        dist_before = abs(x - gx) + abs(y-1 - gy)
        step = -1 if dist_before > dist_after else 1
        l.add((c,step))
    return l

# prints the board as a grid
def print_puzzle(size, board):
    for x in range(0,size**2,size):
        print(" ".join(board[x:x+size]))

# A* search
def a_star(start_state):
    # print("%s , %s" % (start_state[0], start_state[1]))
    # if start_state[0].isdigit() or start_state[1].isdigit():
    #     goal = goal_num
    # else:
    #     goal = goal_alpha
    # print(goal)
    closed = set()
    start_node = (taxicab_dis(start_state), start_state, 0)
    fringe = []
    heappush(fringe, start_node)
    while len(fringe) > 0:
        v = heappop(fringe)
        if find_goal(start_state) == v[1]:
            return v[2]
        if v[1] not in closed:
            closed.add(v[1])
            for c, s in get_children(v[1]):
                if c not in closed:
                    temp = (v[0]+int(s)+1, c, v[2]+1)
                    heappush(fringe, temp)
    return None

s = sys.argv[1]

with open(s) as f:
    count=0
    for line in f:
        start = time.perf_counter()
        board = line.strip()
        moves = a_star(board)
        end = time.perf_counter()
        print("Line %s: %s, %s moves found in %s seconds" % (count,board,moves,(end-start)))      
        print()
        count+=1