import os
def ex1():
    path = str(input("Input the path: "))
    print("Directories:")
    for dir in os.listdir(path):
        if os.path.isdir(os.path.join(path, dir)):
            print(dir)
            
    print("Files:")
    for file in os.listdir(path):
        if os.path.isfile(os.path.join(path, file)):
            print(file)
    print("All:")
    for all in os.listdir(path):
        print(all)

def ex2():
    path = str(input('Input the path: '))
    if os.path.exists(path):
        print('The path exists')
        read = os.access(path, os.R_OK)
        if read:
            print('The file is readable')
        else:
            print('The file is not readable')
        write = os.access(path, os.W_OK)
        if write:
            print('The file is writable')
        else:
            print('The file is not writable')
        exe = os.access(path, os.X_OK)
        if exe:
            print('The file is executable')
        else:
            print('The file is not executable')
    else:
        print('The path does not exist')

def ex3():
    path = str(input('Input the path: '))
    if os.path.exists(path):
        print('The path exists')
        path_name = os.path.basename(path)
        path_dir = os.path.dirname(path)
        print('File name is: ', path_name)
        print('File path is: ', path_dir)
    else:
        print('The path does not exists')
      
def ex4():
    path = input("Input the path: ")
    with open(path, 'r') as f:
        lines = f.readlines()
        print('Number of lines in ', len(lines))
        

def ex5():
    path = str(input("Input the path: "))
    with open(path, 'w') as file:
        list = [1, 2, 3, 4, 5, 6, 7, 8]
        file.write('\n'.join(list))
        
def ex6():
    for letter in "abcdefghijklmnopqrstuvwxyz":
        filename = letter + '.txt'
        with open(filename, 'w') as file:
            file.write(letter)

def ex7():
    path = str(input("Input the path: "))
    new_path = str(input("Input the new path: "))
    with open(path, 'rb') as file:
        write = file.read()
    with open(new_path, 'ab') as new_file:
        new_file.write(write)
        

def ex8():
    path = str(input("Input the path: "))
    if os.path.exists(path):
        if os.access(path, os.X_OK):
            os.remove(path)
            print('The file have been deleted')
        else:
            print('This file is not accessiable')
    else:
        print('The file does not exist')

ex1()
ex2()
ex3()
ex4()
ex5()
ex6()
ex7()
ex8()



    
    