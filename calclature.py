while (True):
    #get numbers from user
    First_num = int(input("what is the first number: "))
    operation = input("what is the operation(-,+,/,*,p,%,): ")

    #define the operation

    if operation == "p":
        power = int(input("Enter number of power : "))
        print(First_num ** power)
    elif operation == "+" or operation == "*" or operation == "/" or operation == "-" or operation == "%":
        second_num = int(input("what is the second number: "))

        if operation == "*":
            print(First_num * second_num)

        elif operation == "+":
            print(First_num + second_num)

        elif operation == "-":
            print(First_num - second_num)

        elif operation == "/":
            if second_num == 0:
                print("Division by zero is an undefined operation.")
            else:
                print(First_num / second_num)
        elif operation == "%":
            print(First_num% second_num)
    else:
        print("this operation is not included yet")
    again= input("do you want to start again: ")
    if  again.lower == "no":
        break    