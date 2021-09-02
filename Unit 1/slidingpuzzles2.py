# -*- coding: utf-8 -*-

import sys
from collections import deque
import time
from heapq import heappush, heappop, heapify

s = sys.argv[1]   
           
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

# BFS finds shortest solution path (step 5), uncomment solution to obtain solution path
def shortest_path(board):
    path=0
    fringe = deque()                        # queue to look at
    visited = set()                         # puzzles already analyzed
    mem = dict()                            # keeps track of the parent node of each puzzle
    fringe.append(board)
    visited.add(board)
    mem[board] = ""                         # adds the root as parent
    while len(fringe)>0:
        v = fringe.popleft()
        if find_goal(board) == v:           # is puzzle solved?
            parent = mem[v]         
            while parent != "":             # keeps going a step back until reaches root
                path+=1
                parent = mem[parent]
            return path                     # returns solution length
        for c in get_children(v):
            if c not in visited:            # if child is new puzzle add it to the line 
                mem[c] = v
                fringe.append(c)
                visited.add(c)
    return None

# k-limited DFS, search every possible non-looping path of length k
def k_DFS(start_state, k):
    fringe = []
    start_node = (start_state, 0, {start_state})
    # start_node[2].add(start_state)
    fringe.append(start_node)
    while len(fringe) > 0:
        v = fringe.pop()
        if find_goal(start_state) == v[0]:
            return v[1]
        if v[1] < k:
            for c in get_children(v[0]):
                # print(v[2])
                if c not in v[2]:
                    temp = (c, v[1]+1, v[2].copy())
                    temp[2].add(c)
                    fringe.append(temp)
    return None

# iterative deepening depth-first search
def ID_DFS(start_state):
    max_depth = 0
    result = None
    while result is None:
        result = k_DFS(start_state, max_depth)
        max_depth += 1
    return result

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

# =============================================================================
# run code    
# =============================================================================
with open(s) as f:
    count=0
    for line in f:
        l = line.split()
        size = int(l[0])
        board = l[1]
        start = time.perf_counter()
        parity = parity_check(size, board)
        end = time.perf_counter()
        if not parity:
            print("Line %s: %s, no solution determined in %s seconds" % (count,board,end-start))
        else:
            if l[2] == "B":
                start = time.perf_counter()
                bfs_moves = shortest_path(board)
                end = time.perf_counter()
                print("Line %s: %s, BFS - %s moves in %s seconds" % (count,board,bfs_moves,end-start))
            elif l[2] == "I":
                start = time.perf_counter()
                dfs_moves = ID_DFS(board)
                end = time.perf_counter()
                print("Line %s: %s, ID-DFS - %s moves in %s seconds" % (count,board,dfs_moves,end-start))
            elif l[2] == "A":
                start = time.perf_counter()
                a_moves = a_star(board)
                end = time.perf_counter()
                print("Line %s: %s, A* - %s moves in %s seconds" % (count,board,a_moves,end-start))
            else:
                start = time.perf_counter()
                bfs_moves = shortest_path(board)
                end = time.perf_counter()
                print("Line %s: %s, BFS - %s moves in %s seconds" % (count,board,bfs_moves,end-start))
                start = time.perf_counter()
                dfs_moves = ID_DFS(board)
                end = time.perf_counter()
                print("Line %s: %s, ID-DFS - %s moves in %s seconds" % (count,board,dfs_moves,end-start))
                start = time.perf_counter()
                a_moves = a_star(board)
                end = time.perf_counter()
                print("Line %s: %s, A* - %s moves in %s seconds" % (count,board,a_moves,end-start))
        print()
        count+=1



