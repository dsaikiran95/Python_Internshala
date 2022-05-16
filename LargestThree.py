'''

Welcome to GDB Online.
GDB online is an online compiler and debugger tool for C, C++, Python, Java, PHP, Ruby, Perl,
C#, VB, Swift, Pascal, Fortran, Haskell, Objective-C, Assembly, HTML, CSS, JS, SQLite, Prolog.
Code, Compile, Run and Debug online from anywhere in world.

'''

num = int(input("enter the number:"))
if num>1:
    #check the factors
    for i in range (2,num):
        if(num % i) == 0:
            print(num,"is not a prime number")
            print(i, "times",num//i, "is",num)
            break
    else:
        print(num,"is a prime number")
