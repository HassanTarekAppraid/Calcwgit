#Addition Main Function
def add(num1, num2):
    return num1 + num2
#Subtract Main Function
def subtract(num1, num2):
    return num1-num2

#print(add(4, 2))
#print(subtract(4, 2))

#Welcome Message
print("Welcome to H&H Git Practice Calculator :)\n"
"Press - for Subtraction & + for Addition\n") #welcome message

#User select which operation to make
selection = input("Select Operation (-,+): ")

#Getting the numbers from the user
num1 = float(input("Enter the First Number: "))
num2 = float(input("Enter the Second Number: "))

#If condition based on user selection
if selection == '-':
    result=subtract(num1, num2)
    print(num1,"-",num2, "=", result) #result
elif selection == '+' : #condition for addition feature
    result=add(num1, num2)
    print(num1,"+",num2, "=", result) #result
else:
    print("this is an invalid operation")   #if none of the operations changed    




