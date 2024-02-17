'''
simple_programming_

This code prints Fibonacci sequence 
using simple loop

Result: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, ...
'''
def fibonacci_loop(n):
    f1 = 0 # first number of sequence 
    f2 = 1 # second number of sequence 
    i = 1 # loop index
    v1 = f1 
    v2 = f2
    while i <= n:
        if i == 1:
            v3 = v1
        elif i == 2:
            v3 = v2
        else:
            v3 = v1 + v2
            # swap the values
            v1 = v2
            v2 = v3 
        i+=1
    return v3

i = 1
while i <= 10:
    print(fibonacci_loop(i))
    i+=1

