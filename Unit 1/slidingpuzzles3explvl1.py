# -*- coding: utf-8 -*-

from collections import deque
from heapq import heappush, heappop, heapify

goal_gol = {"A":(1,3), "B":(2,3), "C":(3,3), "D":(1,2), "E":(2,2), "F":(3,2), "G":(1,1), "H":(2,1), ".":(3,1)}

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
            for c, s in a_get_children(v[1]):
                if c not in closed:
                    temp = (v[0]+int(s)+1, c, v[2]+1)
                    heappush(fringe, temp)
    return None

lengths=dict()
multiple_correct=dict()
one_correct=dict()

# =============================================================================
# EXPLORE LEVEL 1
# =============================================================================
# def reachable_loc(goal_board):
#     fringe = deque()
#     visited = set()
#     storage = dict()
#     fringe.append((goal_board,0,""))
#     visited.add(goal_board)
#     storage[goal_board] = 0
#     one_correct[0] = 1
    
#     while len(fringe)>0:
#         v, p, par = fringe.popleft()
#         check_multiple = 0
#         if p in lengths: lengths[p]+=1
#         else: lengths[p]=1
#         newpath = p+1
#         for c in get_children(v):
            
#             if c in storage:
#                 moves = storage[c]
#                 # moves = a_star(c)
#                 # check_multiple = 2
#                 if moves == newpath:
#                     fringe.append((c,newpath,v))
#                     if newpath in multiple_correct: multiple_correct[newpath]+=1
#                     else: multiple_correct[newpath]=1
#                 #     check_multiple = 1
#                 # if c == par:
#                 #     check_multiple = 2
#             else:
#                 # check_multiple+=1
#                 fringe.append((c,newpath,v))
#                 visited.add(c)
#                 storage[c] = newpath
#                 check_multiple = 0
            
#             # if check_multiple == 1:
#             #     if newpath in multiple_correct: multiple_correct[newpath]+=1
#             #     else: multiple_correct[newpath]=1
#             # if check_multiple == 0:
#             #     if newpath in one_correct: one_correct[newpath]+=1
#             #     else: one_correct[newpath]=1
#             # check_multiple = 2
                
# def reachable_loc(goal_board):
#     fringe = deque()
#     visited = set()
#     storage = dict()
#     fringe.append((goal_board,0,False)) # (board, path length, multiple sol?)
#     visited.add(goal_board)
#     storage[goal_board] = 0             # stores the shortest path length for each board
    
#     while len(fringe)>0:
#         v, p, boo = fringe.popleft()    # (board, path length, multiple sol?)
#         if p in lengths:                # counts how many boards per path length
#             lengths[p]+=1
#         else: 
#             lengths[p]=1
            
#         newpath = p+1
#         mul=False
#         for c in get_children(v):
            
#             if boo:                     # if parent has multiple solutions, child should have multiple too
#                 if newpath in multiple_correct: # increments number of multiple solutions at that path length
#                     multiple_correct[newpath]+=1
#                 else: 
#                     multiple_correct[newpath]=1
#                 mul=True                # remembers that this board has multiple path lengths
            
#             if c in storage:            # if board already visited
#                 moves = storage[c]      # takes board's shortest path and if same as current length, increment multiple
#                 if moves == newpath:
#                     if newpath in multiple_correct: multiple_correct[newpath]+=1
#                     else: multiple_correct[newpath]=1
#             else:                       # if new board, add to fringe, visited, and storage
#                 fringe.append((c,newpath,mul))
#                 visited.add(c)
#                 storage[c] = newpath
#             mul=False
#     return visited                     # returns the puzzles visited (order: hardest -> easiest)

# def reachable_loc(goal_board):
#     fringe = deque()
#     visited = dict()
#     fringe.append(goal_board)
#     visited[goal_board] = (0,0)
    
#     while len(fringe)>0:
#         v = fringe.popleft()
#         p, num = visited[v]
#         if p in lengths: lengths[p]+=1
#         else: lengths[p]=1
#         newpath = p+1
#         for c in get_children(v):
            
#             if c in visited:
#                 moves, num = visited[c]
#                 if moves == newpath:
#                     fringe.append(c)
#                     visited[c] = (moves, num+1)
#             else:
#                 fringe.append(c)
#                 visited[c] = (newpath,0)

#     return visited  

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

# def reachable_loc(goal_board):
#     fringe = deque()
#     storage = dict()
#     fringe.append((goal_board,0,{goal_board})) # (board, path length, multiple sol?)
#     storage[goal_board] = 0             # stores the shortest path length for each board
    
#     while len(fringe)>0:
#         v, p, ancestor = fringe.popleft()    # (board, path length, multiple sol?)
#         if p in lengths:                # counts how many boards per path length
#             lengths[p]+=1
#         else: 
#             lengths[p]=1
            
#         newpath = p+1
#         for c in get_children(v):
#             if c not in ancestor:
#                 if c in storage:
#                     moves = storage[c]      # takes board's shortest path and if same as current length, increment multiple
#                     if moves == newpath:
#                         if newpath in multiple_correct: 
#                             multiple_correct[newpath]+=1
#                         else: 
#                             multiple_correct[newpath]=1
#                 else: 
#                     temp = (c, newpath, ancestor.copy())
#                     temp[2].add(c)
#                     fringe.append(temp)
#                     storage[c] = newpath       
            
#     return storage

def reachable_loc(goal_board):
    fringe = deque()
    visited = set()
    storage = dict()
    fringe.append((goal_board,0,"")) # (board, path length, multiple sol?)
    visited.add(goal_board)
    storage[goal_board] = 0             # stores the shortest path length for each board
    
    while len(fringe)>0:
        v, p, par = fringe.popleft()    # (board, path length, multiple sol?)
        if p in lengths:                # counts how many boards per path length
            lengths[p]+=1
        else: 
            lengths[p]=1
            
        newpath = p+1
        for c in get_children(v):
            if par != c:
                if c in storage:
                    moves = storage[c]      # takes board's shortest path and if same as current length, increment multiple
                    if moves == newpath:
                        fringe.append((c,newpath,v))
                        if newpath in multiple_correct: multiple_correct[newpath]+=1
                        else: multiple_correct[newpath]=1
                else:                       # if new board, add to fringe, visited, and storage
                    fringe.append((c,newpath,v))
                    visited.add(c)
                    storage[c] = newpath
    return visited 

# puzzles = reachable_loc("ABCDEFGH.")
# for k in puzzles:
#     moves, num = puzzles[k]
#     if moves in multiple_correct:
#         multiple_correct[moves]+=num
#     else:
#         multiple_correct[moves]=num

# for x in multiple_correct:
#     print(multiple_correct[x])

puzzles = reachable_loc("ABCDEFGH.")
print("Length\tTotal\tUnique\tMultiple")

for l in lengths:
    if l in one_correct:
        uni = one_correct[l]
    else:
        uni = 0
    if l in multiple_correct:
        mul = multiple_correct[l]
    else:
        mul = 0
    print(mul)
    # print("%s\t%s\t%s\t%s" % (l, lengths[l], uni, mul))
# print(get_children("ABCDEFGH."))
