minOperations Project
Description
The minOperations function is designed to calculate the fewest number of operations needed to produce exactly n characters H in a text editor that supports only two operations:

Copy All: Copies all the characters currently in the text file.
Paste: Pastes the copied characters.
Problem Statement
Given a single character H in a text file, you can only perform the following operations:

Copy All: Copies all the characters present in the text file.
Paste: Pastes the last copied characters into the text file.
The objective is to determine the minimum number of operations required to achieve exactly n H characters in the text file. If n is impossible to achieve, return 0.

Example
For n = 9, the function should return 6 because the minimal sequence of operations is:

H (1 character)
Copy All (1 operation)
Paste (2 operations) → HH
Paste (3 operations) → HHH
Copy All (4 operations)
Paste (5 operations) → HHHHHH
Paste (6 operations) → HHHHHHHHH
Total number of operations: 6

Requirements
To successfully run the minOperations project, you should have:

Python 3.6 or above: The code is written in Python, and you need this version or higher to execute it.
Understanding of basic programming concepts: Familiarity with loops, conditions, and functions is essential.
Knowledge of the following key concepts:
Dynamic Programming: A method for solving complex problems by breaking them down into simpler subproblems and storing the results to avoid redundant calculations.
Prime Factorization: The process of determining the prime numbers that multiply together to give the original number, which helps in identifying the optimal way to reach the desired count of characters.
Code Optimization: Techniques to improve the performance of the code, making it faster and more efficient.
Greedy Algorithm: A problem-solving strategy that makes the locally optimal choice at each step with the hope of finding a global optimum. In this case, we use the smallest divisors to minimize the number of operations.

Prime Factorization: By checking each divisor up to the target number, we effectively factor the number, ensuring that we’re using the least number of operations.
Code Optimization: The implementation avoids unnecessary calculations by breaking out of loops when divisibility fails, improving efficiency.
Greedy Algorithm: The algorithm takes the smallest divisor at each step, ensuring that the total number of operations is minimized.
Why Use Divisors?
For each divisor, we simulate the process of:
Copy All: Copying the existing H characters.
Paste: Pasting multiple times to reach a higher count.
Adding the divisor to operations reflects how many steps are required to use that factor.
Edge Cases
n < 1: The function should return 0 as it’s impossible to create zero or negative characters.
n = 1: No operations are required since the single H already exists.
n as a prime number: For prime numbers, the minimal operations will involve only copying once and pasting multiple times, reflecting the number itself.