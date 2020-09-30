from puzzle_state import PuzzleState 
from node import Node
from utilities import Utilities

import queue as q
import resource
import itertools

class Algorithms:
  @staticmethod
  def search_wrapper(
    client_defined_expand,
    client_defined_goal_state_check,
    client_defined_hashed_state,
    client_defined_compute_state_cost = None,
    start_state_hash = None,
    start_state = None,
    search_type = "bfs",
    debug = False
  ):
    results = {
      "path_to_goal": None,
      "cost_of_path": 0,
      "nodes_expanded": 0,
      "search_depth": 0,
      "max_search_depth": 0,
      "running_time": 0,
      "max_ram_usage": 0
    }

    def update_stats(max_search_depth = None, increment_expanded = False):
      if (max_search_depth is not None and results["max_search_depth"] < max_search_depth):
        results["max_search_depth"] = max_search_depth

      if (increment_expanded == True):
        results["nodes_expanded"] += 1

    # Wrapper to generate node
    def generate_node(node_options):
      return Node(**node_options)

    # Wrap the client_defined_expand and add stats
    def expand_with_stats(state, state_hash):
      children = client_defined_expand(state, state_hash)

      return children

    # Wrapper to track the cost (heuristic) of a given node -- only applicable in A-Star
    def compute_state_cost(state, state_hash):
      if (client_defined_compute_state_cost is not None):
        return client_defined_compute_state_cost(state, state_hash)
      else:
        return 1

    start_time = Utilities.get_current_time()

    node_solution = Algorithms.search(
      expand = expand_with_stats,
      goal_state_check = client_defined_goal_state_check,
      hashed_state = client_defined_hashed_state,
      generate_node = generate_node,
      compute_state_cost = compute_state_cost,
      update_stats = update_stats,
      start_state_hash = start_state_hash,
      start_state = start_state,
      search_type = search_type,
      debug = debug,
    )

    if (node_solution is not None):
      results["path_to_goal"] = Algorithms.get_node_path_to_root(node_solution)
      results["search_depth"] = len(results["path_to_goal"])
      results["cost_of_path"] = node_solution.cost

    end_time = Utilities.get_current_time()

    results["running_time"] = end_time - start_time
    max_ram_usage_in_bytes = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss # in bytes
    results["max_ram_usage"] = max_ram_usage_in_bytes / 1000000

    return results

  @staticmethod
  def get_node_path_to_root(node_solution):
    path_to_goal = []

    # Determine how to find the pathway from root to node using .parent and directions to get there
    while (node_solution.parent):
      path_to_goal.append(node_solution.direction)
      node_solution = node_solution.parent

    path_to_goal.reverse()

    return path_to_goal

  @staticmethod
  def get_queue(search_type = "bfs"):
    if (search_type == "bfs"):
      return q.Queue()
    elif (search_type == "dfs"):
      return q.LifoQueue()
    elif (search_type == "astar"):
      return q.PriorityQueue()
    else:
      return q.Queue()

  @staticmethod
  def add_to_queue(queue, frontier, node, astar_data = None):
    frontier.add(node.state_hash)

    if (astar_data == None):
      queue.put(node)
    else:
      queue.put((astar_data["heuristic_cost"], astar_data["counter"], node))

  @staticmethod
  def get_children(expand, state, state_hash, reverse = False):
    # Provide the state to the client so they can expand the children (should be tuples of direction and child state)
    children = expand(state, state_hash)

    # dfs uses a stack, so we want the first child to be at the top of the stack, to do this we reverse
    if (reverse == True):
      children.reverse()

    return children

  @staticmethod
  def search(
    expand,
    goal_state_check,
    hashed_state,
    generate_node,
    compute_state_cost,
    update_stats,
    start_state_hash = None,
    start_state = None,
    debug = False,
    search_type = "bfs"
  ):
     # start condition, start the queue and add the root node
    queue = Algorithms.get_queue(search_type)

    # track explored nodes
    explored = set()

    # frontier (reflects members in the queue, but added for performance for membership checking O(1))
    frontier = set()

    # counter needed for python priority queue
    counter = itertools.count()

    start_node = generate_node({
      "state_hash": start_state_hash,
      "state": start_state,
      "direction": None,
      "parent": None,
      "cost": 0,
      "depth": 0
    })

    astar_data = {
      "heuristic_cost": 0,
      "counter": next(counter)
    } if search_type == "astar" else None

    Algorithms.add_to_queue(
      queue = queue,
      frontier = frontier,
      node = start_node,
      astar_data = astar_data
    )

    while (queue.empty() is False):
      # pop the next node off the queue
      parent_node = queue.get()
            
      # astar needs unpacking because it comes with cost
      if (search_type == "astar"):
        (_, _, parent_node) = parent_node

      explored.add(parent_node.state_hash)
      frontier.remove(parent_node.state_hash)

      # if goal condition is found, then return it
      if (goal_state_check(parent_node.state) == True):
        return parent_node

      # Provide the state to the client so they can expand the children
      # this should be tuples of direction (or any other means of splitting branches) and child state
      children = Algorithms.get_children(expand, parent_node.state, parent_node.state_hash, reverse = (search_type == "dfs"))
      update_stats(increment_expanded = True)

      # expand all children and add each to the queue
      for direction, child_state in children:
        state_hash = hashed_state(child_state)
        
        child_node = generate_node({
          "state_hash": state_hash,
          "state": child_state,
          "direction": direction,
          "parent": parent_node,
          "depth": parent_node.depth + 1,
          "cost": parent_node.cost + 1,
        })

        if (state_hash in explored or state_hash in frontier):
          continue

        update_stats(max_search_depth = child_node.depth) 

        astar_data = {
          "heuristic_cost": parent_node.cost + compute_state_cost(child_state, state_hash),
          "counter": next(counter)
        } if search_type == "astar" else None

        Algorithms.add_to_queue(
          queue = queue,
          frontier = frontier,
          node = child_node,
          astar_data = astar_data
        )

    return None
