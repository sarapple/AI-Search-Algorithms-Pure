class Node:
  def __init__(self, state_hash, state, direction, parent, depth, cost):
    self.state_hash = state_hash # state_hash to puzzle state
    self.state = state # puzzle state
    self.parent = parent
    self.direction = direction
    self.depth = depth
    self.cost = cost
