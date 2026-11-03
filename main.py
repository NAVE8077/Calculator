try:
    a = int(input("Enter the first number:"))
    b = int(input("Enter the second number:"))
    print("What kind of operation do you want to perform. press + for addition\n press - substraction \n press / for division\n press * for multiplication")
    o = input("Enter operation:")
    match o:
        case "+":
            print(f"the result is : {a+b}")
        case "-":
            print(f"the result is : {a-b}")
        case "*":
            print(f"the result is : {a*b}")
        case "/":
            print(f"the result is : {a/b}")
        case defult:
            print(f"there wasan error")
except Exception as e:
    print("Enter a valid value of a and b")
    