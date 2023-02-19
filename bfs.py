import numpy as np
from queue import Queue

maze = np.array([['+', '-', '+', '-', '+', '-', '+'],
                  ['|', ' ', ' ', ' ', ' ', ' ', '|'],
                  ['+', ' ', '+', '-', '+', ' ', '+'],
                  ['|', ' ', ' ', 'F', '|', ' ', '|'],
                  ['+', '-', '+', '-', '+', ' ', '+'],
                  ['|', '$', ' ', ' ', ' ', ' ', '|'],
                  ['+', '-', '+', '-', '+', '-', '+']])


start = np.argwhere(maze == '$')
finish = np.argwhere(maze == 'F')
start = tuple(map(tuple, start))[0]
finish = tuple(map(tuple, finish))[0]


moves = [(0, 1), (0, -1), (1, 0), (-1, 0)]
directions = {(0,1):"right",(0,-1):"left",(1,0):"down",(-1,0):"up"}

visited = np.zeros(maze.shape, dtype=bool)

q = Queue()
q.put(start)

distances = {start: 0}


while not q.empty():
    current = q.get()
    if current == finish:
        break
    for move in moves:
        next_pos = (current[0] + move[0], current[1] + move[1])
        if (not visited[next_pos] and maze[next_pos] == ' ' or maze[next_pos] == 'F'):
            q.put(next_pos)
            visited[next_pos] = True
            distances[next_pos] = distances[current] + 1


path = [finish]
while path[-1] != start:
    current = path[-1]
    for move in moves:
        next_pos = (current[0] + move[0], current[1] + move[1])
        if (next_pos in distances and
            distances[next_pos] == distances[current] - 1):
            path.append(next_pos)
            break

path = path[::-1]
final_directions = []
for i in range(len(path)-1):
    current_place = path[i]
    next_place = path[i+1]
    direction = (next_place[0]-current_place[0],next_place[1]-current_place[1])
    final_directions.append(directions[direction])

print(', '.join(final_directions))