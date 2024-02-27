

def degreetoradians(degree):
    
    radian = degree * 3.14 / 180

    return radian

inputdegree = int(input()) 
print(degreetoradians(inputdegree))


def trapezoidarea(height, first, second):

    area = (first + second) * height/2

    return area


inputheight = int(input())
inputfirst = int(input())
inputsecond = int(input())
print(trapezoidarea(inputheight, inputfirst, inputsecond))


def polygonarea(n, side):
    import math

    ctgargue = 3.14159 / n
    ctg = 1/ math.tan(ctgargue)
    side = side ** 2
    area = n * side * ctg / 4

    return area

n = int(input())
side = int(input())
print(polygonarea(n, side))


def polygonarea(length, height):

    area = length * height

    return area

length = int(input())
height = int(input())
print(polygonarea(length, height))