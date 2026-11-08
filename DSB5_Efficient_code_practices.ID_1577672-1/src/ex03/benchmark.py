import timeit
import sys
from functools import reduce

def use_loop(n):
    sum = 0
    for i in range(1, n+1):
        sum = sum + i*i
    return sum

def use_reduce(n):
    return reduce(lambda x, i: x + i*i, range(1, n+1), 0)

def main():
    if len(sys.argv)!=4:
        raise Exception('must be 4 arguments')

    func = sys.argv[1]
    num_of_steps = int(sys.argv[2])
    n = int(sys.argv[3])
    if num_of_steps <= 0 or n <= 0:
        raise Exception('must be > 0')
    
    functions  = {
        'loop': use_loop,
        'reduce': use_reduce,
    }

    if func not in functions:
        raise Exception('incorrect function name')
    
    res = timeit.timeit(lambda: functions[func](n), number=num_of_steps)
    print(use_loop(3))
    print(use_reduce(3))
    print(res)

if __name__ == '__main__':
    main()