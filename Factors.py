'''

Welcome to GDB Online.
GDB online is an online compiler and debugger tool for C, C++, Python, Java, PHP, Ruby, Perl,
C#, VB, Swift, Pascal, Fortran, Haskell, Objective-C, Assembly, HTML, CSS, JS, SQLite, Prolog.
Code, Compile, Run and Debug online from anywhere in world.

'''


# Python Program to find the factors of a number

# This function computes the factor of the argument passed
def print_factors(x):
   print("The factors of",x,"are:")
   for i in range (1,x+1):
       if x % i == 0:
           print(i)
num = int(input("entet the number:"))
print_factors(num)
