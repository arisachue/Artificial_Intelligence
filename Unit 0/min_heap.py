# -*- coding: utf-8 -*-

import sys

s = sys.argv[1:]
# s = s.split()

# swaps items in list l of index a and b
def swap(l, a, b):
    temp = l[a]
    l[a] = l[b]
    l[b] = temp
    
# adds a new item into heap_list
def heappush(heap_list, new_item):
    heap_list.append(new_item)                  # adds to the end of list
    index = len(heap_list)-1                    # index of the new item
    while((index-1)/2 >= 0):
        parent = int((index-1)/2)               # finds the parent to check which is smaller
        if(new_item < heap_list[parent]):
            swap(heap_list, parent, index)      # if the new item is smaller than parent, swap, then repeat with while loop
            index = parent
        else:
            return                              # end the while loop once parent value is bigger

# sorts item at index to correct place
def sort(heap_list, index):
    left = int(2*index + 1)
    right = int(2*index + 2)
    if left > len(heap_list)-1:                 # reached end of list
        return
    else:
        node_value = heap_list[index]           # current node
        left_value = heap_list[left]            # left child node
        min_index = left                        # temp value to check if left or right is smaller
        if(right < len(heap_list) and heap_list[right] < left_value): # find the smaller node of the two children
            min_index = right
        if node_value > heap_list[min_index]:
            swap(heap_list, index, min_index)   # swap and repeat
            sort(heap_list, min_index)          # go down the tree and see next children
        
def heapify(heap_list):
    last_parent = int(len(heap_list)/2) - 1     # finds the last parent from the last item in list using parent formula
    for x in range(last_parent, -1, -1):        # go backwards to get children heapified
        sort(heap_list, x)

def heappop(heap_list):
    swap(heap_list, 0, len(heap_list)-1)    # put the root to the end for easy removal
    min = heap_list.pop()                   # remove last item (was previous root and min value)
    sort(heap_list, 0)                      # sort the list since new root is probably not in correct place
    return min    

# =============================================================================
# test protocol
# =============================================================================
integer_list = []
x = 0
while str(s[x]) != "A" and str(s[x]) != "R":
    value = int(s[x])
    integer_list.append(value)
    x+=1   
    
print("Initial list: %s" % str(integer_list))
heapify(integer_list)
print("Heapified list: %s" % str(integer_list))
while x < len(s):
    if s[x] == "A":
        num = int(s[x+1])
        heappush(integer_list, num)
        print("Added %s to heap: %s" % (str(num),str(integer_list)))
        x=x+2
    elif s[x] == "R":
        min = heappop(integer_list)
        print("Popped %s from list: %s" % (str(min), str(integer_list)))
        x+=1

    