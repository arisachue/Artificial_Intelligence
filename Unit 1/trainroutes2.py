# -*- coding: utf-8 -*-

import tkinter as tk
from math import pi , acos , sin , cos
import sys
from heapq import heappush, heappop, heapify

lines = [] #list of all the lines created
distances = dict()
ids = dict()
cities = dict()
lineEdges = dict()

def calcd(node1, node2):
   # y1 = lat1, x1 = long1
   # y2 = lat2, x2 = long2
   # all assumed to be in decimal degrees
   y1, x1 = node1
   y2, x2 = node2
   
   if y1 == y2 and x1 == x2:
       return 0

   R   = 3958.76 # miles = 6371 km
   y1 *= pi/180.0
   x1 *= pi/180.0
   y2 *= pi/180.0
   x2 *= pi/180.0

   # approximate great circle distance with law of cosines
   return acos( sin(y1)*sin(y2) + cos(y1)*cos(y2)*cos(x2-x1) ) * R

def build():
    with open("rrNodeCity.txt") as f:
        for line in f:
            l = line.split()
            city = " ".join(l[1:])
            cities[city] = l[0]
            
    with open("rrNodes.txt") as f:
        for line in f:
            l = line.split()
            ids[l[0]] = (float(l[1]), float(l[2]))
    
    with open("rrEdges.txt") as f:
        for line in f:
            l = line.split()
            dis = calcd(ids[l[0]], ids[l[1]])
            if l[0] in distances:
                distances[l[0]].add((l[1], dis))
            else:
                distances[l[0]] = {(l[1], dis)}
            if l[1] in distances:
                distances[l[1]].add((l[0], dis))
            else:
                distances[l[1]] = {(l[0], dis)}   


def extremes():
    latmi, latma = 800, 0
    longmi, longma = 0, -800
    for i in ids:
        lat, long = ids[i]
        if lat < latmi: latmi = lat
        if lat > latma: latma = lat
        if long < longmi: longmi = long
        if long > longma: longma = long
    return latmi, latma, longmi, longma
        

def coor_xy(lat, long):
    y = lat
    x = long
    return (8.5*x)+1200, 700-(8.5*y)

def create_edges(c):
    for idtag in distances:
        for dest in distances[idtag]:
            # print(idtag)
            lat1, long1 = ids[idtag]
            x1, y1 = coor_xy(lat1, long1)
            lat2, long2 = ids[dest[0]]
            x2, y2 = coor_xy(lat2, long2)
            # print("1: (%s, %s) 2: (%s, %s)" % (x1, y1, x2, y2))
            line = c.create_line([(x1, y1), (x2, y2)], tag="edges")
            lineEdges[(idtag, dest[0])] = line
    # lineEdges length = 50246

def make_edges(r, c):
    for e in lineEdges:
        # print(e)
        c.itemconfig(lineEdges[e], fill="black")
    r.update()

# Dijkstra's Algorithm 
def dijkstra(start_state, goal_state, r, c):
    count=0
    closed = set()
    start_node = (0, cities[start_state], [cities[start_state]])
    fringe = []
    heappush(fringe, start_node)
    while len(fringe) > 0:
        depth, idtag, parent = heappop(fringe)
        if cities[goal_state] == idtag:
            r.update()
            for x in range(0, len(parent)-1):
                j1 = parent[x]
                j2 = parent[x+1]
                c.itemconfig(lineEdges[(j1, j2)], fill="green")
            r.update()
            return depth
        if idtag not in closed:
            closed.add(idtag)
            for junction, dis in distances[idtag]:
                c.itemconfig(lineEdges[(idtag, junction)], fill="red")
                if junction not in closed:
                    temp = (depth+dis, junction, parent.copy())
                    temp[2].append(junction)
                    heappush(fringe, temp)
                    count+=1
                    if count%2000 == 0:
                        r.update()
    return None

def heuristic(start, goal):
    return calcd(ids[start], ids[goal])

# A* search
def a_star(start_state, goal_state, r, c):
    count=0
    closed = set()
    start_node = (heuristic(cities[start_state], cities[goal_state]), cities[start_state], 0, [cities[start_state]])
    fringe = []
    heappush(fringe, start_node)
    while len(fringe) > 0:
        heu, idtag, depth, parent = heappop(fringe)
        if cities[goal_state] == idtag:
            r.update()
            for x in range(0, len(parent)-1):
                j1 = parent[x]
                j2 = parent[x+1]
                c.itemconfig(lineEdges[(j1, j2)], fill="green")
            r.update()
            return depth
        if idtag not in closed:
            closed.add(idtag)
            for junction, dis in distances[idtag]:
                c.itemconfig(lineEdges[(idtag, junction)], fill="blue")
                if junction not in closed:
                    temp = (depth+dis+heuristic(junction, cities[goal_state]), junction, depth+dis, parent.copy())
                    temp[3].append(junction)
                    heappush(fringe, temp)
                    count+=1
                    if count%2000 == 0:
                        r.update()
    r.update()
    return None

city1 = sys.argv[1]
city2 = sys.argv[2]

build()
# print(extremes())
# (14.68673, 60.84682, -130.35722, -60.02403)

# =============================================================================
# Dijkstra's Algorithm
# =============================================================================
root = tk.Tk() #creates the frame

canvas = tk.Canvas(root, height=800, width=800, bg='white') #creates a canvas widget, which can be used for drawing lines and shapes
create_edges(canvas)
canvas.pack(expand=True) #packing widgets places them on the board

make_edges(root, canvas)

moves = dijkstra(city1, city2, root, canvas)
# print(moves)

root.mainloop()

# =============================================================================
# A*star search
# =============================================================================
root = tk.Tk() #creates the frame

canvas = tk.Canvas(root, height=800, width=800, bg='white') #creates a canvas widget, which can be used for drawing lines and shapes
create_edges(canvas)
canvas.pack(expand=True) #packing widgets places them on the board

make_edges(root, canvas)

moves = a_star(city1, city2, root, canvas)
# print(moves)

root.mainloop()
