

def squares(n):

    for i in range(n):
        yield i ** 2
    
    
result_list = list(squares(10))
print(result_list)

def newsquares(n):

    for i in range(0, n, 2):
        yield i ** 2
    
inputnum = int(input())  
result_list = list(newsquares(inputnum))
print(*result_list, sep=', ')

def thirdsquares(n):
    for i in range(n):
        if i % 3 == 0 or i % 4 == 0:
            yield i ** 2


inputnum = int(input())
result_list = list(thirdsquares(inputnum))
print(*result_list, sep=', ')


def atobsqares(a, b):
    for i in range(a, b):
        yield i ** 2


inputnum1 = int(input())
inputnum2 = int(input())
result_list = list(atobsqares(inputnum1, inputnum2))
for num in result_list:
    print(f"{num} ")


def newlist(n):
    yield from range(n)

inputnum = int(input())
result_list = list(newlist(inputnum))
print(*result_list, sep=', ')
