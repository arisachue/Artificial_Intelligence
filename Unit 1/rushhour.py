from collections import deque

dummy_heuristic = lambda tuple: 0;
default_heuristic = dummy_heuristic;

def create_puzzle(str, parent=None):
  return (default_heuristic(str), str, parent[2] if parent is not None else 0, parent);

# prints the board as a grid
def print_puzzle(board):
    print(*[board[x:x+6].replace("", " ") for x in range(0, 36, 6)], sep="\n");
    
# converts index of a board into (x,y)
coor = lambda v:(v//6,v%6);
# converts (x,y) to index
index = lambda x,y:6*x+y;

# returns all the possible moves
def get_children(parent):
    board = parent[1];
    numbers_used = set();
    for i in range(0, len(board)):
      if (board[i].isnumeric() or board[i] == "R") and board[i] not in numbers_used:
        numbers_used.add(board[i]);
        for tmp_board in move_tile(board, board[i], parent):
          yield tmp_board;

def move_tile(string, letter, parent):
  first_index = string.index(letter);
  horizontal = False;
  x, y = coor(first_index)
  if string[index(x+1, y)] == letter:
    horizontal = True;
  
  length = 2;
  if horizontal:
    if index(x+2, y) < len(string) and string[index(x+2, y)] == letter:
      length = 3;
  else:
    if index(x, y+2) < len(string) and string[index(x, y+2)] == letter:
      length = 3;

  #print(letter, horizontal);

  if horizontal:
    for k in range(0, 6-length):
      isGood = True;
      for idx in range(k, k+length):
        if string[index(k, y)] not in (letter, "x"):
          isGood = False;
      if isGood:
        new_board = list(string.replace(letter, "x"));
        for l in range(k, k+length):
          new_board[index(l, y)] = letter;
        yield create_puzzle("".join(new_board), parent=parent);
  else: # obj is vertical
    for k in range(0, 6-length):
      isGood = True;
      for idx in range(k, k+length):
        if string[index(x, k)] not in (letter, "x"):
          isGood = False;
      if isGood:
        new_board = list(string.replace(letter, "x"));
        for l in range(k, k+length):
          new_board[index(x, l)] = letter;
        yield create_puzzle("".join(new_board), parent=parent);

def is_goal(board):
  if board[index(1,4)] == "R" and board[index(1,5)] == "R":
    return True
  return False

def bfs(board):
  path=0
  fringe = deque() # queue to look at
  visited = dict() # puzzles already analyzed                  
  fringe.append(board)
  visited[board[1]] = board
  while fringe:
    tuple = fringe.popleft();
    # print(tuple);
    if is_goal(tuple[1]):
      return tuple;
    for c in get_children(tuple):
      if c not in visited:
        fringe.append(c);
        visited[c[1]] = c;
  return None

print(bfs(create_puzzle("111223RRxxx3xxxxxxxxxxxxxxxxxxxxxxxx")))