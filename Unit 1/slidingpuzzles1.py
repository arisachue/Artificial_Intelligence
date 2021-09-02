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

# goes through check board in textfile (step 3)
# =============================================================================
# with open("slide_puzzle_tests.txt") as f:
#     count=0
#     for line in f:
#         l = line.split()
#         size = int(l[0])
#         board = l[1]
#         print("Line %d start state: " % count) 
#         print_puzzle(size, board)
#         print("Line %d goal state: " % count)
#         print_puzzle(size, find_goal(board))
#         child = get_children(board)
#         print("Line %d children: " % count)
#         for c in child:
#             print_puzzle(size, c)
#             print()
#         count+=1
# =============================================================================

# BFS that returns reachable locations with goal state (step 4)
def reachable_loc(goal_board):
    fringe = deque()
    visited = set()
    last = []                       # stack with same values as set (stacks are more efficient)
    fringe.append(goal_board)
    visited.add(goal_board)
    while len(fringe)>0:
        v = fringe.popleft()
        for c in get_children(v):
            if c not in visited:
                fringe.append(c)
                visited.add(c)
                last.append(c)
    return last                     # returns the puzzles visited (order: hardest -> easiest)


# BFS finds shortest solution path (step 5), uncomment solution to obtain solution path
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

# find hardest puzzle
def find_hardest(goal_board):
    states = reachable_loc(goal_board)  # gets a stack of all the boards in visited (ordered: hardest -> easiest)
    hard = dict()                       # remembers the hardest puzzle
    temp = states.pop()                 # pops the last puzzle added aka hardest puzzle
    max, path = shortest_path(temp)       
    hard[temp] = path
    for x in range(len(states)):
        temp = states.pop()             # pops next hardest puzzle
        moves, path = shortest_path(temp) 
        if moves == max:
            hard[temp] = path           # adds to hard if puzzle is same difficulty as the hardest puzzle
        else:
            return hard, max            # stops loop if the next puzzle is easier (then all the proceeding puzzles are easier)

# prints out the hardest 3x3 puzzle
def print_hardest8():
    dic, max = find_hardest("12345678.")
    for x in dic:
        print("Start state:")
        print_puzzle(3, x)
        print("Solution:")
        while len(dic[x]) > 0:
            p=dic[x].pop()
            print_puzzle(3, p)
            print()
    print("Solution length: %d" % max)
# step 6
# print_hardest8()
    
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
        print("Line %s: %s, %s moves found in %s seconds" % (count,board,moves,(end-start)))   
        # step 5
        # print("Line %d shortest path: %d" % (count,shortest_path(board)))
        # step 4
        # print("Line %d reachable locations: %d" % (count,reachable_loc(find_goal(board))))
        count+=1


