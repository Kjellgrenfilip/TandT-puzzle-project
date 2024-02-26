# Tents and Trees Solver

This project is part of the "Introduction to AI 1" course at the University of Klagenfurt. The aim of this project is to implement a Solver agent for the Tents and Trees puzzle.

## Tents and Trees Puzzle

The Tents and Trees puzzle is a logic puzzle where the player must place tents in a grid of trees. The objective is to place tents according to specific rules:

- Each tree must have exactly one adjacent tent horizontally or vertically.
- Tents cannot be adjacent to each other horizontally, vertically, or diagonally.
- Tents cannot be placed on trees.

## Solver Agent

The Solver agent implemented in this project aims to automatically solve Tents and Trees puzzles using the Z3 library from Microsoft Research [Z3 GitHub](https://github.com/Z3Prover/z3/wiki). The agent analyzes the puzzle grid and intelligently determines the optimal placement of tents to satisfy all puzzle constraints. 

## Features

- Solves Tents and Trees puzzles automatically given the below input format.

    ```
    5 10
    .......... 0
    ......T... 2
    ..T...T... 0
    .......... 1
    .......... 0
    0 0 1 0 0 0 1 1 0 0
    ```

    Where 5 and 10 represent the grid dimensions 5x10.
    . = empty spot. T = tree
    Numbers on the right = The number of tents to be placed in each row.
    Bottom numbers = The number of tents to be placed in each column.

- Provides visualization of the solved puzzle grid.

## Usage
Running on python version 3.9.10
To use the Solver agent:

1. Clone this repository to your local machine.
2. Install the necessary dependencies from the requirements.txt file.
3. Run the Solver agent with the given puzzle input as follows:
    ```
    python main.py <path_to_puzzle_file>
    ```
4. View the solved puzzle grid.

## Testing

Testing for the Tents and Trees Solver is done using the Python `unittest` framework. The `TestSolverFunctionality` class contains various test methods that assess the functionality of the Solver agent under different scenarios. Each test method sets up a Tents and Trees puzzle with specific parameters and constraints, runs the Solver agent, and then asserts whether the generated solution satisfies the puzzle constraints.

Run the tests:
```
python tests.py
```

To add more tests, additional test methods can be defined within the `TestSolverFunctionality` class. These methods should follow the naming convention of starting with 'test_' to be automatically discovered and executed by the `unittest` framework. Each test method should create a new Tents and Trees puzzle with unique parameters and constraints, run the Solver agent, and assert the correctness of the generated solution.
