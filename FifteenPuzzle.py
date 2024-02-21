from FifteenPuzzle_Helpers import node , generate_random_initial
from terminaltables import SingleTable




class problem:
    def __init__(self, state):
        self.initial = node (state)
        self.goal =[[1, 2, 3, 4],
                [5, 6, 7, 8],
               [9, 10, 11, 12],
               [13, 14, 15 , 0] ]
        
goal =[[1, 2, 3, 4],
        [5, 6, 7, 8],
        [9, 10, 11, 12],
        [13, 14, 15 , 0] ]
def print_state(state,dir):
    for i in range(4):
        for j in range(4):
            if state[i][j] == 0 :
                loc = [i, j]

    if dir == "left":
        state[ loc[0] ][ loc[1] ] = "←"

    if dir == "right":
        state[ loc[0] ][ loc[1] ] = "→"

    if dir == "up":
        state[ loc[0] ][ loc[1] ] = "↑"
        
    if dir == "down":
        state[ loc[0] ][ loc[1] ] = "↓"

    table = SingleTable(state)
    table.inner_row_border = True
    print(table.table)

print_state(goal,"up")
