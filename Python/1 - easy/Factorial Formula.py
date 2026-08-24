def factorial(n):
    if n<=1:
        return 1
    else:
        n=n-1
        return (n+1)*factorial(n)