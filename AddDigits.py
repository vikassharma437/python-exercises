two_digit_number = input("Type a two digit number: ")

if len(two_digit_number) == 2:
    flag = two_digit_number.isnumeric()
    if flag:
        digit1 = int(two_digit_number[0])
        digit2 = int(two_digit_number[1])
        print(digit1 + digit2)
    else:
        print("Nothing to print")
else:
    print("Input should be two digit number. Please enter valid input.")




