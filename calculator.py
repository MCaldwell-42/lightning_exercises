# 1. write a function called add that accepts two arguments and returns their sum
# 1. write a function called subtract that accepts two arguments and returns the difference
# 1. write a function called calculate that accepts a function as an argument. In  calculate's body, it should execute that function and pass it the numbers 3 and 5
# 1. print an execution of calculate and pass it a reference to add
# 1. print an execution of calculate and pass it a reference to subtract


def add(x, y):
    ans = x + y
    print(ans)
    return ans


def subtract(x, y):
    ans = x - y
    print(ans)
    return ans

def calculate(funky):
    ans = funky(3, 5)
    return ans

calculate(add)

calculate(subtract)