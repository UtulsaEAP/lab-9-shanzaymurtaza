def fibonacci(n):
    if n < 0:
        return -1
    elif n == 0:
        return 0 
    elif n == 1:
        return 1 
    else:
        fib_sequence = [0,1]
        for i in range(2, n +1):
            fib_sequence.append(fib_sequence[i - 1] + fib_sequence[i - 2])
        return fib_sequence[n]
    

if __name__ == '__main__':
    start_num = int(input())
    print(f'fibonacci({start_num}) is {fibonacci(start_num)}')