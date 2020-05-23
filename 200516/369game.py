number = 1
limit = 300

print("369게임을 시작하지!!")
while number <= limit :
    exponent = 1
    count = 0

    while number > 10 ** (exponent - 1) :
        determinant  = ( (number % (10 ** exponent) ) - (number % 10 ** (exponent -1))) / (10 ** (exponent -1))
        if( determinant % 3 == 0) and (determinant != 0) :
            count = count + 1
        exponent = exponent + 1

    if (count == 0):
    else:
        countChak = 0
        while countChak < count :
            print("짝!",end = "")
            countChak = countChak + 1
        print("")

    number = number + 1
