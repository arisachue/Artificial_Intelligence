# -*- coding: utf-8 -*-

import time
import random

def test_solution(state):
    for var in range(len(state)):
        left = state[var]
        middle = state[var]
        right = state[var]
        for compare in range(var + 1, len(state)):
            left -= 1
            right += 1
            if state[compare] == middle:
                print(var, "middle", compare)
                return False
            if left >= 0 and state[compare] == left:
                print(var, "left", compare)
                return False
            if right < len(state) and state[compare] == right:
                print(var, "right", compare)
                return False
    return True

def goal_test(state):
    if "x" in state:
        return False
    return True

def get_next_unassigned_var(state):
    # start from center
    for r in range(int(len(state)/2)-1, -1, -1):
        if state[r] == "x":
            return r
        if state[len(state)-r-1] == "x":
            return len(state)-r-1

def get_sorted_values(state, var):
    cant = set()
    diff=0
    add=0
    for i in range(len(state)):
        if state[i] != "x":
            cant.add(int(state[i]))
            diff = i - int(state[i])
            cant.add(var-diff)
            add = i + int(state[i])
            cant.add(add-var)
    values= []
    # starting from the edges
    for i in range(int(len(state)/2)):
        if i not in cant:
            values.append(i)
        if (len(state)-i-1) not in cant:
            values.append(len(state)-i-1)
    return values

def csp_backtracking(state):
    if goal_test(state): return state
    var = get_next_unassigned_var(state)
    for val in get_sorted_values(state, var):
        new_state = [ r for r in state]
        new_state[var] = val
        result = csp_backtracking(new_state)
        if result is not None:
            return result
    return None

def generate_empty(size):
    state = []
    for i in range(size):
        state.append("x")
    return state

def generate(size):
    state = []
    for r in range(int(size/2)):
        state.append(r*2)
    for r in range(int(size/2)):
        state.append(r*2)
    return state

def total_conflicts(state):
    count = 0
    for i in range(len(state)-1):
        for n in range(i+1, len(state)):
            if state[i] == state[n] or (i+state[i]) == (n+state[n]) or (i-state[i]) == (n-state[n]): 
                count+=1
    return count

def rowconflicts(state, var):
    count = 0
    for i in range(len(state)):
        if state[i] == state[var] or (i+state[i]) == (var+state[var]) or (i-state[i]) == (var-state[var]):
            count+=1
    return count-1

def colconflicts(state, var):
    tempstate = [ r for r in state]
    min_con = rowconflicts(state, var)
    min_col = state[var]
    for col in range(len(state)):
        tempstate[var] = col
        con = rowconflicts(tempstate, var)
        if (con < min_con): 
                min_con = con
                min_col = col
        if( con == min_con):
            k = random.randint(0,1)
            if k == 0:
                min_con = con
                min_col = col
    return min_col

def incremental_repair(state):
    con = total_conflicts(state)
    print("initial conflicts: %s" % (con))
    while (con > 0):
        max_con = 0
        max_row = 0
        for i in range(len(state)):
            rowcon = rowconflicts(state, i)
            if (rowcon > max_con): 
                max_con = rowcon
                max_row = i
            if( rowcon == max_con):
                k = random.randint(0,1)
                if k == 0:
                    max_con = rowcon
                    max_row = i
        col = colconflicts(state, max_row)
        state[max_row] = col
        con = total_conflicts(state)
        print("conflicts: %s" % (con))
    return state

# =============================================================================
# RUN CODE
# =============================================================================
start = time.perf_counter()
board = csp_backtracking(generate_empty(32))
print("solution: %s" % (board))
print("verify: %s" % (test_solution(board)))
board = csp_backtracking(generate_empty(34))
print("solution: %s" % (board))
print("verify: %s" % (test_solution(board)))
board = generate(32)
print("initial: %s" % (board))
board = incremental_repair(board)
print("verify: %s" % (test_solution(board)))
board = generate(34)
print("initial: %s" % (board))
board = incremental_repair(board)
print("verify: %s" % (test_solution(board)))
end = time.perf_counter()
print("time: %s" % (end-start))
