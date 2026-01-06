def fib(i):
    a=0
    b=1
    c=0
    j=1
    while j<=i:
        c= a+b
        a=b
        b=c
        j=j+1
    return a

print(fib(9))