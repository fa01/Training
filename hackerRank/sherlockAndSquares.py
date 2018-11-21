# Complete the squares function below.
import math

def squares(a, b):
    result = 0
    return math.floor(math.sqrt(b)) - math.ceil(math.sqrt(a)) + 1
    # for number in range(a, b + 1):
    #     print('number = ', number)
    #     temp = math.sqrt(number)
    #     if(number % temp == 0):
    #         result += 1
    # print('temp = ', temp)
    # print('ROUND temp**2 = ', round(temp, 2))
    # rounded = round(temp, 2)
    # if(rounded**2 == number):
    #     print('number IS square = ', number)
    #     result += 1
    # return result
