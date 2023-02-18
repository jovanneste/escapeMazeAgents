import numpy as np
import random
import sys

global maze
global qtable


def up(index):
    return (index[0]-1, index[1])

def down(index):
    return (index[0]+1, index[1])

def left(index):
    return (index[0], index[1]-1)

def right(index):
    return (index[0], index[1]+1)


def step(state, a):
    actions = {0:up, 1:down, 2:left, 3:right}
    action = actions[a]
    done = False
    new_state = action(state)
    l = maze[new_state]
    if l!=[' ']:
        # if we hit a wall
        new_state = state
        reward = -1

    elif l==['F']:
        # if we are finished
        done = True
        reward = 10

    else:
        # move
        reward = 0

    return new_state, done, reward




maze = np.asarray([['+', '-', '+', '-', '+', '-', '+'],
        ['|', ' ', ' ', ' ', ' ', ' ', '|'],
        ['+', ' ', '+', '-', '+', ' ', '+'],
        ['|', '  ', ' ', 'F', '|', ' ', '|'],
        ['+', '-', '+', '-', '+', ' ', '+'],
        ['|', '$', ' ', ' ', ' ', ' ', '|'],
        ['+', '-', '+', '-', '+', '-', '+']])

maze = np.where((maze=='+')|(maze=='-')|(maze=='|'), 1, maze)


# quantise
spaces = np.argwhere(maze==' ')
mapping = {}
i=0
for space in spaces:
    mapping[tuple(space)] = i
    i+=1

state = np.where(maze == '$')
mapping[tuple(np.squeeze(state))] = len(mapping)


qtable = np.zeros((len(mapping), 4))

learning_rate = 0.9
discount_rate = 0.8
epsilon = 1.0
decay_rate= 0.005

num_episodes = 100
max_steps = 10


for episode in range(num_episodes):
    for s in range(max_steps):
        # exploration-exploitation tradeoff
        if random.uniform(0,1) < epsilon:
            # explore
            action = env.action_space.sample()
        else:
            # exploit
            action = np.argmax(qtable[state,:])


        # pick an action (0-up, 1-down, 2-left, 3-right)
        action = random.choice([0,1,2,3])

        # perfom action
        new_state, done, reward = step(state, action)

        new_state_index = mapping[tuple(np.squeeze(new_state))]
        old_state_index = mapping[tuple(np.squeeze(state))]


        # update q table
        qtable[new_state_index, action] += learning_rate * (reward + discount_rate * np.max(qtable[new_state_index,:])-qtable[old_state_index,action])

        state = new_state


        if done == True:
            break

    epsilon = np.exp(-decay_rate*episode)

print(f"Training completed over {num_episodes} episodes")
print(qtable)
