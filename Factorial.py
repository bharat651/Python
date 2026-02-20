def compute_factorial(n):
    if(n==0):
        return 1
    else:
        return n*compute_factorial(n-1) #recursive call to compute_factorial function


num = int(input()) #input (4)
# Call the compute_factorial function
result=compute_factorial(num)
print(result)