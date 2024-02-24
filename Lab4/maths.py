import math 

#ex 1
degree = int(input("Enter a degree: "))
radian = math.radians(degree)
print(round(radian, 6)) 

#ex 2
def trapizode(height, fist, second):
    area = height * (fist + second) / 2
    print(area)
    
height = 5
first = 5
second = 6
trapizode(height, first, second)


#ex 3
def polygon_area(sides, length):
    area = (sides * pow(length, 2))/(4*math.tan(math.pi/sides))
    print(round(area))
    
sides = 4
length = 25
polygon_area(sides, length)

#ex 4
def parallelogram_area(base, height):
    area = base * height
    print(float(area))

base = 5
height = 6
parallelogram_area(base, height)