# -*- coding: utf-8 -*-

import sys

ONE_ROW_ELIMINATE = 40
TWO_ROWS_ELIMINATE = 100
THREE_ROWS_ELIMINATE = 300
FOUR_ROWS_ELIMINATE = 1200
ORIENTATIONS = {("I", 0, 4, 1): [(1, 0), (2, 0), (3, 0)],
                ("I", 1, 1, 4): [(0, -1), (0, -2), (0, -3)],
                ("O", 0, 2, 2): [(0, -1), (1, 0), (1, -1)],
                ("T", 0, 3, 2): [(1, 0), (1, -1), (2, 0)],
                ("T", 1, 2, 3): [(0, -1), (0, -2), (1, -1)],
                ("T", 2, 3, 2): [(1, 1), (1, 0), (2, 0)],
                ("T", 3, 2, 3): [(1, 1), (1, 0), (1, -1)],
                ("S", 0, 3, 2): [(1, 0), (1, -1), (2, -1)],
                ("S", 1, 2, 3): [(0, -1), (1, 1), (1, 0)],
                ("Z", 0, 3, 2): [(1, 1), (1, 0), (2, 1)],
                ("Z", 1, 2, 3): [(0, -1), (1, -1), (1, -2)],
                ("J", 0, 3, 2): [(0, -1), (1, 0), (2, 0)],
                ("J", 1, 2, 3): [(0, -1), (0, -2), (1, -2)],
                ("J", 2, 3, 2): [(1, 0), (2, 1), (2, 0)],
                ("J", 3, 2, 3): [(1, 0), (1, -1), (1, -2)],
                ("L", 0, 3, 2): [(1, 0), (2, 0), (2, -1)],
                ("L", 1, 2, 3): [(0, -1), (0, -2), (1, 0)],
                ("L", 2, 3, 2): [(0, -1), (1, -1), (2, -1)],
                ("L", 3, 2, 3): [(1, 2), (1, 1), (1, 0)]}

def index_to_coor(index):
    y = (index//10)
    x = index%10
    return (x,y)

def coor_to_index(x, y):
    return (10*(y))+x

def in_range(x, y):
    if x > -1 and x < 10 and y > -1 and y < 20:
        return True
    return False

def print_board(board):
    for b in range(0, 20*10, 10):
        print(board[b:b+10])
        
def max_col(heights, a, b):
    max_h = 0
    max_i = 0
    for i in range(a, b):
        h, hi = heights[i]
        if 20-h > max_h:
            max_h = 20-h
            max_i = i
    return max_h, max_i

def check_full_row(board, a, b):
    full_rows = []
    for i in range(a, b):
        if i > -1 and i < 20 and board[10*i:(10*i)+10].count("#") == 10:
            full_rows.append(i)
    return full_rows

def shift_one_down(board, y):
    board_new = "          "
    for row in range(0, y):
        board_new += board[row*10: (row*10)+10]
    board_new += board[(y*10)+10:]
    return board_new

def shift_down(board, rows):
    if len(rows) == 0:
        return board, 0
    blank = "          "
    board_new = blank*len(rows)
    board_new += board[0:rows[0]*10]
    for i in range(len(rows)-1):
        board_new += board[(rows[i]*10)+10:(rows[i+1]*10)]
    board_new += board[(rows[len(rows)-1]*10)+10:]
    return board_new, len(rows)

def find_col_height(board):
    col_height = []
    for c in range(0, 10):
        block = board[coor_to_index(c, 0)]
        count = 0
        while block != "#":
            count +=1
            block = board[coor_to_index(c, count)]
        col_height.append((count, coor_to_index(c, count)))
    return col_height

def get_orientations(p, n, l, h, loc):
    ox0, oy0 = ORIENTATIONS[(p,n,l,h)][0]
    ox1, oy1 = ORIENTATIONS[(p,n,l,h)][1]
    ox2, oy2 = ORIENTATIONS[(p,n,l,h)][2]
    if ox0 == loc:
        return ox0, oy0
    if ox1 == loc:
        return ox1, oy1
    return ox2, oy2

def add_blocks(board):
    col_heights = find_col_height(board)
    # print(col_heights)
    possible_boards = []
    for bp, bn, bl, bh in ORIENTATIONS:
        # print(bp, bn, bl, bh)
        for c in range(0, 10-bl+1):
            # input()
            # print("---")
            # print_board(board)
            max_h, max_i = max_col(col_heights, c, c+bl)
            h, index = col_heights[max_i]
            # print("h, index, max_i: ", h, index, max_i)
            if h < 1:
                possible_boards.append("GAME OVER\n")
                # print("game over")
                continue
            diff = max_i - c
            ox0, oy0 = ORIENTATIONS[(bp,bn,bl,bh)][0]
            ox1, oy1 = ORIENTATIONS[(bp,bn,bl,bh)][1]
            ox2, oy2 = ORIENTATIONS[(bp,bn,bl,bh)][2]
            x, y = index_to_coor(index-10)
            if diff > 0:
                dx, dy = get_orientations(bp, bn, bl, bh, diff)
                x = x-dx
                y = y-dy
            # print("x, y: ", x, y)
            board_new = list(board)
            addable = False
            while addable == False and in_range(x, y):
                if board[coor_to_index(x, y)] != "#" and in_range(x+ox0, y+oy0) and board[coor_to_index(x+ox0, y+oy0)] != "#" and in_range(x+ox1, y+oy1) and board[coor_to_index(x+ox1, y+oy1)] != "#" and in_range(x+ox2, y+oy2) and board[coor_to_index(x+ox2, y+oy2)] != "#":
                    addable = True
                    board_new[coor_to_index(x, y)] = "#"
                    board_new[coor_to_index(x+ox0, y+oy0)] = "#"
                    board_new[coor_to_index(x+ox1, y+oy1)] = "#"
                    board_new[coor_to_index(x+ox2, y+oy2)] = "#"
                else:
                    y -= 1
            # for ox, oy in ORIENTATIONS[(p,n,l)]:
            #     if not in_range(x+ox, y+oy):
            #         addable = False
            #         break
            #     if board[coor_to_index(x+ox, y+oy)] == "#":
            #         addable = False
            #         break
            #     board_new[coor_to_index(x+ox, y+oy)] = "#"
            if addable:
                board_new = "".join(board_new)
                # print_board(board_new)
                hi, ii = col_heights[c]
                # print(hi, ii)
                # print(y-bh, y+bh)
                full_rows = check_full_row(board_new, y-bh, y+bh)
                board_new, rows = shift_down(board_new, full_rows)
                # print_board(board_new)
                possible_boards.append(board_new+"\n")
            else:
                possible_boards.append("GAME OVER\n")
                # print("game over")
    return possible_boards

def write_output(l):
    file1 = open("tetrisout.txt", "w")
    file1.writelines(l)
    file1.close()
    

# test = "          #         #         #      #  #      #  #      #  #     ##  #     ##  #     ## ##     ## #####  ########  ######### ######### ######### ######### ########## #### # # # # ##### ###   ########"
# test = "                               #         #         #         #         #         #         #         #         #         #         #       ###  ######### ######### ######### ######### ########## #####"
# print_board(test)
# print(find_col_height(test))
# print(check_full_row(test, 19))
# print_board(shift_one_down(test, 19))
# boards = add_blocks(test)
# print(boards)
# write_output(boards)

given_board = sys.argv[1]
boards = add_blocks(given_board)
write_output(boards)

