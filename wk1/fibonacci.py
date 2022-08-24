"""
The goal of this algorithm is to compute the nth number of the Fibonacci sequence with Dynamic Programming
*taking the first two numbers as 0 and 1
Fn = Fn-1 + Fn-2
"""

stored_fibonacci_array = [0, 1]


def get_int():
    nth = int(input("Will accept a positive integer: \n"))
    if nth < 0:
        print("C'mon, let's not be annoying. ")
        get_int()

    elif nth == 0:
        return 0

    elif nth == 1 or nth == 2:
        return 1

    else:
        return nth


def fibonacci(n=None):
    if n < len(stored_fibonacci_array):
        return stored_fibonacci_array[n]

    else:
        temp = fibonacci(n-1) + fibonacci(n-2)
        stored_fibonacci_array.append(temp)
        return stored_fibonacci_array[n]


if __name__ == "__main__":
    print("Fibonacci ")
    num = get_int()
    nth_fibonacci_number = fibonacci(num)
    print("Position " + str(num) + " in the Fibonacci sequence is " + str(nth_fibonacci_number) + ".")
