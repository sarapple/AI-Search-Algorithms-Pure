import time

class Utilities:
  @staticmethod
  def get_current_time():
    return time.clock()
  
  @staticmethod
  def expand(state, state_hash):
    return state.expand()
  
  @staticmethod
  def goal_state_check(state):
    tile_runner = 0
    is_sequential = True

    while (is_sequential and tile_runner < 9):
      if (state.config[tile_runner] is not tile_runner):
        is_sequential = False
      
      tile_runner += 1

    return is_sequential

  @staticmethod
  def hashed_state(state):
    return ",".join(map(str, state.config))

  @staticmethod
  def compute_state_cost(state, state_hash):
    return Utilities.compute_manhattan_distances(state)

  @staticmethod
  def compute_manhattan_distances(state):
    config = state.config
    combined_distances = 0
    current_config_matrix = [
      [config[0], config[1], config[2]],
      [config[3], config[4], config[5]],
      [config[6], config[7], config[8]],
    ]
    expected_config = [
      (0, 0), (0, 1), (0, 2),
      (1, 0), (1, 1), (1, 2),
      (2, 0), (2, 1), (2, 2),
    ]

    for row_idx, row in enumerate(current_config_matrix):
      for column_idx, tile in enumerate(row):
        if (tile is 0):
          continue
        
        (expected_row, expected_column) = expected_config[tile]
        if expected_row == row_idx and expected_column == column_idx:
          continue

        combined_distances += abs(row_idx - expected_row) + abs(column_idx - expected_column)

    return combined_distances
