"""
The goal of this algorithm is to compute the nth number of the Fibonacci sequence
*starting from 1, instead of 0
"""

def get_int():
    n = input("This recursion algorithm will accept a positive integer as the nth number in the Fibonacci sequence. "
    try:
        n = int(n)
    except:
        n = get_int()

    if n < 0:
        get_int()

    return n

"def fib(n):"