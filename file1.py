def add(*args):
    print(sum(args))

def sub(*args):
    num1 = args[0]
    for num in args:
        num-=num1
    print(num)

