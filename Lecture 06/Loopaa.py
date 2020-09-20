terminate = False
while not terminate:
    number1 = input("Please enter a number : ")
    number1 = int(number1)
    number2 = input("Please enter a number : ")
    number2 = int(number2)

    while True:
        operation = input("Please enter add/sub ")
        if operation == "quit":
            terminate == True
            break
        if operation not in ["add", "sub"]:
            print("unknown operation!")
            continue

        if operation == "add":
            print("Result is",number1 + number2)
            break

        if operation == "sub":
            print("Result is",number1 - number2)
            break



