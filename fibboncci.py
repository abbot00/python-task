def fib (n):
    if (n == 0) or (n ==1):
        return n
       
    else:
         return fib(n-1) + fib(n-2)
     
#ask the user how many numbers they want
     
n = int(input("how many fib numbers: "))
#loop while calling for each new number
m = 0
while m <= n:
    print(fib(m), end=', ')
    m += 1
   
