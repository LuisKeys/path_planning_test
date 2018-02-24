# ----------
# User Instructions:
# 
# Create a function compute_value which returns
# a grid of values. The value of a cell is the minimum
# number of moves required to get from the cell to the goal. 
#
# If a cell is a wall or it is impossible to reach the goal from a cell,
# assign that cell a value of 99.
# ----------

grid = [[0, 0, 1, 0, 0, 0],
        [0, 0, 1, 0, 0, 0],
        [0, 0, 1, 0, 0, 0],
        [0, 0, 0, 0, 1, 0],
        [0, 0, 1, 1, 1, 0],
        [0, 0, 0, 0, 1, 0]]

goal = [len(grid)-1, len(grid[0])-1]
cost = 1 # the cost associated with moving from a cell to an adjacent one

delta = [[-1, 0 ], # go up
         [ 0, -1], # go left
         [ 1, 0 ], # go down
         [ 0, 1 ]] # go right

delta_name = ['^', '<', 'v', '>']

# Check progress
def isCompleted(progress):
    for row in range(len(progress)):
        for col in range(len(progress[0])):
            if progress[row][col] == 0:
                return False

    return True    

# Handy function to display a matrix
def print_matrix(matrix):
    for row in range(len(matrix)):
        print(matrix[row])


def compute_value(grid,goal,cost):
    # Create values matrix
    values = []

    for row in range(len(grid)):
        values_row = []
        for col in range(len(grid[0])):
            values_row.append(0)
        values.append(values_row)

    # Create progress matrix
    progress = []

    for row in range(len(grid)):
        progress_row = []
        for col in range(len(grid[0])):
            progress_row.append(0)
        progress.append(progress_row)

    # Populate with high values for obstacles
    for row in range(len(grid)):
        for col in range(len(grid[0])):
            if grid[row][col] == 1:
                values[row][col] = 99

    # Populate with high values for obstacles
    for row in range(len(grid)):
        for col in range(len(grid[0])):
            if grid[row][col] == 1:
                progress[row][col] = 1

    # Mark goal as processed
    progress[goal[0]][goal[1]] == 1

    # Iterate until completed
    while not isCompleted(progress):

        # Explore all the cells in the grid
        for row in range(len(grid)):
            for col in range(len(grid[0])):

                # Is not processed?
                if progress[row][col] == 0:

                    #Check all nightbours
                    for step in delta:
                        row_inc = row + step[0]
                        col_inc = col + step[1]

                        # Is cursor within grid?

                        if row_inc >= 0 and row_inc < len(grid) and col_inc >= 0 and col_inc < len(grid[0]):
                            prev_value = values[row_inc][col_inc]

                            # Has a value or is Goal?
                            neightbour_value = values[row_inc][col_inc]
                            if (neightbour_value > 0 and neightbour_value < 99) or (goal[0] == row_inc and goal[1] == col_inc):
                                values[row][col] = neightbour_value + cost
                                progress[row][col] = 1

    values[goal[0]][goal[1]] = 0
    
    return values

values = compute_value(grid,goal,cost)
print("Values:")
print_matrix(values)


