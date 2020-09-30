import math

from utilities import Utilities
from puzzle_state import PuzzleState
from algorithms import Algorithms
from node import Node

def test_bfs_1():
  config = [1, 2, 5, 3, 4, 0, 6, 7, 8]
  size = int(math.sqrt(len(config)))
  puzzle_state = PuzzleState(config, size)
  start_state_hash = Utilities.hashed_state(puzzle_state)
  start_state = puzzle_state

  def generate_node(node_options):
    return Node(**node_options)

  def compute_state_cost(state, state_hash):
    return 1

  def update_stats(max_search_depth = None, increment_expanded = False):
    pass

  result = Algorithms.search(
    expand = Utilities.expand,
    goal_state_check = Utilities.goal_state_check,
    hashed_state = Utilities.hashed_state,
    compute_state_cost = compute_state_cost,
    update_stats = update_stats,
    generate_node = generate_node,
    start_state_hash = start_state_hash,
    start_state = start_state,
    search_type = "bfs"
  )

  assert result.state.config == (0, 1, 2, 3, 4, 5, 6, 7, 8)

def test_bfs_wrapper_1():
  config = [1, 2, 5, 3, 4, 0, 6, 7, 8]
  size = int(math.sqrt(len(config)))
  puzzle_state = PuzzleState(config, size)
  start_state_hash = Utilities.hashed_state(puzzle_state)
  start_state = puzzle_state

  result = Algorithms.search_wrapper(
    client_defined_expand = Utilities.expand,
    client_defined_goal_state_check = Utilities.goal_state_check,
    client_defined_hashed_state = Utilities.hashed_state,
    start_state_hash = start_state_hash,
    start_state = start_state,
    search_type = "bfs"
  )

  assert result["path_to_goal"] == ["Up", "Left", "Left"]
  assert result["cost_of_path"] == 3
  assert result["search_depth"] == 3
# #   assert result["running_time"] < 0.002
# #   # assert result["max_ram_usage"] < 0.08 # look into why this is 100x worse

def test_bfs_wrapper_2():
  config = [6, 1, 8, 4, 0, 2, 7, 3, 5]
  size = int(math.sqrt(len(config)))
  puzzle_state = PuzzleState(config, size)
  start_state_hash = Utilities.hashed_state(puzzle_state)
  start_state = puzzle_state

  result = Algorithms.search_wrapper(
    client_defined_expand = Utilities.expand,
    client_defined_goal_state_check = Utilities.goal_state_check,
    client_defined_hashed_state = Utilities.hashed_state,
    start_state_hash = start_state_hash,
    start_state = start_state,
    search_type = "bfs"
  )

  assert result["path_to_goal"] == [
    'Down',
    'Right',
    'Up',
    'Up',
    'Left',
    'Down',
    'Right',
    'Down',
    'Left',
    'Up',
    'Left',
    'Up',
    'Right',
    'Right',
    'Down',
    'Down', 
    'Left',
    'Left',
    'Up',
    'Up'
  ]
  assert result["cost_of_path"] == 20
  assert result["nodes_expanded"] == 54094
  assert result["search_depth"] == 20
  assert result["max_search_depth"] == 21

def test_bfs_wrapper_3():
  config = [8, 6, 4, 2, 1, 3, 5, 7, 0]
  size = int(math.sqrt(len(config)))
  puzzle_state = PuzzleState(config, size)
  start_state_hash = Utilities.hashed_state(puzzle_state)
  start_state = puzzle_state

  result = Algorithms.search_wrapper(
    client_defined_expand = Utilities.expand,
    client_defined_goal_state_check = Utilities.goal_state_check,
    client_defined_hashed_state = Utilities.hashed_state,
    start_state_hash = start_state_hash,
    start_state = start_state,
    search_type = "bfs"
  )

  assert result["path_to_goal"] == ['Left', 'Up', 'Up', 'Left', 'Down', 'Right', 'Down', 'Left', 'Up', 'Right', 'Right', 'Up', 'Left', 'Left', 'Down', 'Right', 'Right', 'Up', 'Left', 'Down', 'Down', 'Right', 'Up', 'Left', 'Up', 'Left']
  assert result["cost_of_path"] == 26
  assert result["nodes_expanded"] == 166786
  assert result["search_depth"] == 26
  assert result["max_search_depth"] == 27

# Depth first search tests

def test_dfs_1():
  config = [1, 2, 5, 3, 4, 0, 6, 7, 8]
  size = int(math.sqrt(len(config)))
  puzzle_state = PuzzleState(config, size)
  start_state_hash = Utilities.hashed_state(puzzle_state)
  start_state = puzzle_state

  def generate_node(node_options):
    return Node(**node_options)

  def compute_state_cost(state, state_hash):
    return 1

  def update_stats(max_search_depth = None, increment_expanded = False):
    pass

  result = Algorithms.search(
    expand = Utilities.expand,
    goal_state_check = Utilities.goal_state_check,
    hashed_state = Utilities.hashed_state,
    compute_state_cost = compute_state_cost,
    update_stats = update_stats,
    generate_node = generate_node,
    start_state_hash = start_state_hash,
    start_state = start_state,
    search_type = "dfs"
  )

  assert result.state.config == (0, 1, 2, 3, 4, 5, 6, 7, 8)

