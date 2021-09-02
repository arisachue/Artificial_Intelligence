# -*- coding: utf-8 -*-

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
    # if len(set(state)) != len(state):
    #     return False
    # return check_diagonal(state)

def get_next_unassigned_var(state):
    for r in range(len(state)):
        if state[r] == "x":
            return r

def get_sorted_values(state, var):
    cant = set()
    for i in range(len(state)):
        if state[i] != "x":
            cant.add(int(state[i]))
            diff = i - int(state[i])
            cant.add(var-diff)
            add = i + int(state[i])
            cant.add(add-var)
    # for i in state:
    #     if i != "x":
    #         cant.add(int(i))
    #         diff = i-int(i)
    #         cant.add(var-diff)
    #         add = i+int(i)
    #         cant.add(var+add)
    values= []
    for i in range(len(state)):
        if i not in cant:
            values.append(i)
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

print(csp_backtracking(["x","x","x","x"]))

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