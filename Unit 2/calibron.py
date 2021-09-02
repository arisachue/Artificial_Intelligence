# -*- coding: utf-8 -*-

import sys

# You are given code to read in a puzzle from the command line.  The puzzle should be a single input argument IN QUOTES.
# A puzzle looks like this: "56 56 28x14 32x11 32x10 21x18 21x18 21x14 21x14 17x14 28x7 28x6 10x7 14x4"
# The code below breaks it down:
puzzle = sys.argv[1].split()
puzzle_height = int(puzzle[0])
puzzle_width = int(puzzle[1])
rectangles = [(int(temp.split("x")[0]), int(temp.split("x")[1])) for temp in puzzle[2:]]
# puzzle_height is the height (number of rows) of the puzzle
# puzzle_width is the width (number of columns) of the puzzle
# rectangles is a list of tuples of rectangle dimensions
def get_key(dic, val):
    for key, value in dic.items():
         if val == value:
             dic[key] = 0
             return key

def sort():
    global rectangles
    temp = dict()
    areas = []
    newsorted = []
    for i in range(len(rectangles)):
        temp[i] = rectangles[i][0]*rectangles[i][1]
        areas.append(temp[i])
    areas.sort(reverse=True)
    for a in areas:
        index = get_key(temp, a)
        newsorted.append(rectangles[index])
    rectangles = newsorted
    
board = []
# for i in range(len(rectangles)):
#     board[i] = (0, 0, rectangles[i][0], rectangles[i][1])

def insert(board, height, width):
    if len(board) == 0:
        board.append(0,0, height, width)
        return board;
    x, y, h, w = board.pop()
    if x+w+width < puzzle_width:
        board.append(x, y, h, w)
        board.append(x+w, y, height, width)
        return board
    return None

def get_next_unassigned_var(board):
    if len(board) == 0:
        return 0, 0, rectangles[0][0], rectangles[0][1]
    x, y, h, w = board.pop()
    board.append(x, y, h, w)
    return x, y, h, w

def get_sorted_values(board, x, y, height, width):
    values = []
    for h, w in rectangles:
        if x+width+w < puzzle_width:
            values.append((h,w))
    return values

def assign(board, x, y, height, width):
    new_b = []
    for b in board:
        new_b.append(b)
    new_b.append(x, y, height, width)
    
def remove(rect, h, w):
    new_rect = []
    for rh, rw in rect:
        if rh != h and rw != w:
            new_rect.append((rh, rw))
    return new_rect

def solve(brd, rect):
    if len(rect) == 0:
        return brd
    x, y, height, width = get_next_unassigned_var(brd)
    for h, w in get_sorted_values(brd, x, y, height, width):
        new_brd = assign(brd, x, y, h, w)
        if new_brd is not None:
            rect = remove(rect, x, y)
            result = solve(new_brd, rect)
            if result is not None:
                return result
    return None
        
        
    

# INSTRUCTIONS:
#
# First check to see if the sum of the areas of the little rectangles equals the big area.
area = 0
for h, w in rectangles:
    area += (h*w)
if area != (puzzle_height*puzzle_width):
    print("Containing rectangle incorrectly sized.")
else:
    sort()
    print(solve(board, rectangles))
    

    
# If not, output precisely this - "Containing rectangle incorrectly sized."
#
# Then try to solve the puzzle.
# If the puzzle is unsolvable, output precisely this - "No solution."
#
# If the puzzle is solved, output ONE line for EACH rectangle in the following format:
# row column height width
# where "row" and "column" refer to the rectangle's top left corner.
#
# For example, a line that says:
# 3 4 2 1
# would be a rectangle whose top left corner is in row 3, column 4, with a height of 2 and a width of 1.
# Note that this is NOT the same as 3 4 1 2 would be.  The orientation of the rectangle is important.
#
# Your code should output exactly one line (one print statement) per rectangle and NOTHING ELSE.
# If you don't follow this convention exactly, my grader will fail.