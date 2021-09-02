# -*- coding: utf-8 -*-

from collections import deque
import time
import sys

# prints the board as a grid
def print_puzzle(size, board):
    for x in range(0,size**2,size):
        print(" ".join(board[x:x+size]))
   
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
    
# returns all the possible moves
def get_children(board):
    size = int(int(len(board))**(1/2))
    space_index = board.index(".")              # where is the blank tile
    x, y = index_to_coor(board, space_index)    # find coordinates of the blank tile
    l = []
    # blank tile goes to the right 
    if(x<size):
        index = int(coor_to_index(board, x+1, y))
        c = board[:index-1]+board[index]+board[index-1]+board[index+1:]
        l.append(c)
    # blank tile goes to the left
    if(x>1):
        index = int(coor_to_index(board, x-1, y))
        c = board[:index]+board[index+1]+board[index]+board[index+2:]
        l.append(c)
    # blank tile goes up
    if(y<size):
        index = int(coor_to_index(board, x, y+1))
        c = board[:index]+board[space_index]+board[index+1:space_index]+board[index]+board[space_index+1:]
        l.append(c)
    # blank tile goes down
    if(y>1):
        index = int(coor_to_index(board, x, y-1))
        c = board[:space_index]+board[index]+board[space_index+1:index]+board[space_index]+board[index+1:]
        l.append(c)
    return l

# check if board is completed    
def goal_test(board):
    return True if(board == find_goal(board)) else False


def bibfs(board):
    goal = find_goal(board)
    path=0
    source_fringe = deque()                        # queue to look at
    source_visited = set()                         # puzzles already analyzed
    goal_fringe = deque()
    goal_visited = set()
    source_mem = dict()                            # keeps track of the parent node of each puzzle
    goal_mem=dict()
    source_fringe.append(board)
    source_visited.add(board)
    goal_fringe.append(goal)
    goal_visited.add(goal)
    source_mem[board] = ""                         # adds the root as parent
    goal_mem[find_goal(board)] = ""
    # solution=[]
    while len(source_fringe)>0 and len(goal_fringe)>0:
        if len(source_fringe)>0:
            sv = source_fringe.popleft()
            if find_goal(board) == sv:
                # solution.append(sv)
                parent = source_mem[sv]         
                while parent != "":             # keeps going a step back until reaches root
                    path+=1
                    # solution.append(parent)
                    parent = source_mem[parent]
                return path
            if sv in goal_visited:
                # solution.append(sv)
                child = goal_mem[sv]
                while child != "":
                    path+=1
                    # solution.append(child)
                    child = goal_mem[child]
                # solution = solution[::-1]
                parent = source_mem[sv]         
                while parent != "":             # keeps going a step back until reaches root
                    path+=1
                    # solution.append(parent)
                    parent = source_mem[parent]
                return path
            for c in get_children(sv):
                if c not in source_visited:            # if child is new puzzle add it to the line 
                    source_mem[c] = sv
                    source_fringe.append(c)
                    source_visited.add(c)
        if len(goal_fringe)>0:
            gv = goal_fringe.popleft()
            if board == gv:
                # solution.append(gv)
                child = goal_mem[gv]
                while child != "":             # keeps going a step back until reaches root
                    path+=1
                    # solution.append(child)
                    child = goal_mem[child]
                return path
            if gv in source_visited:
                # solution.append(gv)
                child = goal_mem[gv]
                while child != "":
                    path+=1
                    # solution.append(child)
                    child = goal_mem[child]
                # solution = solution[::-1]
                parent = source_mem[gv]         
                while parent != "":             # keeps going a step back until reaches root
                    path+=1
                    # solution.append(parent)
                    parent = source_mem[parent]               
                return path
            for c in get_children(gv):
                if c not in goal_visited:            # if child is new puzzle add it to the line 
                    goal_mem[c] = gv
                    goal_fringe.append(c)
                    goal_visited.add(c)
    return None

def shortest_path(board):
    path=0
    fringe = deque()                        # queue to look at
    visited = set()                         # puzzles already analyzed
    mem = dict()                            # keeps track of the parent node of each puzzle
    fringe.append(board)
    visited.add(board)
    mem[board] = ""                         # adds the root as parent
    # solution=[]
    while len(fringe)>0:
        v = fringe.popleft()
        if find_goal(board) == v:           # is puzzle solved?
            # solution.append(v)
            parent = mem[v]         
            while parent != "":             # keeps going a step back until reaches root
                path+=1
                # solution.append(parent)
                parent = mem[parent]
            return path                     # returns solution length
            # return path, solution
        for c in get_children(v):
            if c not in visited:            # if child is new puzzle add it to the line 
                mem[c] = v
                fringe.append(c)
                visited.add(c)
    return None

s = sys.argv[1]   
           
with open(s) as f:
    count=0
    for line in f:
        l = line.split()
        size = int(l[0])
        board = l[1]
        start = time.perf_counter()
        moves = shortest_path(board)
        end = time.perf_counter()
        print("(BFS) Line %s: %s, %s moves found in %s seconds" % (count,board,moves,(end-start)))   
        start = time.perf_counter()
        moves = bibfs(board)
        end = time.perf_counter()
        print("(biBFS) Line %s: %s, %s moves found in %s seconds" % (count,board,moves,(end-start)))   
        count+=1


