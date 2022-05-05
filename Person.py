'''

Welcome to GDB Online.
GDB online is an online compiler and debugger tool for C, C++, Python, Java, PHP, Ruby, Perl,
C#, VB, Swift, Pascal, Fortran, Haskell, Objective-C, Assembly, HTML, CSS, JS, SQLite, Prolog.
Code, Compile, Run and Debug online from anywhere in world.

'''
class person:
    
    def __init__(self):
        self.name="Domakonda Sai kiran"
        self.gender="Male"
        self.age=30
    
    
    def talk(self):
        print("Hi iam" , self.name)
        
    def vote(self) :
        if self.age<18 :
            print("iam not eligible for vote")
        else:
            print("Iam eligible to vote")
            
obj= person()
person.talk(obj)
person.vote(obj)

    
