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
    closed = [[0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0]]

    # Mark initial point as closed    
    closed[init[0]][init[1]] = 1

    x = init[0]
    y = init[1]
    g = 0

    # Init open list
    open = [[g, x, y]]

    # process flags
    found = False
    resign = False

    # print('Initial open list')
    # print_matrix(open)

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

            x = next[1]
            y = next[2]
            g = next[0]

            # Check if next node is the goal
            if x == goal[0] and y == goal[1]:
                found = True
                print(next)
            # It is not the goal then evaluate movements
            else:
                # Explore winning node, try to move on all possible directions
                for i in range(len(delta)):
                    x2 = x + delta[i][0]
                    y2 = y + delta[i][1]
                    # Only add nodes within the grid
                    if x2 >= 0 and y2 >= 0 and x2 < len(grid) and y2 < len(grid[0]):
                        # Only add nodes on available locations (open and no obstacle)
                        if closed[x2][y2] == 0 and grid[x2][y2] == 0:
                            # Update previous cost
                            g2 = g + cost
                            open.append([g2, x2, y2])
                            closed[x2][y2] = 1

search()