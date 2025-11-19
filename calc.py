def add(num1, num2): #function to add numbers
    return num1 + num2

def subtract(num1, num2): #function to subtract numbers
    return num1-num2

#print(add(4, 2))
#print(subtract(4, 2))

#Welcome Message
print("Welcome to H&H Git Practice Calculator :)\n"
"Press - for Subtraction & + for Addition\n") #welcome message

selection = input("Select Operation (-,+): ") #asks user to select operation
num1 = float(input("Enter the First Number: ")) #asks user to enter first number
num2 = float(input("Enter the Second Number: ")) #asks user to enter second number

if selection == '-': #if condition for subtraction feature
    result=subtract(num1, num2)
    print(num1,"-",num2, "=", result) #result
elif selection == '+' : #condition for addition feature
    result=add(num1, num2)
    print(num1,"+",num2, "=", result) #result
else:
    print("this is an invalid operation")   #if none of the operations changed    




