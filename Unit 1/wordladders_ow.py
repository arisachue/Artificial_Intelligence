# -*- coding: utf-8 -*-

from collections import deque
import time
import sys

alpha=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
dic=set()
dic_children=dict()
max_sub=0
max_sub_key=""
sub=set()
max_clump=[]

def exist(word):
    return True if word in dic else False

# returns all the possible moves
def get_children(word):
    global dic_children
    return dic_children[word]
    # l = []
    # for i in range(len(word)):
    #     for a in alpha:
    #         st = word[:i]+a
    #         if i < (len(word)-1):
    #             st += word[i+1:]
    #         if exist(st):
    #             l.append(st)
    #         st = word[:i]+a+word[i:]
    #         if exist(st):
    #             l.append(st)
    #     st = word[:i]
    #     if i < (len(word)-1):
    #             st += word[i+1:]
    #     if exist(st):
    #         l.append(st)
    # return l

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


def create_dict():
    global dic, alpha, dic_children
    for w in dic:
        l = set()
        for i in range(len(w)):
            for a in alpha:
                st = w[:i]+a
                if i < (len(w)-1):
                    st += w[i+1:]
                if exist(st) and st != w:
                    l.add(st)
                st = w[:i]+a+w[i:]
                if exist(st):
                    l.add(st)
            st = w[:i]
            if i < (len(w)-1):
                    st += w[i+1:]
            if exist(st):
                l.add(st)
        for a in alpha:
            st = w + a
            if exist(st):
                l.add(st)
        dic_children[w] = l
        
def singleton():
    global dic_children
    count=0
    for w in dic_children:
        if len(dic_children[w])==0:
            count+=1
    return count

def large_sub():
    global dic, dic_children, max_sub, max_sub_key, max_clump
    looked=set()
    count=0
    for w in dic:
        if w not in looked:
            temp = reachable_loc(w)
            count+=1
            if len(temp) > max_sub:
                max_sub = len(temp) +1
                max_sub_key = w
                max_clump = temp
            for x in temp:
                looked.add(x)
    return max_sub, max_sub_key, count

def clumps():
    global sub, dic
    looked=set()
    count=0
    for d in dic:
        if d not in sub:
            count+=1
            temp = reachable_loc(d)
            for x in temp:
                sub.add(x)
    return count

def long_path_old():
    path_max = 0
    sol_max = ""
    last_max = ""
    st = reachable_loc(max_sub_key)
    # looked=set()
    for x in st:
        # if x not in looked:
        reach = reachable_loc(x)
        # for r in reach:
        #     looked.add(r)
        last = reach.pop()
        path, sol = shortest_path(x, last)
        if path > path_max:
            path_max = path
            sol_max = sol
            last_max = last
    return path_max, sol_max, last_max

def long_path():
    global max_clump, max_sub_key
    path_max = 0
    sol_max = ""
    last_max = ""
    
    last = max_clump.pop()
    path, sol = shortest_path(max_sub_key, last)
    while(path != path_max):
        if path > path_max:
            path_max = path
            sol_max = sol
            last_max = last
        reach = reachable_loc(last)
        next_last = reach.pop()
        path, sol = shortest_path(last, next_last)
    return path_max, sol_max, last_max          
      
dictionary = sys.argv[1]
words = sys.argv[2] 
start = time.perf_counter()  

# =============================================================================
# RUN CODE
# =============================================================================
   
with open(dictionary) as f:
    for line in f:
        dic.add(line.strip())
create_dict()

puzzle=dict()
with open(words) as f:
    for line in f:
        temp = line.strip().split()
        puzzle[temp[0]]=temp[1]

end = time.perf_counter()
print("Time to create the data structure was: %f seconds" % (end-start))   
print("There are %d words in this dict." % len(dic))
    
start = time.perf_counter()
count=0
for p in puzzle:
    # print("Line: %d" % count)
    # count+=1
    path, sol = shortest_path(p, puzzle[p])
    if path>0:
        print("Length of solution: %d" % path)
        print("\n".join(sol[::-1]))
    else:  
        print("No solution!")
    print()
end = time.perf_counter()
print("Time to solve all of these puzzles was: %f seconds" % (end-start))
print()
start = time.perf_counter()
sing = singleton()
print("1) There are %s singletons." % (sing))
mx, mxk, cnt = large_sub()
print("2) The biggest subcomponent has %s words." % (mx))
# cnt = clumps()
print("3) There are %s 'clumps' (subgraphs with at least two words)" % (cnt-sing))
end = time.perf_counter()
print("Questions 1-3 answered in %s seconds." % (end-start))
print()
start = time.perf_counter()
path, sol, last = long_path()
end = time.perf_counter()
print("4) The longest path is: [['%s', '%s'], %s], found in %s seconds." % (last, mxk, path, end-start))
print("The solution to this puzzle is:")
print("Length of solution: %s" % (path))
print("\n".join(sol[::-1]))