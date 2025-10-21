#!/usr/bin/env python3

# Fibonacci Sequence Exercise with functions
# TODO: (Read detailed instructions in the Readme file)
def get_positive_integer():

    while True:
        num = input("Please enter a positive integer: ")
        if num.isdigit() and int(num) > 0:
            return int(num)
        else:
            print("Invalid input. Try again.")

def generate_fibonacci(n):
    fib_sequence = []
    a, b = 0, 1
    for _ in range(n):
        fib_sequence.append(a)
        a, b = b, a + b
    return fib_sequence

def print_fibonacci_sequence(seq):
    print("Fibonacci sequence:")
    for num in seq:
        print(num, end=' ')
    print()

num_terms = get_positive_integer()
fibonacci_sequence = generate_fibonacci(num_terms)
print_fibonacci_sequence(fibonacci_sequence)

