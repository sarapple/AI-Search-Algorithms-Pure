# Algorithm to solve 8-Puzzle Game

## Author
Sara Wong @sarapple

## Course from edx
ColumbiaX: CSMM.101x
Artificial Intelligence (AI)

## The Task

Implement an agent to solve the 8-puzzle game.  Implement and compare several search algorithms, and collect statistics related to their performances. 

Rules:
```
An instance of the N-puzzle game consists of a board holding N = m^2 − 1 (m = 3, 4, 5, ...) distinct movable tiles, plus an empty space. The tiles are numbers from the set {1, …, m^2 − 1}. For any such board, the empty space may be legally swapped with any tile horizontally or vertically adjacent to it. In this assignment, we will represent the blank space with the number 0 and focus on the m = 3 case (8-puzzle).

Given an initial state of the board, the combinatorial search problem is to find a sequence of moves that transitions this state to the goal state; that is, the configuration with all tiles arranged in ascending order ⟨0, 1, …, m^2 − 1⟩. The search space is the set of all possible states reachable from the initial state.

The blank space may be swapped with a component in one of the four directions {‘Up’, ‘Down’, ‘Left’, ‘Right’}, one move at a time. The cost of moving from one configuration of the board to another is the same and equal to one. Thus, the total cost of path is equal to the number of moves made from the initial state to the goal state.
```

A preexisting skeleton is provided from `puzzle_state.py` and `driver.py` (essentially the game structure and not the algorithms), and all other code is written by myself.
- The `puzzle_state.py` file was adjusted from the original to return a list of tuples of (direction, child) instead of just a list of children.
- `driver.py` was adjusted to use my code

## Process for revealing nodes
Searches begin by visiting the root node of the search tree, given by the initial state. Among other book-keeping details, three major things happen in sequence in order to visit a node:

- First, we remove a node from the frontier set.
- Second, we check the state against the goal state to determine if a solution has been found.
- Finally, if the result of the check is negative, we then expand the node. To expand a given node, we generate successor nodes adjacent to the current node, and add them to the frontier set. Note that if these successor nodes are already in the frontier, or have already been visited, then they should not be added to the frontier again.

This describes the life-cycle of a visit, and is the basic order of operations for search agents in this assignment—(1) remove, (2) check, and (3) expand. In this assignment, we will implement algorithms as described here. Please refer to lecture notes for further details, and review the lecture pseudocode before you begin the assignment.

## To Run
To run the code, execute the driver like so (bfs for breadth-first, dfs for depth-first, ast for a-star):

```python
python3 driver.py bfs 1,2,5,3,4,0,6,7,8
python3 driver.py dfs 1,2,5,3,4,0,6,7,8
python3 driver.py ast 1,2,5,3,4,0,6,7,8
```
