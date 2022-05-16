'''

Welcome to GDB Online.
GDB online is an online compiler and debugger tool for C, C++, Python, Java, PHP, Ruby, Perl,
C#, VB, Swift, Pascal, Fortran, Haskell, Objective-C, Assembly, HTML, CSS, JS, SQLite, Prolog.
Code, Compile, Run and Debug online from anywhere in world.

'''
#check given nunber is positive,negative,zero.
def NumberCheck(a):   
    # Checking if the number is positive  
    if a > 0:   
        print("Number given by you is Positive")   
    # Checking if the number is negative   
    elif a < 0:   
        print("Number given by you is Negative")   
    # Else the number is zero  
    else:   
        print("Number given by you is zero")  
# Taking number from user  
a = float(input("Enter a number as input value: "))  
# Printing result  
NumberCheck(a)
