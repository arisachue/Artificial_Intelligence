# -*- coding: utf-8 -*-

from heapq import heappush, heappop, heapify
import time
from collections import deque

goal_gol = {"A":(1,5), "B":(2,5), "C":(3,5), "D":(4,5), "E":(5,5), "F":(1,4), "G":(2,4), "H":(3,4), "I":(4,4), "J":(5,4), "K":(1,3), "L":(2,3), "M":(3,3), "N":(4,3), "O":(5,3), "P":(1,2), "Q":(2,2), "R":(3,2), "S":(4,2), "T":(5,2), "U":(1,1), "V":(2,1), "W":(3,1), "X":(4,1), ".":(5,1)}
# goal_gol = {"A":(1,4), "B":(2,4), "C":(3,4), "D":(4,4), "E":(1,3), "F":(2,3), "G":(3,3), "H":(4,3), "I":(1,2), "J":(2,2), "K":(3,2), "L":(4,2), "M":(1,1), "N":(2,1), "O":(3,1), ".":(4,1)}
# goal_gol = {"A":(1,3), "B":(2,3), "C":(3,3), "D":(1,2), "E":(2,2), "F":(3,2), "G":(1,1), "H":(2,1), ".":(3,1)}
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
def a_get_children(board):
    size = int(int(len(board))**(1/2))
    space_index = board.index(".")              # where is the blank tile
    x, y = index_to_coor(board, space_index)    # find coordinates of the blank tile
    l = set()
    # blank tile goes to the right 
    if(x<size):
        index = int(coor_to_index(board, x+1, y))
        c = board[:index-1]+board[index]+board[index-1]+board[index+1:]
        gx, gy = goal_gol[str(board[index])]
        dist_after = abs(x - gx) + abs(y - gy)
        dist_before = abs(x+1 - gx) + abs(y - gy)
        step = -1 if dist_before > dist_after else 1
        l.add((c,step))
    # blank tile goes to the left
    if(x>1):
        index = int(coor_to_index(board, x-1, y))
        c = board[:index]+board[index+1]+board[index]+board[index+2:]
        gx, gy = goal_gol[str(board[index])]
        dist_after = abs(x - gx) + abs(y - gy)
        dist_before = abs(x-1 - gx) + abs(y - gy)
        step = -1 if dist_before > dist_after else 1
        l.add((c,step))
    # blank tile goes up
    if(y<size):
        index = int(coor_to_index(board, x, y+1))
        c = board[:index]+board[space_index]+board[index+1:space_index]+board[index]+board[space_index+1:]
        gx, gy = goal_gol[str(board[index])]
        dist_after = abs(x - gx) + abs(y - gy)
        dist_before = abs(x - gx) + abs(y+1 - gy)
        step = -1 if dist_before > dist_after else 1
        l.add((c,step))
    # blank tile goes down
    if(y>1):
        index = int(coor_to_index(board, x, y-1))
        c = board[:space_index]+board[index]+board[space_index+1:index]+board[space_index]+board[index+1:]
        gx, gy = goal_gol[str(board[index])]
        dist_after = abs(x - gx) + abs(y - gy)
        dist_before = abs(x - gx) + abs(y-1 - gy)
        step = -1 if dist_before > dist_after else 1
        l.add((c,step))
    return l

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

# A* search
def a_star(start_state):
    count=0
    closed = set()
    start_node = (taxicab_dis(start_state), start_state, 0)
    fringe = []
    heappush(fringe, start_node)
    while len(fringe) > 0:
        v = heappop(fringe)
        count+=1
        if find_goal(start_state) == v[1]:
            return v[2]
        if v[1] not in closed:
            closed.add(v[1])
            for c, s in a_get_children(v[1]):
                if c not in closed:
                    temp = (v[0]+int(s)+1, c, v[2]+1)
                    heappush(fringe, temp)
    return None

# k-limited DFS, search every possible non-looping path of length k
def k_DFS(start_state, k):
    count=0
    fringe = []
    start_node = (start_state, 0, {start_state})
    fringe.append(start_node)
    while len(fringe) > 0:
        v = fringe.pop()
        count+=1
        if find_goal(start_state) == v[0]:
            return v[1], count
        if v[1] < k:
            for c in get_children(v[0]):
                # print(v[2])
                if c not in v[2]:
                    temp = (c, v[1]+1, v[2].copy())
                    temp[2].add(c)
                    fringe.append(temp)
    return None, None

