def mul(*args):
    num1 = 1
    for num in args:
        num1*=num
    print(num1)

mul(3,4,2,5)