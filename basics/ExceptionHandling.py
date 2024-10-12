"""
if True:
    raise Exception('raise exception testing')
    """
#assert False
try:
    with open('noSuchFile.txt') as file:
        print(file.readlines())
except FileNotFoundError as e:
    print('No such file present')
    print(e)
    try:
        div = 10/0
    except ArithmeticError:
        print('dont divide by zero')
finally:
    print('done')