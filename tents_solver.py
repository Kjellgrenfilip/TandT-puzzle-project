from z3 import *

class TentSolver:
    def __init__(self, rows, columns, row_tent_counts, column_tent_counts, tree_locations):
        self.rows = rows
        self.columns = columns
        self.row_tent_counts = row_tent_counts
        self.column_tent_counts = column_tent_counts
        self.tree_locations = tree_locations
        #using the Bool-function from Z3 to represent every variable in the grid. So far all we know is
        #that there can be a tent in every tile of the grid. Bool allows us to use Boolean logic when constructing constraints.
        # Results in a row*column 2d grid.
        self.tent_variables = [[Bool("tent_on_tile_%d_%d" % (j, i)) for i in range(columns)] for j in range(rows)]
        self.solver = Solver()

    #The following function sets all constraints for the tent and tree puzzle. The contraints themselves are explained below.
    def set_constraints(self):
        self._add_row_constraints()
        self._add_column_constraints()
        self._add_tree_constraints()
        self._add_tent_adjacency_constraints()
        self._add_tree_adjacency_constraints()
        self._add_no_adjacent_tent_variables_constraints()

    #Constraint1: ensure the correct amount of tents on every i:th row.
    def _add_row_constraints(self):
        for i in range(self.rows):
            self.solver.add(Sum(self.tent_variables[i]) == self.row_tent_counts[i])
            
    #Constraint2: ensure the correct amount of tents on every j:th column.
    def _add_column_constraints(self):
        for j in range(self.columns):
            self.solver.add(Sum([self.tent_variables[i][j] for i in range(self.rows)]) == self.column_tent_counts[j])

    #Constraint3: ensure no tent is places where there is already a tree.
    def _add_tree_constraints(self):
        for row, col in self.tree_locations:
            self.solver.add(Not(self.tent_variables[row][col]))
    
    #Constraint4: ensure that every tent has atleast one adjacent tree (in horizontal and vertical direction)
    def _add_tent_adjacency_constraints(self):
        for i, j in self.tree_locations:
            adjacent_tent_variables = []

            for di, dj in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                if 0 <= i + di < self.rows and 0 <= j + dj < self.columns:
                    adjacent_tent_variables.append(self.tent_variables[i + di][j + dj])

            self.solver.add(Or(*adjacent_tent_variables))

    #Constraint5: ensure that every tree has atleast one adjacent tent.
    def _add_tree_adjacency_constraints(self):
        for i in range(self.rows):
            for j in range(self.columns):
                adjacent_trees = []

                if i > 0:
                    adjacent_trees.append((i - 1, j) in self.tree_locations)
                if i < self.rows - 1:
                    adjacent_trees.append((i + 1, j) in self.tree_locations)
                if j > 0:
                    adjacent_trees.append((i, j - 1) in self.tree_locations)
                if j < self.columns - 1:
                    adjacent_trees.append((i, j + 1) in self.tree_locations)
                
                self.solver.add(Implies(self.tent_variables[i][j], Or(*adjacent_trees)))

    #Constraint6: ensure no tent next to each other in any direction (horizontal,vertical, diagonal)
    def _add_no_adjacent_tent_variables_constraints(self):
        for i in range(self.rows):
            for j in range(self.columns):
                for di, dj in [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (-1, 1), (1, -1), (1, 1)]:
                    if 0 <= i + di < self.rows and 0 <= j + dj < self.columns:
                        self.solver.add(Not(self.tent_variables[i][j] & self.tent_variables[i + di][j + dj]))

    def get_solver(self):
        return self.solver
    
    def get_tent_variables(self):
        return self.tent_variables
