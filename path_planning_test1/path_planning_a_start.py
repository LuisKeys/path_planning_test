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


#grid = [[0, 0, 1, 0, 0, 0],
#        [0, 0, 1, 0, 0, 0],
#        [0, 0, 0, 0, 1, 0],
#        [0, 0, 1, 1, 1, 0],
#        [0, 0, 0, 0, 1, 0]]

grid = [[0, 1, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0]]

heuristic = [[9, 8, 7, 6, 5, 4],
             [8, 7, 6, 5, 4, 3],
             [7, 6, 5, 4, 3, 2],
             [6, 5, 4, 3, 2, 1],
             [5, 4, 3, 2, 1, 0]]

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
    
    # Init expand, closed and directions and directions_mark matrices
    node_index = 0
    expand = []
    closed = []
    directions = []
    directions_marks = []

    for row in range(len(grid)):
        expand_row = []
        for col in range(len(grid[0])):
            expand_row.append(0)
        expand.append(expand_row)
       
    for row in range(len(grid)):
        closed_row = []
        for col in range(len(grid[0])):
            closed_row.append(0)
        closed.append(closed_row)

    for row in range(len(grid)):
        directions_row = []
        for col in range(len(grid[0])):
            directions_row.append(" ")
        directions.append(directions_row)

    for row in range(len(grid)):
        directions_marks_row = []
        for col in range(len(grid[0])):
            directions_marks_row.append(0)
        directions_marks.append(directions_marks_row)

    # Mark initial point as closed    
    closed[init[0]][init[1]] = 1

    row = init[0]
    col= init[1]
    g = 0
    f = g + heuristic[row][col]

    # Init open list
    open = [[f, g, row, col]]

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

            g = next[1]
            row = next[2]
            col = next[3]

            # Check if next node is the goal
            if row == goal[0] and col == goal[1]:
                found = True
                directions[row][col] = "*"
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
                            f = g_inc + heuristic[row_inc][col_inc]
                            next_step = [f, g_inc, row_inc, col_inc]
                            open.append(next_step)
                            node_index += 1
                            directions[row][col] = delta_name[i]
                            expand[row_inc][col_inc] = node_index
                            closed[row_inc][col_inc] = 1

    # Set to -1 no expanded locations
    for row in range(len(expand)):
        for col in range(len(expand[0])):
            if expand[row][col] == 0 and not (row == init[0] and col == init[1]):
                expand[row][col] = -1

    # Analyze directions to get clean final path
    found = False
    row_cur = init[0]
    col_cur = init[1]

    while not found:
        if row_cur == goal[0] and col_cur == goal[1]:
            found = True
        directions_marks[row_cur][col_cur] = 1
        if directions[row_cur][col_cur] == '>':
            col_cur += 1
        elif directions[row_cur][col_cur] == '<':
            col_cur -= 1
        elif directions[row_cur][col_cur] == '^':
            row_cur -= 1
        elif directions[row_cur][col_cur] == 'v':
            row_cur += 1

    for row in range(len(directions)):
        for col in range(len(directions[0])):
            if directions_marks[row][col] == 0:
                directions[row][col] = ' '

    print("-------------")
    print("Expand matrix")
    print_matrix(expand)

    print("-------------")
    print("Directions matrix")
    print_matrix(directions)

search()

