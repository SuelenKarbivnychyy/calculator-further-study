"""CLI application for a prefix-notation calculator."""

from arithmetic import (add, subtract, multiply, divide, square, cube,
                        power, mod, )


# Replace this with your code

while True:
    user_input = input("Type Which operation do you want to do, followed by the numbers you want to work with, or tap 'q' to quit: ")    
    
    operation_list = user_input.split(" ")
    math_operation = operation_list[0]    

    if user_input == "q":
        print("good bye")
        break
    elif len(operation_list) < 3:
        print("not enough input. Please try again.")    
        continue

    num_1 = operation_list[1]
    num_2 = operation_list[2]
    result = 0
    
    if not num_1.isdigit() or not num_2.isdigit():
        print("Make sure you are entering numbers.")
        continue    
    
    elif math_operation == "+":        
        result = add(float(num_1), float(num_2))     
        print(result)
    elif math_operation == "-":
        result = subtract(float(num_1), float(num_2))   
        print(result)
    elif math_operation == "*":
        result = multiply(float(num_1), float(num_2))
        print(result)
    elif math_operation == "/":
        result = divide(float(num_1), float(num_2))  
        print(result)
    elif math_operation== "square":
        result = square(float(num_1))
        print(result)
    elif math_operation== "cube":
        result = cube(float(num_1)) 
        print(result) 
    elif math_operation == "power":
        result = power(float(num_1), float(num_2))  
        print(result)     
    elif math_operation == "mod":
        result = mod(float(num_1), float(num_2))  
        print(result)    
    else:
        print("operation not found, please enter a valid operator")     
        continue
