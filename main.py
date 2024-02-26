from z3 import *
import sys
import tents_solver


def parse_puzzle(file_name):
    row_tent_counts = list()
    tree_locations = []
    with open(file_name, 'r') as file:
        rows, columns = map(int, file.readline().split())
        for line in range(rows):
            row_data = [char for char in file.readline().strip()]
            row_tent_counts.append(int(row_data[columns+1]))
            
            
            for j, cell in enumerate(row_data):
                if(cell == 'T'):
                    tree_locations.append((line,j))
        
        column_tent_counts = list(map(int, file.readline().split()))
        
    return rows, columns, row_tent_counts, column_tent_counts, tree_locations

def print_puzzle(file_name, solution):
    rows, columns, row_tent_counts, column_tent_counts, tree_locations = parse_puzzle(file_name)
    
    with open(file_name, 'r') as file:
        lines = file.readlines()
        
        print("The following puzzle was provided: "+'\n')
        for line in lines:
            print(line, end='')
    print()
    print('\n'+"The following solution was given by the solver:" + '\n')
    
    print(rows ,columns)
    for row in range(rows):
        for col in range(columns):
            if((row, col) in tree_locations):
                print('T', end=' ')
            elif((row, col) in solution):
                print('∧', end=' ')
            else:    
                print('.', end=' ')
        print('',row_tent_counts[row])
    for i in column_tent_counts:
        print(i, end=' ')
    print('= ' + str(sum(column_tent_counts)))
    print("Number of tents placed: "+str(len(solution)))


def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <puzzle_file>")
        return
    puzzle_file = sys.argv[1]
    
    #parse the given puzzle input. Tree locations are given by a tuple of coords (row,col)
    rows, columns, row_tent_counts, column_tent_counts, tree_locations = parse_puzzle(puzzle_file)
    
    #basic checks to see if the puzzle is even solvable straight away.
    #Check: The amount of tents to be places are the same amount in the rows and columns
    #Check: The amount of tress are the same as the object amount of tents to be placed.
    if(sum(row_tent_counts) == sum(column_tent_counts) & len(tree_locations) == sum(row_tent_counts)):    
        solver = tents_solver.TentSolver(rows, columns, row_tent_counts, column_tent_counts, tree_locations)
        solver.set_constraints()
        
        solution = []
        if solver.get_solver().check() == sat:
            m = solver.get_solver().model()
            tents = solver.get_tent_variables()
            
            for i in range(rows):
                for j in range(columns):
                    #is_true comes with the z3-package. Since the built in z3-booleans.
                    if is_true(m[tents[i][j]]):
                        solution.append((i,j)) 
            print_puzzle(puzzle_file, solution)
        else:
            print("The problem is unsatisfiable.")

        
        if(len(solution) == sum(column_tent_counts)):
            print("The correct amount of tents were places")
    else:
        print("The puzzle provided either comes in the wrong format, or it is not satisfiable")

if __name__ ==  '__main__':
    main()
    

    


    
