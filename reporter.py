class Reporter:
  @staticmethod
  def write_output(
    path_to_goal,
    cost_of_path,
    nodes_expanded,
    search_depth,
    max_search_depth,
    running_time,
    max_ram_usage,
    file_name
  ):
    f = open(file_name, "w+")
    f.write(
      ""
      # path_to_goal: the sequence of moves taken to reach the goal
      + "path_to_goal: {path_to_goal}".format(path_to_goal = path_to_goal)
      + "\n"
      # cost_of_path: the number of moves taken to reach the goal
      + "cost_of_path: {cost_of_path}".format(cost_of_path = cost_of_path)
      + "\n"
      # nodes_expanded: the number of nodes that have been expanded
      + "nodes_expanded: {nodes_expanded}".format(nodes_expanded = nodes_expanded)
      + "\n"
      # search_depth: the depth within the search tree when the goal node is found
      + "search_depth: {search_depth}".format(search_depth = search_depth)
      + "\n"
      # max_search_depth:  the maximum depth of the search tree in the lifetime of the algorithm
      + "max_search_depth: {max_search_depth}".format(max_search_depth = max_search_depth)
      + "\n"
      # running_time: the total running time of the search instance, reported in seconds
      + "running_time: {running_time:.8f}".format(running_time = running_time)
      + "\n"
      # max_ram_usage: the maximum RAM usage in the lifetime of the process as measured by the ru_maxrss attribute in the resource module, reported in megabytes
      + "max_ram_usage: {max_ram_usage:.8f}".format(max_ram_usage = max_ram_usage)
    )

    f.close()
