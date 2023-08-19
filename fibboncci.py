def fib (n):
    if (n == 0) or (n ==1):
        return n
       
    else:
         return fib(n-1) + fib(n-2)
n = 0
while n <= 20:
    print(fib(n), end=', ')
    n += 1
