# def add(num1, num2):
#     return num1 + num2
 

# def subtract(num1, num2):
#     return num1 - num2
 

# def multiply(num1, num2):
#     return num1 * num2
 

# def divide(num1, num2):
#     return num1 / num2
 
# print("Please select operation -\n" \
#         "1. Add\n" \
#         "2. Subtract\n" \
#         "3. Multiply\n" \
#         "4. Divide\n")
 
# select = int(input("Select operations form 1, 2, 3, 4 :"))
 
# number_1 = int(input("Enter first number: "))
# number_2 = int(input("Enter second number: "))
 
# if select == 1:
#     print(number_1, "+", number_2, "=",
#                     add(number_1, number_2))
 
# elif select == 2:
#     print(number_1, "-", number_2, "=",
#                     subtract(number_1, number_2))
 
# elif select == 3:
#     print(number_1, "*", number_2, "=",
#                     multiply(number_1, number_2))
 
# elif select == 4:
#     print(number_1, "/", number_2, "=",
#                     divide(number_1, number_2))
# else:
#     print("Invalid input")

def Add(num1, num2):
    return num1 + num2
def Subtract(num1, num2):
    return num1 - num2
def Multiply(num1, mum2):
    return num1 * num2
def Divide(num1, num2):
    return num1 / num2
print("please select your operation -\n"
      "1. Add \n"
      "2. Subtract \n"
      "3. Multiply \n"
      "4. Divide \n")

select=int(input("Select Operation Form 1,2,3,4: "))
number1=int(input("please enter first num: "))
number2=int(input("please enter second num: "))

if select == 1:
    print(number1, "+", number2, "=",
          Add(number_1, number_2))
elif select == 2:
    print(number1, "-", number2, "=",
          Multiply(number1, number2))
elif select == 3:
    print(number1, "*", number2, "="
          Divide(number1, number2))
elif select == 4:
    print(number1)
else:
    print("Invalid number")