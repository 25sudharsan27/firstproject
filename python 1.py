import random
a=int(input("Enter smaller number: "))
b=int(input("Enter greater number: "))
if a<=b:
    value = (random.randint(a,b))
    print(value)
    if value>0:
        print(value,"is a positive number")
    if value < 0:
        print(value ,"is negative number")
    if value%2==0:
        print(value,"is even number")
    if value%2!=0:
        print(value,"is odd number")
    if value==0:

        print(value,"is neither prime nor composite")
        print(value,"is neither negative nor positive")
    elif value == 1:
        print(value,"Neither prime nor composite" )
    else:
        for divisor in range(2,(value//2)+1):
            if (value % divisor) ==0:
                print(value,"is Composite number")
                break
        else:
            print(value,"is prime number")
else:
    print("Greater number must be greater than or equal to Smaller number")