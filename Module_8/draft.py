try:
    for i in range (-5, 5):
        print(10/i)
except (SyntaxError):
    print('допиши код')
except ZeroDivisionError:
    print('на ноль делить нельзя')
