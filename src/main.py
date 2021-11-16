import Error

number = 10
while True:
    try:
        my_number = int(input("Please enter a number :"))
        if my_number < number:
            raise Error.ValueSmallError
        elif my_number > number:
            raise Error.ValueLargeError
        break
    except Error.ValueSmallError as vsr:
        print(vsr)
        print("please enter again...")
    except Error.ValueLargeError as vlr:
        print(vlr)
        print("please enter again...")

print("done...")