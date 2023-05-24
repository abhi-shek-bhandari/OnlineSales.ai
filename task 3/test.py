#here is the function name compute is defined which is taking n as a parameter value
def compute(n):
    #in this if condtion if n is less then 10 then the square of n is calculated and stored in out name variable
    if n < 10:
        out = n ** 2
    #in this else if condition if n is greater than and equal to 20 then the factorial of n-10 is calculated and stored in out name variable 
    elif n <= 20:
        out = 1
        for i in range(1, n-10+1):
            out *= i
    else:
        #and this else condition will only work if both first and second condition is false  and then sum of n-20 is calculated and stored in out name variable 
        out = 0
        for i in range(1,n-20+1):
            out += i

    # here the out var is printed after performing the calculations
    print(out)


n = int(input("Enter an integer: "))
compute(n)