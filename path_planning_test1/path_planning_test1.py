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

# Initial point, goal and cost
init = [0, 0]
goal = [len(grid)-1, len(grid[0])-1]
cost = 1

# possible movements
delta = [[-1, 0], # go up
         [ 0,-1], # go left
         [ 1, 0], # go down
         [ 0, 1]] # go right

delta_name = ['^', '<', 'v', '>']

# Handy function to display a matrix
def print_matrix(matrix):
    for row in range(len(matrix)):
        print(matrix[row])

def search():
    # Buffer to mark closed nodes
    closed = []

    for row in range(len(grid)):
        closed_row = []
        for col in range(len(grid[0])):
            closed_row.append(0)
        closed.append(closed_row)
       
    # Mark initial point as closed    
    closed[init[0]][init[1]] = 1

    row = init[0]
    col= init[1]
    g = 0

    # Init open list
    open = [[g, row, col]]

    # process flags
    found = False
    resign = False

    # print('Initial open list')
    # print_matrirow(open)

    # Main iteration
    while found is False and resign is False:    
        # Empty open list means no solution
        if len(open) == 0:
            resign = True
            print('fail')
        #  Else continue search
        else:
            # Remove minor g value node from list
            open.sort()
            open.reverse()
            next = open.pop()

            row = next[1]
            col = next[2]
            g = next[0]

            # Check if next node is the goal
            if row == goal[0] and col == goal[1]:
                found = True
                print(next)
            # It is not the goal then evaluate movements
            else:
                # Explore winning node, try to move on all possible directions
                for i in range(len(delta)):
                    row_inc = row + delta[i][0]
                    col_inc = col + delta[i][1]
                    # Only add nodes within the grid
                    if row_inc >= 0 and col_inc >= 0 and row_inc < len(grid) and col_inc < len(grid[0]):
                        # Only add nodes on available locations (open and no obstacle)
                        if closed[row_inc][col_inc] == 0 and grid[row_inc][col_inc] == 0:
                            # Update previous cost
                            g_inc = g + cost
                            next_step = [g_inc, row_inc, col_inc]
                            open.append(next_step)
                            closed[row_inc][col_inc] = 1

search()