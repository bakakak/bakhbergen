import re

#ex 1
def text(list_word):
    for word in list_word:
        valid = re.compile(r'ab*', re.IGNORECASE)
        check = valid.findall(word)
        if check:
            print(word.strip(),"=", end=" ", sep="")
            print(check)

#ex 2
def text2(list_word):
    for word in list_word:
        valid = re.compile(r'ab{2,3}', re.IGNORECASE)
        check = valid.findall(word)
        if check:
            print(word.strip(),"=", end=" ", sep="")
            print(check)

#ex 3
def score(list_word):
    for word in list_word:
        valid = re.compile(r'[a-z]+_+[a-z]+')
        check = valid.findall(word)
        if check:
            print(word.strip(),"=", end=" ", sep="")
            print(check)

#ex 4
def uppercase(list_word):
    for word in list_word:
        valid = re.compile(r'[A-Z][a-z]+')
        check = valid.findall(word)
        if check:
            print(word.strip(),"=", end=" ", sep="")
            print(check)

#ex 5
def any(list_word):
    for word in list_word:
        valid = re.compile(r'a[\W|\w]*b')
        check = valid.findall(word)
        if check:
            print(word.strip(),"=", end=" ", sep="")
            print(check)

#ex 6
def to(list_word):
    for word in list_word:
        find = re.compile(r'[ |,|.]')
        result = re.sub(find, ':', word)
        print(word.strip(),"=", end=" ", sep="")
        print(result)

#ex 7
def snake(list_word):
    for word in list_word:
        snake = re.compile(r'snake')
        valid = snake.findall(word)
        if valid:
            change = re.sub(snake, 'camel', word)
            print(word.strip(),"=", end=" ", sep="")
            print(change)

#ex 8
def split(list_word):
    for word in list_word:
        check = re.findall(r'[A-Z][^A-Z]*', word)
        print(word.strip(),"=", end=" ", sep="")
        print(check)

#ex 9
def insert(list_word):
    for word in list_word:
        find = r'(?<=[a-z])(?=[A-Z])'
        change = re.sub(find,' ', word)
        print(word.strip(),"=", change)

#ex 10
def camel(list_word):
    for word in list_word:
        snake = re.compile(r'camel')
        valid = snake.findall(word)
        if valid:
            change = re.sub(snake, 'snake', word)
            print(word.strip(),"=", end=" ", sep="")
            print(change)



with open("row.txt", "r") as file:
    text1 = file.readlines()

print("1 task")
text(text1)
print("2 task")
text2(text1)
print("3 task")
score(text1)
print("4 task")
uppercase(text1)
print("5 task")
any(text1)
print("6 task")
to(text1)
print("7 task")
snake(text1)
print("8 task")
split(text1)
print("9 task")
insert(text1)
print("10 task")
camel(text1)