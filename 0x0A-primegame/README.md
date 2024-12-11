Prime Game Challenge

Overview

The Prime Game is a turn-based strategy game played between two players, Maria and Ben, where they choose numbers from a set of integers and remove them along with their multiples. The player unable to make a move loses the game. This project implements a Python function to determine the winner of multiple rounds of this game.

Features

Precomputes prime numbers efficiently using the Sieve of Eratosthenes.

Optimized calculations using cumulative prime counts.

Simulates multiple rounds of the game.

Determines the overall winner between Maria and Ben based on optimal play.

Requirements

Python 3.4.3

Ubuntu 20.04 LTS

Function Prototype

def isWinner(x, nums):
    """
    Determines the winner of each round of the game.

    Args:
        x (int): Number of rounds.
        nums (list): List of integers representing the upper limit for each round.

    Returns:
        str: Name of the player that won the most rounds ("Maria" or "Ben").
             If the winner cannot be determined, return None.
    """

Project Guidelines

All Python files must start with #!/usr/bin/python3.

Files must adhere to PEP 8 style (version 1.7.x).

All files are executable.

A README.md file is mandatory at the root of the project.

Use only allowed editors (vi, vim, emacs).

Project test:

 cat main_0.py
#!/usr/bin/python3

isWinner = __import__('0-prime_game').isWinner


print("Winner: {}".format(isWinner(5, [2, 5, 1, 4, 3])))


Output:
./main_0.py
Winner: Ben
