# -*- coding: utf-8 -*-

from collections import deque
import time
import sys

alpha=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
singleton=0

def exist(word):
    return True if word in dic else False

# returns all the possible moves
def get_children(word):
    l = []
    for i in range(len(word)):
        for a in alpha:
            st = word[:i]+a
            if i < (len(word)-1):
                st += word[i+1:]
            if exist(st) and st != word:
                l.append(st) 
    # l.append(word)
    return l

# BFS finds shortest solution path (step 5), uncomment solution to obtain solution path
def shortest_path(word, goal):
    path=1
    fringe = deque()                        # queue to look at
    visited = set()                         # puzzles already analyzed
    mem = dict()                            # keeps track of the parent node of each puzzle
    fringe.append(word)
    visited.add(word)
    mem[word] = ""                         # adds the root as parent
    solution=[]
    while len(fringe)>0:
        v = fringe.popleft()
        if v == goal:           # is puzzle solved?
            solution.append(v)
            parent = mem[v]         
            while parent != "":             # keeps going a step back until reaches root
                path+=1
                solution.append(parent)
                parent = mem[parent]                
            return path, solution
        for c in get_children(v):
            if c not in visited:            # if child is new puzzle add it to the line 
                mem[c] = v
                fringe.append(c)
                visited.add(c)
    return 0, "No solution!"
        
# BFS that returns reachable locations with goal state (step 4)
def reachable_loc(word):
    fringe = deque()
    visited = set()
    last = []                       # stack with same values as set (stacks are more efficient)
    fringe.append(word)
    visited.add(word)
    while len(fringe)>0:
        v = fringe.popleft()
        for c in get_children(v):
            if c not in visited:
                fringe.append(c)
                visited.add(c)
                last.append(c)
    return last

dic=set()
# dic=[]
with open("words_06_letters.txt") as f:
    for line in f:
        dic.add(line.strip())

puzzle=dict()
with open("puzzles_normal.txt") as f:
    for line in f:
        temp = line.strip().split()
        puzzle[temp[0]]=temp[1]
        
# =============================================================================
# RUN CODE
# =============================================================================
max=0
max_key=""
# max = 1625
storage=set()
count=0
path_max=0
sol_max=[]
index =0
# stk = reachable_loc("hawked")
# for x in stk:
#     for y in stk:
#         path, sol = shortest_path(x, y)
#         if path > path_max:
#             path_max = path
#             sol_max = sol

st = reachable_loc("hawked")
for x in st:
    reach = reachable_loc(x)
    last = reach.pop()
    path, sol = shortest_path(x, last)
    if path > path_max:
        path_max = path
        sol_max = sol
print("Length: %d" % path)
print("\n".join(sol[::-1]))

# for d in dic:
#     # print(d)
#     temp = reachable_loc(d)
#     # if temp not in storage:
#     #     storage.add(temp)
#     # count+=1
#     if temp > max:
#         max = temp
#         max_key=d
#         # print(count)
# # print(len(storage))
# print("max: %s max key: %s" % (str(max), max_key))
# for i in range(len(dic)-1, 0, -1):
#     temp = dic.pop()
#     path = reachable_loc(temp)
#     if path > path_max:
#         path_max = path
#         index = i
# print("max: %d max key: %d" % (path_max, index))
# print("word: " + dic[index])
looked = set()
for d in dic:
    if d not in looked:
        count+=1
        temp = reachable_loc(d)
        for x in temp:
            looked.add(x)
    
print(count)