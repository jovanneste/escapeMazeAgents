import numpy as np
import sys

global maze

maze = np.asarray([['+', '-', '+', '-', '+', '-', '+'],
        ['|', ' ', ' ', ' ', ' ', ' ', '|'],
        ['+', ' ', '+', '-', '+', ' ', '+'],
        ['|', '  ', ' ', 'F', '|', ' ', '|'],
        ['+', '-', '+', '-', '+', ' ', '+'],
        ['|', '$', ' ', ' ', ' ', ' ', '|'],
        ['+', '-', '+', '-', '+', '-', '+']])

maze = np.where((maze=='+')|(maze=='-')|(maze=='|'), 1, maze)
print(maze)


def up(index):
    return (index[0]-1, index[1])

def down(index):
    return (index[0]+1, index[1])

def left(index):
    return (index[0], index[1]-1)

def right(index):
    return (index[0], index[1]+1)




def step(state, action):
    done = False
    new_state = maze[action(state)]
    print(new_state)
    if new_state!=[' ']:
        print('wall')
        # if we hit a wall
        new_state = state
        reward = -1

    elif new_state==['F']:
        print('finished')
        # if we are finished
        done = True
        reward = 10

    else:
        print('space')
        # move
        reward = 0

    return new_state, done, reward


state = np.where(maze == '$')
step(state, right)
