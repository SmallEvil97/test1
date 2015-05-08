from Test1py3.function import test_simplicity
try:
    f = open('my_number', 'r')
    number = int(f.read())
except ValueError:
    print("Enter the corrrect number!!!")
else:
    test_simplicity(number)
