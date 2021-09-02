# -*- coding: utf-8 -*-

def score(board, xm, om, xc, oc): # returns weight of board
    # mob = (len(xm) - len(om))*100
    # corner = 0
    # # corners
    # c = 1
    # if board[0] == "x":
    #     corner += c
    # if board[0] == "o":
    #     corner -= c
    # if board[7] == "x":
    #     corner += c
    # if board[7] == "o":
    #     corner -= c
    # if board[56] == "x":
    #     corner += c
    # if board[56] == "o":
    #     corner -= c
    # if board[63] == "x":
    #     corner += c
    # if board[63] == "o":
    #     corner -= c
    # corner = corner*100
    # edge = 0
    # # edges
    # e = 1
    # if board[2] == "x":
    #     edge += e
    # if board[3] == "x":
    #     edge += e
    # if board[4] == "x":
    #     edge += e
    # if board[5] == "x":
    #     edge += e
    # if board[2] == "o":
    #     edge -= e
    # if board[3] == "o":
    #     edge -= e
    # if board[4] == "o":
    #     edge -= e
    # if board[5] == "o":
    #     edge -= e
    # if board[58] == "x":
    #     edge += e
    # if board[59] == "x":
    #     edge += e
    # if board[60] == "x":
    #     edge += e
    # if board[61] == "x":
    #     edge += e
    # if board[58] == "o":
    #     edge -= e
    # if board[59] == "o":
    #     edge -= e
    # if board[60] == "o":
    #     edge -= e
    # if board[61] == "o":
    #     edge -= e
    # if board[16] == "x":
    #     edge += e
    # if board[24] == "x":
    #     edge += e
    # if board[32] == "x":
    #     edge += e
    # if board[40] == "x":
    #     edge += e
    # if board[16] == "o":
    #     edge -= e
    # if board[24] == "o":
    #     edge -= e
    # if board[32] == "o":
    #     edge -= e
    # if board[40] == "o":
    #     edge -= e
    # if board[23] == "x":
    #     edge += e
    # if board[31] == "x":
    #     edge += e
    # if board[39] == "x":
    #     edge += e
    # if board[47] == "x":
    #     edge += e
    # if board[23] == "o":
    #     edge -= e
    # if board[31] == "o":
    #     edge -= e
    # if board[39] == "o":
    #     edge -= e
    # if board[47] == "o":
    #     edge -= e
    # edge = edge *100
    # corneradj = 0
    # # corner-adjacent squares
    # ca = 1
    # if board[1] == "x" and board[0] != "x":
    #     corneradj -= ca
    # if board[8] == "x" and board[0] != "x":
    #     corneradj -= ca
    # if board[9] == "x" and board[0] != "x":
    #     corneradj -= ca
    # if board[1] == "o" and board[0] != "o":
    #     corneradj += ca
    # if board[8] == "o" and board[0] != "o":
    #     corneradj += ca
    # if board[9] == "o" and board[0] != "o":
    #     corneradj += ca
    # if board[6] == "x" and board[7] != "x":
    #     corneradj -= ca
    # if board[14] == "x" and board[7] != "x":
    #     corneradj -= ca
    # if board[15] == "x" and board[7] != "x":
    #     corneradj -= ca
    # if board[6] == "o" and board[7] != "o":
    #     corneradj += ca
    # if board[14] == "o" and board[7] != "o":
    #     corneradj += ca
    # if board[15] == "o" and board[7] != "o":
    #     corneradj += ca
    # if board[48] == "x" and board[56] != "x":
    #     corneradj -= ca
    # if board[49] == "x" and board[56] != "x":
    #     corneradj -= ca
    # if board[57] == "x" and board[56] != "x":
    #     corneradj -= ca
    # if board[48] == "o" and board[56] != "o":
    #     corneradj += ca
    # if board[49] == "o" and board[56] != "o":
    #     corneradj += ca
    # if board[57] == "o" and board[56] != "o":
    #     corneradj += ca
    # if board[54] == "x" and board[63] != "x":
    #     corneradj -= ca
    # if board[55] == "x" and board[63] != "x":
    #     corneradj -= ca
    # if board[62] == "x" and board[63] != "x":
    #     corneradj -= ca
    # if board[54] == "o" and board[63] != "o":
    #     corneradj += ca
    # if board[55] == "o" and board[63] != "o":
    #     corneradj += ca
    # if board[62] == "o" and board[63] != "o":
    #     corneradj += ca
    # corneradj = corneradj*100
    # score = 0.1*corneradj + 0.5*mob + 0.5*corner + 0.2*edge
    score = (len(xm) - len(om))*10         # mobility
    score += (xc-oc)
    # corners
    c = 250
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
    ca = 40
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
    e = 90
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

