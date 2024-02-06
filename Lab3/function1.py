# ex 1
def gram(grams):
    ounces = 28.3495231 * grams
    print(ounces)
# ex 2
def far(f):
    c=(5/9)*(f-32)
    return c
# ex 3
def solve(numheads, numlegs):
    rabbit=(numlegs-2*numheads)/2
    chicken=numheads-rabbit
    print("rabbit = ", rabbit, "chicken = ", chicken)
# ex 4
import math
def filter_prime(list):
    li=[]
    for i in list:
        j=2
        while(j<=math.sqrt(i)):
            if(i/j==int(i/j)):
                j=0
                break
            j=j+1
        if (j!=0):
            li.append(i)
    return li
# ex 5
from itertools import permutations 
def permut(str):
    a=permutations(str) 
    for i in list(a): 
        print("".join(i)) 
# ex 6
def revers(str):
    s=""
    se=""
    for i in str:
        if(i!=" " and i!=str[-1]):
            s=s+i
        elif(i!=str[-1]):
            se=se+s+" "
            s=""
        else:
            se=se+s+i
    return se
# ex 7
def has_33(nums):
    f=False
    for i in range(len(nums)-1):
        if (nums[i]==3 and nums[i+1]==3):
            f=True
            break
    return f
# ex 8
def spy_game(nums):
    c=0
    f=False
    for i in range(len(nums)):
        if (nums[i]==0 and c==0):
            c=1
        if (nums[i]==0 and c==1):
            c=2
        if (nums[i]==7 and c==2):
            f=True
    return f
# ex 9
import math
def vol(a):
    vo=4*3.14*pow(a,3)/3
    return vo
# ex 10
def unique(lis):
    li=[]
    for i in lis:
        if i not in li:
            li.append(i)
    return li
# ex 11
def palin(str):
    for i in range(len(str)):
        if(str[i]!=str[-1-i]):
            return False
    return True
# ex 12
def histogram(nums):
    for i in nums:
        print("*"*i)
# ex 13
import random
def game():
    num=random.randint(1, 20)
    b=1
    print("Hello! What is your name?")
    name=input()
    print("Well, "+name +", I am thinking of a number between 1 and 20.")
    number=int(input())
    while(num!=number):
        if num > number:
            b=b+1
            print("Your guess is too low.\nTake a guess.")
            number=int(input())
        elif num < number:
            b=b+1
            print("Your guess is too high.\nTake a guess.")
            number=int(input())
    print("Good job, ",name,"! You guessed my number in ",b," guesses!",num)
game()

