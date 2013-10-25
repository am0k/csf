def fib(n):
    a = 0
    b = 1
    while b < n:
        print b,
        a = b
        b = a+b

n = 1337
series = raw_input("Enter 'f' for fibonacci or 's' for sum': ") 

if series == "f":
    fib(n)

elif series == "s":
    total = sum(range(0, 3*n+1, 3))
    print total 
    
else:
    print "Invalid string"

        