def score_later(board, xm, om, xc, oc):
    # mob = (len(xm) - len(om))*100
    # corner = 0
    # # corners
    # c = 1
    # if board[0] == "x":
    #     corner += c
    # if board[0] == "o":
    #     corner -= c
    # if board[7] == "x":
    #     corner += c
    # if board[7] == "o":
    #     corner -= c
    # if board[56] == "x":
    #     corner += c
    # if board[56] == "o":
    #     corner -= c
    # if board[63] == "x":
    #     corner += c
    # if board[63] == "o":
    #     corner -= c
    # corner = corner*100
    # edge = 0
    # # edges
    # e = 1
    # if board[2] == "x":
    #     edge += e
    # if board[3] == "x":
    #     edge += e
    # if board[4] == "x":
    #     edge += e
    # if board[5] == "x":
    #     edge += e
    # if board[2] == "o":
    #     edge -= e
    # if board[3] == "o":
    #     edge -= e
    # if board[4] == "o":
    #     edge -= e
    # if board[5] == "o":
    #     edge -= e
    # if board[58] == "x":
    #     edge += e
    # if board[59] == "x":
    #     edge += e
    # if board[60] == "x":
    #     edge += e
    # if board[61] == "x":
    #     edge += e
    # if board[58] == "o":
    #     edge -= e
    # if board[59] == "o":
    #     edge -= e
    # if board[60] == "o":
    #     edge -= e
    # if board[61] == "o":
    #     edge -= e
    # if board[16] == "x":
    #     edge += e
    # if board[24] == "x":
    #     edge += e
    # if board[32] == "x":
    #     edge += e
    # if board[40] == "x":
    #     edge += e
    # if board[16] == "o":
    #     edge -= e
    # if board[24] == "o":
    #     edge -= e
    # if board[32] == "o":
    #     edge -= e
    # if board[40] == "o":
    #     edge -= e
    # if board[23] == "x":
    #     edge += e
    # if board[31] == "x":
    #     edge += e
    # if board[39] == "x":
    #     edge += e
    # if board[47] == "x":
    #     edge += e
    # if board[23] == "o":
    #     edge -= e
    # if board[31] == "o":
    #     edge -= e
    # if board[39] == "o":
    #     edge -= e
    # if board[47] == "o":
    #     edge -= e
    # edge = edge *100
    # corneradj = 0
    # # corner-adjacent squares
    # ca = 1
    # if board[1] == "x" and board[0] != "x":
    #     corneradj -= ca
    # if board[8] == "x" and board[0] != "x":
    #     corneradj -= ca
    # if board[9] == "x" and board[0] != "x":
    #     corneradj -= ca
    # if board[1] == "o" and board[0] != "o":
    #     corneradj += ca
    # if board[8] == "o" and board[0] != "o":
    #     corneradj += ca
    # if board[9] == "o" and board[0] != "o":
    #     corneradj += ca
    # if board[6] == "x" and board[7] != "x":
    #     corneradj -= ca
    # if board[14] == "x" and board[7] != "x":
    #     corneradj -= ca
    # if board[15] == "x" and board[7] != "x":
    #     corneradj -= ca
    # if board[6] == "o" and board[7] != "o":
    #     corneradj += ca
    # if board[14] == "o" and board[7] != "o":
    #     corneradj += ca
    # if board[15] == "o" and board[7] != "o":
    #     corneradj += ca
    # if board[48] == "x" and board[56] != "x":
    #     corneradj -= ca
    # if board[49] == "x" and board[56] != "x":
    #     corneradj -= ca
    # if board[57] == "x" and board[56] != "x":
    #     corneradj -= ca
    # if board[48] == "o" and board[56] != "o":
    #     corneradj += ca
    # if board[49] == "o" and board[56] != "o":
    #     corneradj += ca
    # if board[57] == "o" and board[56] != "o":
    #     corneradj += ca
    # if board[54] == "x" and board[63] != "x":
    #     corneradj -= ca
    # if board[55] == "x" and board[63] != "x":
    #     corneradj -= ca
    # if board[62] == "x" and board[63] != "x":
    #     corneradj -= ca
    # if board[54] == "o" and board[63] != "o":
    #     corneradj += ca
    # if board[55] == "o" and board[63] != "o":
    #     corneradj += ca
    # if board[62] == "o" and board[63] != "o":
    #     corneradj += ca
    # corneradj = corneradj*100
    # taken = (xc-oc)*100
    # score = 0.1*corneradj + 0.4*mob + 0.4*corner + 0.15*edge + 0.5*taken
    score = (xc-oc)*4 
    score += ((len(xm) - len(om))*8)         # mobility
    # corners
    c = 250
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
    ca = 90
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
    e = 150
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
