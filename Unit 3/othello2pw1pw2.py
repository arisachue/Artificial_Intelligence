# -*- coding: utf-8 -*-

def index_to_coor(index):
    y = 7-(index//8)
    x = index%8
    return (x,y)

def coor_to_index(x, y):
    return 8*(7-y)+x

def print_board(board):
    for col in range(0, 64, 8):
        print(board[col:col+8])
 
def in_range(x, y):
    if x > -1 and x < 8 and y > -1 and y < 8:
        return True
    return False

def possibleMoves(board, token):
    spaces = []
    opp = "x"
    if token == "x":
        opp = "o"
    for i in range(len(board)):
        if board[i] != ".":
            continue
        x, y = index_to_coor(i)
        if x > 1 and board[coor_to_index(x-1, y)] == opp: # left
            tempx = x
            while tempx > 0 and board[coor_to_index(tempx-1, y)] == opp: # keep going left
                tempx -= 1
            new_index = coor_to_index(tempx-1, y)
            if in_range(tempx-1, y) and board[new_index] == token:
                spaces.append(i)
                continue
        if x < 6 and board[coor_to_index(x+1, y)] == opp: # right
            tempx = x
            while tempx < 7 and board[coor_to_index(tempx+1, y)] == opp: # keep going right
                tempx += 1
            new_index = coor_to_index(tempx+1, y)
            if in_range(tempx+1, y) and board[new_index] == token:
                spaces.append(i)
                continue
        if y > 1 and board[coor_to_index(x, y-1)] == opp: # down
            tempy = y
            while tempy > 0 and board[coor_to_index(x, tempy-1)] == opp: # keep going down
                tempy -= 1
            new_index = coor_to_index(x, tempy-1)
            if in_range(x, tempy-1) and board[new_index] == token:
                spaces.append(i)
                continue
        if y < 6 and board[coor_to_index(x, y+1)] == opp: # up
            tempy = y
            while tempy < 7 and board[coor_to_index(x, tempy+1)] == opp: # keep going up
                tempy += 1
            new_index = coor_to_index(x, tempy+1)
            if in_range(x, tempy+1) and board[new_index] == token:
                spaces.append(i)
                continue
        if x > 1 and y > 1 and board[coor_to_index(x-1, y-1)] == opp: # diagonal left down
            tempx = x    
            tempy = y
            while tempx > 0 and tempy > 0 and board[coor_to_index(tempx-1, tempy-1)] == opp: # keep going left+down
                tempx -= 1
                tempy -= 1
            new_index = coor_to_index(tempx-1, tempy-1)
            if in_range(tempx-1, tempy-1) and board[new_index] == token:
                spaces.append(i)
                continue
        if x > 1 and y < 6 and board[coor_to_index(x-1, y+1)] == opp: # diagonal left up
            tempx = x    
            tempy = y
            while tempx > 0 and tempy < 7 and board[coor_to_index(tempx-1, tempy+1)] == opp: # keep going left+up
                tempx -= 1
                tempy += 1
            new_index = coor_to_index(tempx-1, tempy+1)
            if in_range(tempx-1, tempy+1) and board[new_index] == token:
                spaces.append(i)
                continue
        if x < 6 and y > 1 and board[coor_to_index(x+1, y-1)] == opp: # diagonal right down
            tempx = x    
            tempy = y
            while tempx < 7 and tempy > 0 and board[coor_to_index(tempx+1, tempy-1)] == opp: # keep going right+down
                tempx += 1
                tempy -= 1
            new_index = coor_to_index(tempx+1, tempy-1)
            if in_range(tempx+1, tempy-1) and board[new_index] == token:
                spaces.append(i)
                continue
        if x < 6 and y < 6 and board[coor_to_index(x+1, y+1)] == opp: # diagonal right up
            tempx = x    
            tempy = y
            while tempx < 7 and tempy < 7 and board[coor_to_index(tempx+1, tempy+1)] == opp: # keep going right+up
                tempx += 1
                tempy += 1
            new_index = coor_to_index(tempx+1, tempy+1)
            if in_range(tempx+1, tempy+1) and board[new_index] == token:
                spaces.append(i)
                continue
    return spaces

def move(board, token, position):
    board = list(board)
    board[position] = token
    opp = "x"
    if token == "x":
        opp = "o"
    x, y = index_to_coor(position)
    if x > 1 and board[coor_to_index(x-1, y)] == opp:
        tempx = x
        while tempx > 0 and board[coor_to_index(tempx-1, y)] == opp: # keep going left
            tempx -= 1
        new_index = coor_to_index(tempx-1, y)
        if in_range(tempx-1, y) and board[new_index] == token:
            for i in range(new_index+1, position):
                board[i] = token
    if x < 6 and board[coor_to_index(x+1, y)] == opp: # right
        tempx = x
        while tempx < 7 and board[coor_to_index(tempx+1, y)] == opp: # keep going right
            tempx += 1
        new_index = coor_to_index(tempx+1, y)
        if in_range(tempx+1, y) and board[new_index] == token:
            for i in range(position+1, new_index):
                board[i] = token
    if y > 1 and board[coor_to_index(x, y-1)] == opp: # down
        tempy = y
        while tempy > 0 and board[coor_to_index(x, tempy-1)] == opp: # keep going down
            tempy -= 1
        new_index = coor_to_index(x, tempy-1)
        if in_range(x, tempy-1) and board[new_index] == token:
            for i in range(position, new_index, 8):
                board[i] = token
    if y < 6 and board[coor_to_index(x, y+1)] == opp: # up
        tempy = y
        while tempy < 7 and board[coor_to_index(x, tempy+1)] == opp: # keep going up
            tempy += 1
        new_index = coor_to_index(x, tempy+1)
        if in_range(x, tempy+1) and board[new_index] == token:
            for i in range(new_index, position, 8):
                board[i] = token
    if x > 1 and y > 1 and board[coor_to_index(x-1, y-1)] == opp: # diagonal left down
        tempx = x    
        tempy = y
        while tempx > 0 and tempy > 0 and board[coor_to_index(tempx-1, tempy-1)] == opp: # keep going left+down
            tempx -= 1
            tempy -= 1
        new_index = coor_to_index(tempx-1, tempy-1)
        if in_range(tempx-1, tempy-1) and board[new_index] == token:
            for i in range(0, abs(x-(tempx-1))):
                newx = (tempx-1) + i
                newy = (tempy-1) + i
                board[coor_to_index(newx, newy)] = token
    if x > 1 and y < 6 and board[coor_to_index(x-1, y+1)] == opp: # diagonal left up
        tempx = x    
        tempy = y
        while tempx > 0 and tempy < 7 and board[coor_to_index(tempx-1, tempy+1)] == opp: # keep going left+up
            tempx -= 1
            tempy += 1
        new_index = coor_to_index(tempx-1, tempy+1)
        if in_range(tempx-1, tempy+1) and board[new_index] == token:
            for i in range(0, abs(x-(tempx-1))):
                newx = (tempx-1) + i
                newy = (tempy+1) - i
                board[coor_to_index(newx, newy)] = token
    if x < 6 and y > 1 and board[coor_to_index(x+1, y-1)] == opp: # diagonal right down
        tempx = x    
        tempy = y
        while tempx < 7 and tempy > 0 and board[coor_to_index(tempx+1, tempy-1)] == opp: # keep going right+down
            tempx += 1
            tempy -= 1
        new_index = coor_to_index(tempx+1, tempy-1)
        if in_range(tempx+1, tempy-1) and board[new_index] == token:
            for i in range(0, abs((tempx+1)-x)):
                newx = (tempx+1) - i
                newy = (tempy-1) + i
                board[coor_to_index(newx, newy)] = token
    if x < 6 and y < 6 and board[coor_to_index(x+1, y+1)] == opp: # diagonal right up
        tempx = x    
        tempy = y
        while tempx < 7 and tempy < 7 and board[coor_to_index(tempx+1, tempy+1)] == opp: # keep going right+up
            tempx += 1
            tempy += 1
        new_index = coor_to_index(tempx+1, tempy+1)
        if in_range(tempx+1, tempy+1) and board[new_index] == token:
            for i in range(0, abs((tempx+1)-x)):
                newx = (tempx+1) - i
                newy = (tempy+1) - i
                board[coor_to_index(newx, newy)] = token
    return "".join(board)

def game_over(board, xm, om):
    if "." not in board:
        return True
    if len(xm) == 0 or len(om) == 0:
        return True
    return False

def score(board, xm, om): # returns weight of board
    score = (len(xm) - len(om))*10         # mobility
    # corners
    c = 70
    if board[0] == "x":
        score += c
    if board[0] == "o":
        score -= c
    if board[7] == "x":
        score += c
    if board[7] == "o":
        score -= c
    if board[56] == "x":
        score += c
    if board[56] == "o":
        score -= c
    if board[63] == "x":
        score += c
    if board[63] == "o":
        score -= c
    # corner-adjacent squares
    ca = 20
    if board[1] == "x" and board[0] != "x":
        score -= ca
    if board[8] == "x" and board[0] != "x":
        score -= ca
    if board[9] == "x" and board[0] != "x":
        score -= ca
    if board[1] == "o" and board[0] != "o":
        score += ca
    if board[8] == "o" and board[0] != "o":
        score += ca
    if board[9] == "o" and board[0] != "o":
        score += ca
    if board[6] == "x" and board[7] != "x":
        score -= ca
    if board[14] == "x" and board[7] != "x":
        score -= ca
    if board[15] == "x" and board[7] != "x":
        score -= ca
    if board[6] == "o" and board[7] != "o":
        score += ca
    if board[14] == "o" and board[7] != "o":
        score += ca
    if board[15] == "o" and board[7] != "o":
        score += ca
    if board[48] == "x" and board[56] != "x":
        score -= ca
    if board[49] == "x" and board[56] != "x":
        score -= ca
    if board[57] == "x" and board[56] != "x":
        score -= ca
    if board[48] == "o" and board[56] != "o":
        score += ca
    if board[49] == "o" and board[56] != "o":
        score += ca
    if board[57] == "o" and board[56] != "o":
        score += ca
    if board[54] == "x" and board[63] != "x":
        score -= ca
    if board[55] == "x" and board[63] != "x":
        score -= ca
    if board[62] == "x" and board[63] != "x":
        score -= ca
    if board[54] == "o" and board[63] != "o":
        score += ca
    if board[55] == "o" and board[63] != "o":
        score += ca
    if board[62] == "o" and board[63] != "o":
        score += ca
    # edges
    e = 40
    if board[2] == "x":
        score += e
    if board[3] == "x":
        score += e
    if board[4] == "x":
        score += e
    if board[5] == "x":
        score += e
    if board[2] == "o":
        score -= e
    if board[3] == "o":
        score -= e
    if board[4] == "o":
        score -= e
    if board[5] == "o":
        score -= e
    if board[58] == "x":
        score += e
    if board[59] == "x":
        score += e
    if board[60] == "x":
        score += e
    if board[61] == "x":
        score += e
    if board[58] == "o":
        score -= e
    if board[59] == "o":
        score -= e
    if board[60] == "o":
        score -= e
    if board[61] == "o":
        score -= e
    if board[16] == "x":
        score += e
    if board[24] == "x":
        score += e
    if board[32] == "x":
        score += e
    if board[40] == "x":
        score += e
    if board[16] == "o":
        score -= e
    if board[24] == "o":
        score -= e
    if board[32] == "o":
        score -= e
    if board[40] == "o":
        score -= e
    if board[23] == "x":
        score += e
    if board[31] == "x":
        score += e
    if board[39] == "x":
        score += e
    if board[47] == "x":
        score += e
    if board[23] == "o":
        score -= e
    if board[31] == "o":
        score -= e
    if board[39] == "o":
        score -= e
    if board[47] == "o":
        score -= e
    return score

def next_board(board, t, xmoves):
    boards = []
    for xm in xmoves:
        temp = move(board, t, xm)
        boards.append((temp, xm))
    return boards

def max_step(board, depth, alpha, beta): # return max weight of future outcome
    xMoves = possibleMoves(board, "x")
    oMoves = possibleMoves(board, "o")
    if depth == 0:
        return score(board, xMoves, oMoves)
    if game_over(board, xMoves, oMoves):
        if len(oMoves) == 0:
            return 100000
        if len(xMoves) == 0:
            return -100000
        return (board.count("x") - board.count("o"))*1000
    results = []
    for next_b, m in next_board(board, "x", xMoves):
        ms = min_step(next_b, depth-1, alpha, beta)
        results.append(ms)
        if ms > alpha: 
            alpha = ms
        if alpha >= beta:
            break;
    return max(results)

def min_step(board, depth, alpha, beta): # return min weight of future outcome
    xMoves = possibleMoves(board, "x")
    oMoves = possibleMoves(board, "o")    
    if depth == 0:
        return score(board, xMoves, oMoves)
    if game_over(board, xMoves, oMoves):
        if len(oMoves) == 0:
            return 100000
        if len(xMoves) == 0:
            return -100000
        return (board.count("x") - board.count("o"))*1000
    results = []
    for next_b, m in next_board(board, "o", oMoves):
        ms = max_step(next_b, depth-1, alpha, beta)
        results.append(ms)
        if ms < beta: 
            beta = ms
        if alpha >= beta:
            break;
    return min(results)

def max_move(board, depth, alpha, beta): # return max move location, play X
    values = []
    xMoves = possibleMoves(board, "x") 
    for next_b, m in next_board(board, "x", xMoves):
        res = min_step(next_b, depth-1, alpha, beta)
        values.append((m, res))
        if res > alpha: 
            alpha = res
        if alpha >= beta:
            break;
    maxm, maxv = values[0]
    for move, val in values:
        if val > maxv: 
            maxv = val
            maxm = move
    return maxm

def min_move(board, depth, alpha, beta): # return min move location, play O
    values = []
    oMoves = possibleMoves(board, "o")
    for next_b, m in next_board(board, "o", oMoves):
        res = max_step(next_b, depth-1, alpha, beta)
        values.append((m, res))
        if res < beta: 
            beta = res
        if alpha >= beta:
            break;
    minm, minv = values[0]
    for move, val in values:
        if val < minv: 
            minv = val
            minm = move
    return minm

def find_next_move(board, player, depth):
    if player == "x":
        return max_move(board, depth, float('-inf'), float('inf'))
    return min_move(board, depth, float('-inf'), float('inf'))

class Strategy():

    logging = False  # Optional

    def best_strategy(self, board, player, best_move, still_running):

        depth = 1

        for count in range(15):  # 15 is arbitrary; a depth that your code won't reach, but infinite loops crash the grader

            best_move.value = find_next_move(board, player, depth)
            
            depth += 1