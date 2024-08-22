from collections import deque

def is_valid(state,num):
    missionaries, cannibals, boat = state
    if missionaries < 0 or cannibals < 0 or missionaries > num or cannibals > num:
        return False
    if missionaries > 0 and missionaries < cannibals:
        return False
    if num - missionaries > 0 and num - missionaries < num - cannibals:
        return False
    return True

def get_successors(state,num):
    successors = []
    missionaries, cannibals, boat = state
    moves = [(2, 0), (0, 2), (1, 1), (1, 0), (0, 1)]
    for move in moves:
        if boat == 1:
            new_state = (missionaries - move[0], cannibals - move[1], 0)
        else:
            new_state = (missionaries + move[0], cannibals + move[1], 1)
        if is_valid(new_state,num):
                successors.append(new_state)    
    return successors

def bfs(start_state, goal_state,num):
    queue = deque([(start_state, [])])
    visited = set()
    while queue:
        (state, path) = queue.popleft()
        if state in visited:
            continue
        visited.add(state)
        path = path + [state]
        if state == goal_state:
            return path
        for successor in get_successors(state,num):
            queue.append((successor, path))
    return None

num=4
start_state = (num, num, 1)
goal_state = (0, 0, 0)

solution = bfs(start_state, goal_state,num)
if solution:
    print("Solution found:")
    for step in solution:
        print(step)
else:
    print("No solution found.")
