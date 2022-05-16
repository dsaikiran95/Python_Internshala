'''

Welcome to GDB Online.
GDB online is an online compiler and debugger tool for C, C++, Python, Java, PHP, Ruby, Perl,
C#, VB, Swift, Pascal, Fortran, Haskell, Objective-C, Assembly, HTML, CSS, JS, SQLite, Prolog.
Code, Compile, Run and Debug online from anywhere in world.

'''

num=10

#factorial of a value through input
#num = int(input("enter the number:"))
factorial = 1
#check if the number is negative,postive,zero.
if num < 0:
    print("Sorry factorial is does not exist for negative number")
elif num == 0:
    print("the factorial of 0 is 1")
else:
    for i in range (1,num+1):
        factorial = factorial*i
    print("The factorial of",num,"is",factorial)    
