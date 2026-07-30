
# input fuctions  use input() function to take input from user
first_name = input("Enter your first name: ")
last_name = input("Enter your last name: ")

print("are you " ,first_name + " " + last_name)

print (first_name ,end="&&\n")
print(first_name , last_name ,sep="-")

#if else condition
marks = int(input("enter your marks = "))
if marks >= 10:
    print("excellent")
elif marks <= 10 and marks>=5:
    print("good")
else:
    print("bad")


#ternary operator 

marks =     int(input("enter the marks = "))
result = "pass" if marks >=10 else "fail"
print(result) 