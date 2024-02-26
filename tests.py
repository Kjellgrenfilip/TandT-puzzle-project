import tents_solver
import unittest
from z3 import *


class TestSolverFunctionality(unittest.TestCase):

    # Define test methods that start with 'test_'
    '''
    . 0
    . 1
    T 0
    . 1
    T 0
    2
    '''
    def test_simple_case_satisfiable(self):
        solver = tents_solver.TentSolver(5, 1, [0,1,0,1,0], [2], [(2,0),(4,0)])
        solver.set_constraints()
        c = solver.get_solver().check()
        self.assertEqual(c, sat)
        
    '''
    . 1
    . 0
    T 0
    . 1
    T 0
    2
    '''
    def test_simple_case_not_satisfiable(self):
        solver = tents_solver.TentSolver(5, 1, [1,0,0,1,0], [2], [(2,0),(4,0)])
        solver.set_constraints()
        c = solver.get_solver().check()
        self.assertNotEqual(c, sat)
        
    '''
    . 0
    . 1
    T 0
    . 1
    T 0
    3
    '''
    def test_simple_case2_not_satisfiable(self):
        solver = tents_solver.TentSolver(5, 1, [0,1,0,1,0], [3], [(2,0),(4,0)])
        solver.set_constraints()
        c = solver.get_solver().check()
        self.assertNotEqual(c, sat)
        
    '''
    . 0
    . 0
    T 0
    . 1
    T 0
    2
    '''
    def test_simple_case3_not_satisfiable(self):
        solver = tents_solver.TentSolver(5, 1, [0,0,0,1,0], [2], [(2,0),(4,0)])
        solver.set_constraints()
        c = solver.get_solver().check()
        self.assertNotEqual(c, sat)
    
    '''
    5 1
    . 0
    . 0
    T 0
    . 1
    T 0
    1
    '''
    def test_simple_case4_not_satisfiable(self):
        solver = tents_solver.TentSolver(5, 1, [0,0,0,1,0], [1], [(2,0),(4,0)])
        solver.set_constraints()
        c = solver.get_solver().check()
        self.assertNotEqual(c, sat)
        
    '''
    1 5
    ..T.T 2
    0 1 0 1 0
    '''
    def test_simple_case2_satisfiable(self):
        solver = tents_solver.TentSolver(1, 5, [2],[0,1,0,1,0], [(0,2),(0,4)])
        solver.set_constraints()
        c = solver.get_solver().check()
        self.assertEqual(c, sat)
        m = solver.get_solver().model()
        tents = solver.get_tent_variables()
        
        self.assertTrue(is_true(m[tents[0][1]])) #correct tent placement
        self.assertTrue(is_true(m[tents[0][3]])) #correct tent placement
        
    '''
    8 8
    ..T.T.T. 3
    .T....T. 1
    ...T.... 2
    ....TT.. 1
    ........ 2
    .T....T. 1
    T....... 1
    .....T.. 1
    1 3 0 1 2 2 1 2
    '''
    def test_larger_case(self):
        solver = tents_solver.TentSolver(8, 8, [3,1,2,1,2,1,1,1],[1,3,0,1,2,2,1,2], [(0,2),(0,4),(0,6),(1,1),(1,6),(2,3),(3,4),(3,5),(5,1),(5,6),(6,0),(7,5)])
        solver.set_constraints()
        c = solver.get_solver().check()
        self.assertEqual(c, sat)
        m = solver.get_solver().model()
        tents = solver.get_tent_variables()
        
        self.assertTrue(is_true(m[tents[0][1]])) #correct tent placement
        self.assertTrue(is_true(m[tents[0][3]])) #correct tent placement
        self.assertTrue(is_true(m[tents[0][5]])) #correct tent placement
        self.assertTrue(is_true(m[tents[1][7]])) #correct tent placement
        self.assertTrue(is_true(m[tents[2][1]])) #correct tent placement
        self.assertTrue(is_true(m[tents[7][0]])) #correct tent placement
        
        
        

# If this script is run directly, run the tests
if __name__ == '__main__':
    unittest.main()