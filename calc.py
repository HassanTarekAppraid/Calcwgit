def add(num1, num2):
    return num1 + num2

def subtract(num1, num2):
    return num1-num2

#print(add(4, 2))
#print(subtract(4, 2))

print("Welcome to H&H Git Practice Calculator :)\n"
"Press - for Subtraction\n")

selection = input("Select Operation (-): ")
num1 = float(input("Enter the First Number: "))
num2 = float(input("Enter the Second Number: "))

if selection == '-':
    result=subtract(num1, num2)
    print(num1,"-",num2, "=", result)
elseif selection == '+' :
    result=add(num1, num2)
    print(num1,"-",num2, "=", result)   




