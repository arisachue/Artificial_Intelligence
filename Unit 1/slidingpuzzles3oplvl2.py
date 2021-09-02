# -*- coding: utf-8 -*-

from heapq import heappush, heappop, heapify

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
        l.add(c)
    # blank tile goes to the left
    if(x>1):
        index = int(coor_to_index(board, x-1, y))
        c = board[:index]+board[index+1]+board[index]+board[index+2:]
        l.add(c)
    # blank tile goes up
    if(y<size):
        index = int(coor_to_index(board, x, y+1))
        c = board[:index]+board[space_index]+board[index+1:space_index]+board[index]+board[space_index+1:]
        l.add(c)
    # blank tile goes down
    if(y>1):
        index = int(coor_to_index(board, x, y-1))
        c = board[:space_index]+board[index]+board[space_index+1:index]+board[space_index]+board[index+1:]
        l.add(c)
    return l

row1="ABCD"
row2="EFGH"
row3="IJKL"
row4="MNO."

def heuristic(board):
    temp=""
    count=0
    order=0
    for x in range(0,4):
        if board[x] in row1:
            temp+= board
    s = "".join(sorted(board))
    if temp == s:
        count+=0
    elif temp == s[::-1]:
        count+=6
    for x in range(len(temp)-1):
        if temp[x] >
        

# A* search
def a_star(start_state):
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
            for c in get_children(v[1]):
                if c not in closed:
                    temp = (v[2]+1+taxicab_dis(c), c, v[2]+1)
                    heappush(fringe, temp)
    return None