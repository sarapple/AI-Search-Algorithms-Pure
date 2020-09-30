import math

from utilities import Utilities
from puzzle_state import PuzzleState

def test_goal_state_check_success():
  config = [0, 1, 2, 3, 4, 5, 6, 7, 8]
  size = int(math.sqrt(len(config)))
  result = Utilities.goal_state_check(PuzzleState(config, size))
  assert result == True

def test_goal_state_check_not_success():
  config = [0, 1, 2, 4, 3, 5, 6, 7, 8]
  size = int(math.sqrt(len(config)))
  result = Utilities.goal_state_check(PuzzleState(config, size))
  assert result == False

def test_hashed_state():
  config = [0, 1, 2, 4, 3, 5, 6, 7, 8]
  size = int(math.sqrt(len(config)))
  result = Utilities.hashed_state(PuzzleState(config, size))
  assert result == '0,1,2,4,3,5,6,7,8'

def test_expand():
  config = [1, 2, 5, 3, 4, 0, 6, 7, 8]
  size = int(math.sqrt(len(config)))
  puzzle_state = PuzzleState(config, size)
  result = Utilities.expand(puzzle_state, Utilities.hashed_state(puzzle_state))
  first_child_direction, first_child_state = result[0]
  second_child_direction, second_child_state = result[1]
  third_child_direction, third_child_state = result[2]

  assert first_child_direction == "Up"
  assert second_child_direction == "Down"
  assert third_child_direction == "Left"

  assert first_child_state.config == (1, 2, 0, 3, 4, 5, 6, 7, 8)
  assert second_child_state.config == (1, 2, 5, 3, 4, 8, 6, 7, 0)
  assert third_child_state.config == (1, 2, 5, 3, 0, 4, 6, 7, 8)

def test_compute_manhattan_distance_zero():
  config = [0, 1, 2, 3, 4, 5, 6, 7, 8]
  size = int(math.sqrt(len(config)))
  puzzle_state = PuzzleState(config, size)
   
  result = Utilities.compute_manhattan_distances(puzzle_state)
  assert result == 0

def test_compute_manhattan_distance_one():
  config = [3, 1, 2, 0, 4, 5, 6, 7, 8]
  size = int(math.sqrt(len(config)))
  puzzle_state = PuzzleState(config, size)

  result = Utilities.compute_manhattan_distances(puzzle_state)
  assert result == 1

def test_compute_manhattan_distance_all():
  config = [8, 7, 6, 5, 4, 3, 2, 1, 0]
  size = int(math.sqrt(len(config)))
  puzzle_state = PuzzleState(config, size)

  result = Utilities.compute_manhattan_distances(puzzle_state)
  assert result == 20