def test_dfs_wrapper_1():
  config = [1, 2, 5, 3, 4, 0, 6, 7, 8]
  size = int(math.sqrt(len(config)))
  puzzle_state = PuzzleState(config, size)
  start_state_hash = Utilities.hashed_state(puzzle_state)
  start_state = puzzle_state

  result = Algorithms.search_wrapper(
    client_defined_expand = Utilities.expand,
    client_defined_goal_state_check = Utilities.goal_state_check,
    client_defined_hashed_state = Utilities.hashed_state,
    start_state_hash = start_state_hash,
    start_state = start_state,
    search_type = "dfs"
  )

  assert result["path_to_goal"] == ["Up", "Left", "Left"]
  assert result["cost_of_path"] == 3
  assert result["search_depth"] == 3
  assert result["max_search_depth"] == 66125

def test_dfs_wrapper_2():
  config = [6, 1, 8, 4, 0, 2, 7, 3, 5]
  size = int(math.sqrt(len(config)))
  puzzle_state = PuzzleState(config, size)
  start_state_hash = Utilities.hashed_state(puzzle_state)
  start_state = puzzle_state

  result = Algorithms.search_wrapper(
    client_defined_expand = Utilities.expand,
    client_defined_goal_state_check = Utilities.goal_state_check,
    client_defined_hashed_state = Utilities.hashed_state,
    start_state_hash = start_state_hash,
    start_state = start_state,
    search_type = "dfs"
  )

  assert result["path_to_goal"][0] == "Up"
  assert result["path_to_goal"][1] == "Left"
  assert result["path_to_goal"][2] == "Down"
  assert result["cost_of_path"] == 46142
  assert result["nodes_expanded"] == 51015
  assert result["search_depth"] == 46142
  assert result["max_search_depth"] == 46142

def test_dfs_wrapper_3():
  config = [8, 6, 4, 2, 1, 3, 5, 7, 0]
  size = int(math.sqrt(len(config)))
  puzzle_state = PuzzleState(config, size)
  start_state_hash = Utilities.hashed_state(puzzle_state)
  start_state = puzzle_state

  result = Algorithms.search_wrapper(
    client_defined_expand = Utilities.expand,
    client_defined_goal_state_check = Utilities.goal_state_check,
    client_defined_hashed_state = Utilities.hashed_state,
    start_state_hash = start_state_hash,
    start_state = start_state,
    search_type = "dfs"
  )

  assert result["path_to_goal"][0] == "Up"
  assert result["path_to_goal"][1] == "Up"
  assert result["path_to_goal"][2] == "Left"
  assert result["cost_of_path"] == 9612
  assert result["nodes_expanded"] == 9869
  assert result["search_depth"] == 9612
  assert result["max_search_depth"] == 9612

def test_astar_wrapper_1():
  config = [6, 1, 8, 4, 0, 2, 7, 3, 5]
  size = int(math.sqrt(len(config)))
  puzzle_state = PuzzleState(config, size)
  start_state_hash = Utilities.hashed_state(puzzle_state)
  start_state = puzzle_state

  result = Algorithms.search_wrapper(
    client_defined_expand = Utilities.expand,
    client_defined_goal_state_check = Utilities.goal_state_check,
    client_defined_hashed_state = Utilities.hashed_state,
    client_defined_compute_state_cost = Utilities.compute_state_cost,
    start_state_hash = start_state_hash,
    start_state = start_state,
    search_type = "astar"
  )

  assert result["path_to_goal"] == ['Down', 'Right', 'Up', 'Up', 'Left', 'Down', 'Right', 'Down', 'Left', 'Up', 'Left', 'Up', 'Right', 'Right', 'Down', 'Down', 'Left', 'Left', 'Up', 'Up']
  assert result["cost_of_path"] == 20
  assert result["nodes_expanded"] == 696
  assert result["search_depth"] == 20
  assert result["max_search_depth"] == 20

def test_astar_wrapper_2():
  config = [8, 6, 4, 2, 1, 3, 5, 7, 0]
  size = int(math.sqrt(len(config)))
  puzzle_state = PuzzleState(config, size)
  start_state_hash = Utilities.hashed_state(puzzle_state)
  start_state = puzzle_state

  result = Algorithms.search_wrapper(
    client_defined_expand = Utilities.expand,
    client_defined_goal_state_check = Utilities.goal_state_check,
    client_defined_hashed_state = Utilities.hashed_state,
    client_defined_compute_state_cost = Utilities.compute_state_cost,
    start_state_hash = start_state_hash,
    start_state = start_state,
    search_type = "astar"
  )

  assert result["path_to_goal"] == ['Left', 'Up', 'Up', 'Left', 'Down', 'Right', 'Down', 'Left', 'Up', 'Right', 'Right', 'Up', 'Left', 'Left', 'Down', 'Right', 'Right', 'Up', 'Left', 'Down', 'Down', 'Right', 'Up', 'Left', 'Up', 'Left']
  assert result["cost_of_path"] == 26
  assert result["nodes_expanded"] == 1585
  assert result["search_depth"] == 26
  assert result["max_search_depth"] == 26
