import numpy as np
import sys

maze = np.asarray([['+', '-', '+', '-', '+', '-', '+'],
        ['|', ' ', ' ', ' ', ' ', ' ', '|'],
        ['+', ' ', '+', '-', '+', ' ', '+'],
        ['|', '  ', ' ', 'F', '|', ' ', '|'],
        ['+', '-', '+', '-', '+', ' ', '+'],
        ['|', '$', ' ', ' ', ' ', ' ', '|'],
        ['+', '-', '+', '-', '+', '-', '+']])

maze = np.where((maze=='+')|(maze=='-')|(maze=='|'), 1, maze)
index = np.where(maze == '$')

print(maze)
print(index)
print(maze[index])

def up(index):
    return (index[0]-1, index[1])

def down(index):
    return (index[0]+1, index[1])

def left(index):
    return (index[0], index[1]-1)

def right(index):
    return (index[0], index[1]+1)





sys.exit()
def step(state, action):


    return new_state, done, reward
