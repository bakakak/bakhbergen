import math
import time

#ex 1
def ex1():
    n = int(input("Input length: "))
    list = []
    for i in range(n):
        list.append(int(input()))
    print(math.prod(list))

#ex 2
def ex2():
    text = str(input("Input the text: "))
    low = sum(1 for letter in text if letter.islower())
    up = sum(1 for letter in text if letter.isupper())
    
    print('Lower case letters: ', low)
    print('Upper case letters: ', up)

#ex 3
def ex3():
    text = str(input("Input the text: "))
    if text == text[::-1]:
        print(text, "is a palindrome")
    else:
        print(text, "is not a palindrome")
    
#ex 4
def ex4():
    num = int(input("Input the number: "))
    mil= int(input("Input the number of miliseconds: "))
    seconds = mil/1000
    
    time.sleep(seconds)
    result = int(math.sqrt(num))
    
    print('The root of ' + num + 'is ' + result + 'after ' + mil + ' miliseconds')

#ex 5
def ex5():
    tup = (True, False, True, False, True)
    false = sum(1 for i in tup if i == False)
    if false > 0:
        return False
    else:
        return True
    


ex1()
ex2()
ex3()
ex4()
ex5()
    