# iterative deepening depth-first search
def ID_DFS(start_state):
    tcount=0
    max_depth = 0
    result = None
    while result is None:
        result, count = k_DFS(start_state, max_depth)
        max_depth += 1
        if count != None:
            tcount+=count
    return tcount

# BFS finds shortest solution path (step 5), uncomment solution to obtain solution path
def shortest_path(board):
    count=0
    path=0
    fringe = deque()                        # queue to look at
    visited = set()                         # puzzles already analyzed
    # mem = dict()                            # keeps track of the parent node of each puzzle
    fringe.append(board)
    visited.add(board)
    # mem[board] = ""                         # adds the root as parent
    while len(fringe)>0:
        v = fringe.popleft()
        count+=1
        if find_goal(board) == v:           # is puzzle solved?
            # parent = mem[v]         
            # while parent != "":             # keeps going a step back until reaches root
            #     path+=1
            #     parent = mem[parent]
            return count                     # returns solution length
        for c in get_children(v):
            if c not in visited:            # if child is new puzzle add it to the line 
                # mem[c] = v
                fringe.append(c)
                visited.add(c)
    return None

lengths=dict()
# BFS that returns reachable locations with goal state (step 4)
def reachable_loc(goal_board):
    fringe = deque()
    visited = set()
    fringe.append((goal_board,0,""))
    visited.add(goal_board)
    lengths[0] = goal_board
    while len(fringe)>0:
        v, p, par = fringe.popleft()
        if p == 1:
            lengths[p]=v 
        if p > 1 and lengths[p-1] != par:
            lengths[p] = v
        if p > 31:
            return lengths
        for c in get_children(v):
            if c not in visited:
                newpath = p+1
                fringe.append((c,newpath,v))
                visited.add(c)
                              
        
    return visited                        # returns the puzzles visited (order: hardest -> easiest)

# puzzles=reachable_loc("ABCDEFGHIJKLMNOPQRSTUVWX.")
# print(len(lengths))
# for l in lengths:
#     print(lengths[l])
    
# board = "HFGBEDC.A"
# start = time.perf_counter()
# nodes, moves = a_star(board)
# end = time.perf_counter()
# print(moves)
# print("a*star (8): total:%s, %s, time:%s" % (nodes, nodes/(end-start), end-start))
# board = "EFHA.BCDMJLONGIK"
# start = time.perf_counter()
# nodes, moves = a_star(board)
# end = time.perf_counter()
# print(moves)
# print("a*star (15): total:%s, %s, time:%s" % (nodes, nodes/(end-start), end-start))
# board = "GACDE.BHIJFQMNTLKROXUVPSW"
# start = time.perf_counter()
# nodes, moves = a_star(board)
# end = time.perf_counter()
# print(moves)
# print("a*star (24): total:%s, %s, time:%s" % (nodes, nodes/(end-start), end-start))
# start = time.perf_counter()
# moves = ID_DFS(board)
# end = time.perf_counter()
# print("ID_DFS: total:%s, %s, time:%s" % (moves, moves/(end-start), end-start))
# board = "ABCFEJGD.MLHNIKO"
# start = time.perf_counter()
# moves = shortest_path(board)
# end = time.perf_counter()
# print("bfs: total:%s, %s, time:%s" % (moves, moves/(end-start), end-start))

with open("24_puzzles.txt") as f:
    count=0
    for line in f:
        board = line.strip()
        moves = a_star(board)
        print("line: %s, moves: %s" % (count, moves))
# board = "CA.HGNFDIBEKMLOJ"
# start = time.perf_counter()
# moves = a_star(board)
# end = time.perf_counter()
# if (end-start) > 10:
#     print(board)
#     print("a*star: total:%s, %s, time:%s" % (moves, moves/(end-start), end-start))
# start = time.perf_counter()
# moves = ID_DFS(board)
# end = time.perf_counter()
# if (end-start) > 10:
#     print("ID-DFS: total:%s, %s, time:%s" % (moves, moves/(end-start), end-start))
# start = time.perf_counter()
# moves = shortest_path(board)
# end = time.perf_counter()
# if (end-start) > 10:
#     print("BFS: total:%s, %s, time: %s" % (moves, moves/(end-start), end-start))
        # print()
        # count+=1