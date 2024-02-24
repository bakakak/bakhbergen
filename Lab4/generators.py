#ex 1
def square_nums(N):
    for i in range(1, N+1):
        yield i**2
        
n = int(input("Enter a number: "))
square = square_nums(n)
print(*square )

#ex 2
def evens(N):
    for i in range(1, N+1):
        if i % 2 == 0:
            yield i

n = int(input("Enter a number: "))
even = evens(n)
print(*even, sep = ", ")

#ex 3
def div_three_and_four(N):
    for i in range(1, N+1):
        if i % 3 == 0 and i % 4 == 0:
            yield i
            
n = int(input("Enter a number: "))
divisiable_nums = div_three_and_four(n)
print(*divisiable_nums, sep = ", ")

#ex 4
def sqab(N, M):
    for i in range(N, M+1):
        yield i**2

n = int(input("Enter a number: "))
m = int(input("Enter a number: "))
sq_ab = sqab(n, m)
print(*sq_ab, sep = ", ")

#ex 5
def rev_lsit(N):
    for i in range(N, 0, -1):
        yield i

n = int(input("Enter a number: "))
rev_list = rev_lsit(n)
print(*rev_list, sep = ", ")