#exception handeling
# a=int(input("enter the no"))
# b=int(input("enter the no"))
# try:
#     print(a/b)
# except ZeroDivisionError:
#     print("you can not divide by zero")

# name=input("enter the name")


#raise an exception`
# age=int(input("enter the age"))
# if age>18:
#     raise valueError("age is greater than 18")  
# print(f"the age is {age}")


# file=open("hello.txt","w")

# data=input("what you want to write :-")

# file.write(data)

#to read from file
file =open("hello.txt","r")
print(file.read())


#to update in a file 
with open("hello.txt",'a') as f:
    f.write(""+"i want to see this add or not")
    