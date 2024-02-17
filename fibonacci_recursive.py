'''
simple_programming_

This code prints Fibonacci sequence 
using recursive

Result: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, ...
'''
def fibonacci_recursive(n):
    if n == 1:
        return 0
    elif n == 2:
        return 1
    else: 
        v1 = fibonacci_recursive(n - 2)
        v2 = fibonacci_recursive(n - 1)
        return v1 + v2

i = 1
while i <= 10:
    print(fibonacci_recursive(i))
    i+=1


