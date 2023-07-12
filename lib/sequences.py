#!/usr/bin/env python3
def print_fibonacci(length):
    fib_sequence = []

    if length == 1:
        fib_sequence.append(0)
        print(fib_sequence)
        return

    if length <= 0:
       
        print(fib_sequence)
        return

    
    fib_1 = 0
    fib_2 = 1

    
    fib_sequence.append(fib_1)
    fib_sequence.append(fib_2)

    
    for i in range(2, length):
        next_fib = fib_1 + fib_2
        fib_sequence.append(next_fib)
        fib_1 = fib_2
        fib_2 = next_fib

    print(fib_sequence)