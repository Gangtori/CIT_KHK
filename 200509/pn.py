number = 6379
divider = 2
isprime = False

while (divider < number) and (not isprime):
    if number % divider == 0:
        print(divider)
        print("로 나누어떨어지므로 소수가 아님!")
        isprime = True
    elif divider == number -1 :
        print("소수로구나!")

    divider = divider + 1
