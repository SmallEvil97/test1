def test_simplicity(n):
    if n <= 0:
        print("enter the correct number!!!")  
    elif n == 1:
        print("ONE. has one divider (exception)!")  
    else:
        d = 2
        while n % d:
            d += 1
        if n == d:
            print("is a prime number!")
        else:
            print("is the number of composite!")
