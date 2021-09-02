# -*- coding: utf-8 -*-

import sys

s = sys.argv[1]         # takes in text file with words
ml = int(sys.argv[2])   # minimum length of words
words_list = set()      # all the possible words
game = ""               # starting game
dic_children = dict()   # key = the "stems" of words (ex: w, wo, wor for word); values = a valid move with an extra letter

if len(sys.argv) > 3:
    game = sys.argv[3].upper()  # if game already started

with open(s) as f:
    for line in f:
        line = line.strip().upper()
        if len(line) >= ml and line.isalpha() and line[:len(game)] == game: # only takes words longer, alphabets, and disgards any words that don't share starting letters as current game
            words_list.add(line)


def create_dict():
    global words_list, dic_children
    for w in words_list:
        for i in range(len(w)):     
            temp = w[:i]                            # stemming!
            if temp not in words_list:              # so "the" won't be added for "them"
                if temp not in dic_children:        # if key doesn't exist, create new set
                    dic_children[temp] = set()
                    dic_children[temp].add(w[:i+1]) # adds with extra letter from a valid word from words_list
                else:
                    dic_children[temp].add(w[:i+1])
            
def next_word(word):
    moves = []
    if word in dic_children:
        future_words = dic_children[word]           
        for w in future_words:
            moves.append((w, w[len(word)]))         # tuple (next increased game word, valid next letter)
    return moves    

def max_step(word, alpha, beta): # return max weight of future outcome
    if word in words_list:          # means minstep returned a real word -> minstep loses
        return 1
    results = []
    for next_w, m in next_word(word):
        ms = min_step(next_w, alpha, beta)
        results.append(ms)
        if ms > alpha:              # alpha beta pruning
            alpha = ms
        if alpha >= beta:
            break;
    return max(results)

def middle_step(word, alpha, beta):
    if word in words_list:          # means maxstep returned a real word -> maxstep loses
        return 0
    results = []
    for next_w, m in next_word(word):
        ms = max_step(next_w, alpha, beta)
        results.append(ms)
        if ms < beta:               # alpha beta pruning
            beta = ms
        if alpha >= beta:
            break;
    return min(results)

def min_step(word, alpha, beta): # return max weight of future outcome
    if word in words_list:          # means maxstep returned a real word -> maxstep loses
        return -1
    results = []
    for next_w, m in next_word(word):
        ms = middle_step(next_w, alpha, beta)
        results.append(ms)
        if ms < beta:               # alpha beta pruning
            beta = ms
        if alpha >= beta:
            break;
    return min(results)

def max_move(word, alpha, beta): # return all winning letters
    values = []
    for next_w, m in next_word(word):
        res = min_step(next_w, alpha, beta)
        values.append((m, res))
    possible_wins = []
    for move, val in values:
        if val > -1:                    # if winning letters
            possible_wins.append(move)
    possible_wins.sort()
    return possible_wins   
        
# =============================================================================
# RUN CODE
# =============================================================================
create_dict()
wins = max_move(game, float('-inf'), float('inf'))      # only need to call maxmove to find next step
if len(wins) == 0:                                      # winning letters just don't exist
    print("Next player will lose!")
else:
    print("Next player can guarantee victory by playing any of these letters: %s" % wins)