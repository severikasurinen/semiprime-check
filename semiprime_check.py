import math


def prime(num):
    for n in range(2, int(num**1/2)+1):
        if num % n == 0:
            return False
    return True


def semiprime(num):
    cnt = 0
    for i in range(2, int(math.sqrt(num)) + 1):
        while num % i == 0:
            num /= i
            cnt += 1
        if cnt >= 2:
            break
    if num > 1:
        cnt += 1

    return cnt == 2


while True:
    inputText = input("Type number (negative to exit):")
    try:
        inputNum = int(inputText)
        if inputNum < 0:
            break
        if prime(inputNum):
            print(inputNum, "is prime.")
        elif semiprime(inputNum):
            print(inputNum, "is semiprime.")
        else:
            print(inputNum, "is neither prime nor semiprime.")
    except:
        print("Invalid number.")
