def fib(n):
    a = 0
    b = 1
    while b < n:
        print b,
        a = b
        b = a+b


n = 7
series = "sum"



if series == "fibonacci":
    fib(n)

elif series == "sum":
    sum(n)



        
        
# print fib(2000)

        