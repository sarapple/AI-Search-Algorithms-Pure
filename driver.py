import queue as Q

import time

import resource

import sys

import math

from puzzle_state import PuzzleState
from algorithms import Algorithms
from utilities import Utilities
from reporter import Reporter

def main():

    sm = sys.argv[1].lower()

    begin_state = sys.argv[2].split(",")

    begin_state = tuple(map(int, begin_state))

    size = int(math.sqrt(len(begin_state)))

    hard_state = PuzzleState(begin_state, size)

    args = {
        "client_defined_expand": Utilities.expand,
        "client_defined_goal_state_check": Utilities.goal_state_check,
        "client_defined_hashed_state": Utilities.hashed_state,
        "client_defined_compute_state_cost": Utilities.compute_state_cost,
        "start_state_hash": sm,
        "start_state": hard_state,
    }

    if sm == "bfs":

        result = Algorithms.search_wrapper(
            **args,
            search_type = "bfs"
        )

    elif sm == "dfs":

        result = Algorithms.search_wrapper(
            **args,
            search_type = "dfs"
        )

    elif sm == "ast":

        result = Algorithms.search_wrapper(
            **args,
            search_type = "astar"
        )

    else:

        print("Enter valid command arguments !")
    
    Reporter.write_output(file_name = "output.txt", **result)

if __name__ == '__main__':

    main()
