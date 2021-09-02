# -*- coding: utf-8 -*-

from collections import deque
import time
import sys

alpha=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]

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
            if exist(st):
                l.append(st)
    return l

# BFS finds shortest solution path (step 5), uncomment solution to obtain solution path
def shortest_path(word, goal):
    path=1
    fringe = deque()                        # queue to look at
    visited = set()                         # words already analyzed
    mem = dict()                            # keeps track of the parent node of each word
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

dictionary = sys.argv[1]
words = sys.argv[2]

start = time.perf_counter()        
dic=set()
with open(dictionary) as f:
    for line in f:
        dic.add(line.strip())
end = time.perf_counter()
print("Time to create the data structure was: %f seconds" % (end-start))   
print("There are %d words in this dict." % len(dic))
print()

puzzle=dict()
with open(words) as f:
    for line in f:
        temp = line.strip().split()
        puzzle[temp[0]]=temp[1]
        
# =============================================================================
# RUN CODE
# =============================================================================
start = time.perf_counter()
count=0
for p in puzzle:
    print("Line: %d" % count)
    count+=1
    path, sol = shortest_path(p, puzzle[p])
    if path>0:
        print("Length is: %d" % path)
        print("\n".join(sol[::-1]))
    else:  
        print("No solution!")
    print()
end = time.perf_counter()
print("Time to solve all of these puzzles was: %f seconds" % (end-start))