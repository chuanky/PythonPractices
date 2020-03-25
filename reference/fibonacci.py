def fib(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fib(n - 1) + fib(n - 2)

if __name__ == '__main__':
    msg = ""
    while msg != "quit":
        msg = input("你想知道Fibonacci数列的第几位? ")
        print(fib(int(msg)))
