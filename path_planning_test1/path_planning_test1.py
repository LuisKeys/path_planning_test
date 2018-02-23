# ----------
# User Instructions:
# 
# Define a function, search() that returns a list
# in the form of [optimal path length, row, col]. For
# the grid shown below, your function should output
# [11, 4, 5].
#
# If there is no valid path from the start point
# to the goal, your function should return the string
# 'fail'
# ----------

# Grid format:
#   0 = Navigable space
#   1 = Occupied space

grid = [[0, 0, 1, 0, 0, 0],
        [0, 0, 1, 0, 0, 0],
        [0, 0, 0, 0, 1, 0],
        [0, 0, 1, 1, 1, 0],
        [0, 0, 0, 0, 1, 0]]
init = [0, 0]
goal = [len(grid)-1, len(grid[0])-1]
cost = 1

delta = [[-1, 0], # go up
         [ 0,-1], # go left
         [ 1, 0], # go down
         [ 0, 1]] # go right

delta_name = ['^', '<', 'v', '>']

path = []

def print_matrix(matrix):
    for row in range(len(matrix) - 1):
        print(matrix[row])

def search(grid,init,goal,cost):
    # ----------------------------------------
    # insert code here
    # ----------------------------------------
    
    print_matrix(grid)
    print(path)
    input("Press key...")
    # Explore available cells with provided cost
    grid[init[0]][init[1]] = 1
    previous_cost = 0
    for delta_step in delta:
        inc_row = init[0] + delta_step[0];
        inc_col = init[1] + delta_step[1];
        # Get original initial cost
        for path_step in path:
            if inc_row == path_step[0]:
                if inc_col == path_step[1]:
                    previous_cost = path_step[2]

        if inc_row >= 0 and inc_col >= 0:
            if grid[inc_row][inc_col] == 0:
                path.append([inc_row, inc_col, cost + previous_cost])
    for path_step in path:
        row = path_step[0]
        col = path_step[1]
        g = path_step[2]
        if grid[row][col] == 0:
            init[0] = row
            init[1] = col
            search(grid, init, goal, cost)  
        else:
            return path    
    
    return path

search(grid, init, goal, cost)