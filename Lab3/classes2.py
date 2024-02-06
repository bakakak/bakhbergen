# ex 1
class String1():
    def getString(self):
        self.str=input()
    def printString(self):
        print(self.str)
# ex 2
class Shape():
    def __init__(self):
        self.ar=0
    def area(self):
        print(self.ar)
class Square(Shape):
    def __init__(self,length):
        self.length=length
        self.ar=length*length
# ex 3
class Rectangle(Shape):
    def __init__(self,length,width):
        self.length=length
        self.width=width
        self.ar=length*width
# ex 4
import math
class Point():
    def __init__(self,x,y):
        self.x=x
        self.y=y
    def show(self):
        print("x=",self.x," y=",self.y)
    def move(self):
        self.x=self.x+5
        self.y=self.y-5
    def dist(self,x1,y1):
        print(math.sqrt(pow(x1-self.x,2)+pow(y1-self.y,2)))
# ex 5
class Account():
    def __init__(self,owner,balance):
        self.owner=owner
        self.balance=balance
    def deposit(self,bal):
        self.balance=self.balance+bal
        print("the balance is topped up on",bal,"\n it is available to you", self.balance)
    def withdraw(self,bal):
        if(self.balance>=bal):
            self.balance=self.balance-bal
            print("you have withdrawn from the account",bal,"\n it is available to you", self.balance)
        else:
            print("You don't have enough funds","\n it is available to you",self.balance)
p1=Account("Bakhbergen",500000)
p1.deposit(20000)
p1.withdraw(200000)
p1.withdraw(400000)
print(p1.owner)
# ex 6

