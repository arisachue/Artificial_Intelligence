# -*- coding: utf-8 -*-

from math import pi , acos , sin , cos
from heapq import heappush, heappop, heapify
import sys
import time

distances = dict()
ids = dict()
cities = dict()

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

# Dijkstra's Algorithm 
def dijkstra(start_state, goal_state):
    closed = set()
    start_node = (0, cities[start_state])
    fringe = []
    heappush(fringe, start_node)
    while len(fringe) > 0:
        depth, idtag = heappop(fringe)
        if cities[goal_state] == idtag:
            return depth
        if idtag not in closed:
            closed.add(idtag)
            for junction, dis in distances[idtag]:
                if junction not in closed:
                    temp = (depth+dis, junction)
                    heappush(fringe, temp)
    return None

def heuristic(start, goal):
    return calcd(ids[start], ids[goal])

# A* search
def a_star(start_state, goal_state):
    closed = set()
    start_node = (heuristic(cities[start_state], cities[goal_state]), cities[start_state], 0)
    fringe = []
    heappush(fringe, start_node)
    while len(fringe) > 0:
        heu, idtag, depth = heappop(fringe)
        if cities[goal_state] == idtag:
            return depth
        if idtag not in closed:
            closed.add(idtag)
            for junction, dis in distances[idtag]:
                if junction not in closed:
                    temp = (depth+dis+heuristic(junction, cities[goal_state]), junction, depth+dis)
                    heappush(fringe, temp)
    return None

city1 = sys.argv[1]
city2 = sys.argv[2]

start = time.perf_counter()
build()
end = time.perf_counter()
print("Time to create data structure: %s" % str(end-start))
start = time.perf_counter()
dis = dijkstra(city1, city2)
end = time.perf_counter()
print("%s to %s with Dijkstra: %s in %s seconds." % (city1, city2, dis, (end-start)))
start = time.perf_counter()
dis = a_star(city1, city2)
end = time.perf_counter()
print("%s to %s with A*: %s in %s seconds." % (city1, city2, dis, (end-start)))

        