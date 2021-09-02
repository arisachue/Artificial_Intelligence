# -*- coding: utf-8 -*-
import time

def check_diagonal(state):
    # dia = set()
    for i in range(len(state)-1):
        for n in range(i+1, len(state)):
            if i-int(state[i]) == n-int(state[n]) or i+int(state[i]) == n+int(state[n]):
                return False
    return True

def goal_test(state):
    if "x" in state:
        return False
    return True

def get_next_unassigned_var(state):
    for r in range(int(len(state)/2)-1, -1, -1):
        if state[r] == "x":
            return r
        if state[len(state)-r-1] == "x":
            return len(state)-r-1
    # starting from the edges
    # for r in range(int(len(state)/2)):
    #     if state[r] == "x":
    #         return r
    #     if state[len(state)-r-1] == "x":
    #         return len(state)-r-1

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
    # for i in range(len(state)):
    #     if i not in cant:
    #         values.append(i)
    # for i in range(int(len(state)/2)-1, -1):
    #     if i not in cant:
    #         values.append(i)
    #     if (len(state)-i-1) not in cant:
    #         values.append(len(state)-i-1)
    # starting from the edges
    for i in range(int(len(state)/2)):
        if i not in cant:
            values.append(i)
        if (len(state)-i-1) not in cant:
            values.append(len(state)-i-1)
    return values
        
def csp_backtracking(state):
    # print(state)
    # input()
    if goal_test(state): return state
    var = get_next_unassigned_var(state)
    # print(var)
    # input()
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

# board = ["x","x","x","x","x","x","x","x","x","x","x","x","x","x","x","x","x","x","x","x","x","x","x","x","x","x","x","x","x","x","x","x","x","x"]
# print(len(board))
# print(len(board)/2)
# board = ["x","x","x","x","x","x","x","x"]
start = time.perf_counter()
board = generate_empty(200)
board = csp_backtracking(board)
end = time.perf_counter()
print("%s seconds" % (end-start))
print(board)

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
# board = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29]
# board = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28]
print(test_solution(board))