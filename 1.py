#hi
intvariable = 4
floatVariable =4.5
stringVariable = "Software 1 is fun"

print (intvariable)
print(floatVariable)
print(stringVariable)

print (type(intvariable))
print (type(floatVariable))
print (type(stringVariable))

#typecasting is fun
intvariable = int(floatVariable)
print("here is the the int version of float variable " , intvariable)

share0fLoan = 500.50/3
print(share0fLoan)
print(int(share0fLoan))
print(type(share0fLoan))


num1= int(input("enter a number: " ))
num2=float(input("enter another number: " ))
sum= num1 + num2

print (sum)

name = input("enter your name: ")
school = input("enter your school: ")
print("you are: " ,name, " and your school name is: ",school)
print (f"your name is,{name},and your school name is : {school}")
floatVariable = 4.534763943042804
print(f"your name is {name},and your floatVariable is {floatVariable} ")
print ("your name is {name} and your floatVariable is {floatVariable: .2f}")