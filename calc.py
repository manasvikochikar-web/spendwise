class solution : 
    
    num1 = input("Enter the first number : ")
    operation = input("Enter the operation : ")
    num2 = input("Enter the second number : ")   

    if operation == "+" :
        sum = int(num1) + int(num2)    
        print(sum)
    elif operation == "-" :
        sub = int(num1) - int(num2)    
        print(sub)
    elif operation == "*" :
        mul = int(num1) * int(num2)    
        print(mul)
    elif operation == "/" :
        div = int(num1) / int(num2)    
        print(div)
    else :
        print("Invalid operation")