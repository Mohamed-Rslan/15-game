
import random
import queue

class node:

    def __init__(self, state, parent = None, action = None ,cost = 0):
        self.state = state
        self.parent = parent   
        self.action = action
        self.cost = cost


def generate_random_initial():
    numbers = list(range(16))
    random.shuffle(numbers)
    grid = []
    for i in range(4):
        grid.append(numbers[i * 4: (i + 1) * 4])

    return grid

rand_init = generate_random_initial()

def expand(n):
    child = []
    for i in range(4):
        for j in range(4):
            if n.state[i][j] == 0 :
                loc =[i, j]


    if ( loc[0] > 0 ):
        new_state = action("up", n.state, loc)
        child.append(node(new_state, n, "up", n.cost+1))

    if ( loc[0] < 3 ):
        new_state = action("down", n.state, loc)
        child.append(node(new_state, n, "down", n.cost+1))

    if ( loc[1] > 0 ):
        new_state = action("left", n.state, loc)
        child.append(node(new_state, n, "left", n.cost+1))

    if ( loc[1] < 3 ):
        new_state = action("right", n.state, loc)
        child.append(node(new_state, n, "right", n.cost+1))
    return child



def action(dir, state, loc):
    if dir == "left":
        state[ loc[0] ][ loc[1] ], state[ loc[0] ][ loc[1] - 1 ] = state[ loc[0] ][ loc[1]-1 ], state[ loc[0] ][ loc[1] ]

    if dir == "right":
        state[ loc[0] ][ loc[1] ], state[ loc[0] ][ loc[1] + 1 ] = state[ loc[0] ][ loc[1] + 1 ], state[ loc[0] ][ loc[1] ]

    if dir == "up":
        state[ loc[0] ][ loc[1] ], state[ loc[0] + 1][ loc[1]] = state[loc[0] + 1 ][ loc[1]], state[ loc[0] ][ loc[1] ]
        
    if dir == "down":
        state[ loc[0] ][ loc[1] ], state[ loc[0] - 1][ loc[1]] = state[loc[0] - 1 ][ loc[1]], state[ loc[0] ][ loc[1] ]
    return state



