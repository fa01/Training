# Complete the squares function below.
def squares(a, b):
    result = 0
    for number in range(a, b + 1):
        print('number = ', number)
        temp = math.sqrt(number)
        print('temp = ', round(temp, 1))
        print('temp**2 = ', temp**2)
        if(temp**2 == number):
            print('this number is a square within range = ', number)
            result += 1
    return result
