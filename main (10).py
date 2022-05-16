'''

Welcome to GDB Online.
GDB online is an online compiler and debugger tool for C, C++, Python, Java, PHP, Ruby, Perl,
C#, VB, Swift, Pascal, Fortran, Haskell, Objective-C, Assembly, HTML, CSS, JS, SQLite, Prolog.
Code, Compile, Run and Debug online from anywhere in world.

'''
# Program to display the Fibonacci sequence up to n-th term

nterms = int(input("Enter the terms:"))
# first two terms
n1, n2 = 0, 1
count = 0

if nterms <= 0:
    print("Enter a postive number")
elif nterms == 1:
    print("Fibonacci sequence upto",nterms,":")
    print(n1)
#generate a fibonacci sequence
else:
    print("fibonacci sequence")
    while count < nterms:
        print(n1)
        nth = n1+n2
        #update Values
        n1 = n2
        n2 = nth
        count+=1
    