'''

Welcome to GDB Online.
GDB online is an online compiler and debugger tool for C, C++, Python, Java, PHP, Ruby, Perl,
C#, VB, Swift, Pascal, Fortran, Haskell, Objective-C, Assembly, HTML, CSS, JS, SQLite, Prolog.
Code, Compile, Run and Debug online from anywhere in world.

'''
# single tasking using a single thread
from threading import *
from time import *

#create our own class 
class MyThread:
    #a nethod that perfoms 3 tasks one by one
    def prepareTea(self):
        self.task1()
        self.task2()
        self.task3()
    
    def task1(self):
        print("Boil mil and tea powder for s minutes...", end=" ")
        sleep(5)
        print("Done")
        
    def task2(self):
        print("add sugar and boil for 3 minutes....",end=" ")
        sleep(3)
        print("Done")
        
    def task3(self):
        print("Filter it and serve....",end=" ")
        print("Done")
        
# create an instance to our class

obj = MyThread()

#create a thread and run prepareTea method pf obj
t = Thread(target=obj.prepareTea)
t.start()
