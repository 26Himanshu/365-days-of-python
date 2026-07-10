#question 1 print hello world 
# print("Hello himanshu")

#question 2 print your name and age
# name=input("enter your name")
# age=int(input("enter your age"))
# print (f"my name is {name} and age is {age}")

#question 3 adding two numbers
# num1=int(input("enter no1"))
# num2=int(input("enter no2"))
# sum=num1+num2
# print(f"the sum of your no is {sum}")

#question 4 check whetehger a no is divisible by 2 or not
# num=int(input('enter the no'))
# if num%2==0:
#     print("the no is divisible by 2 ")
# else:
#     print("the no is not divisible by 2")

#question 5 check whether a person is elgible for voting or not 
# Name=input("enter your name")
# age=int(input("enter the age"))
# if age>=18:
#     print(f"hello {Name} you are eligible for voting ")
# else :
#     print (f"hello {Name} you are not eligible for voting")
    
#question 6 to find the sum of first n natural no
# n=int(input("enter the no"))
# a=0
# for i in range (1,n+1):
#     a=a+i
# print(f"the sum of you first {n} natural no is {a}")

#question 7  to find the factorial of a no 
# n=int(input("enter the no"))
# a=1
# for i in range (1,n+1):
#     a=a*i
# print(f"the factorial of {n} is {a}")

# question 8 to print the table of any no
# n=int(input("enter the no "))
# for i in range (n,n*10+1,n):
#     print(i)

# question 9 print the table in form of like( 5x1=5) this form 
# n=int(input("enter the no"))      
# for i in range (1,11):
#  print(f"{n} x {i} = {n*i}")

#question 10 if your age is above 18 and height is above 170 cm then only yor are eligible for afcat
# Name=input("enter your name")
# Age=int(input("enter your age"))
# Height=int(input("enter your height in cm"))
# if Age >=18 and Height>=170:
#     print (f'hello {Name} you are eligible for afcat')
# else:
#     print("you are not elgible for afcat")

#question 11 find which no is greater between two no
# n1=int(input("enter the no"))
# n2=int(input("enter the no"))
# if n1>n2:
#     print(f'{n1} is greater than {n2}')
# else:
#     print(f'{n2} is greater than {n1}')

#question 12 accept gender and print message acc to the gender 
# gender=input("enter the gender")
# if gender=="male":
#     print("good morning sir")
# elif gender=="female":
#     print("good morning madam")
# else:
#     print("good morning guest")

#question 13 accpet temp and write the description
# temp=int(input("enter the temp"))
# if temp<=0 and temp>=-10:
#     print ("the temp is very cold ")
# elif temp>=1 and temp<=10:
#     print("the temp is cold")
# elif temp>=20 and temp<=30:
#     print("the temp is normal")
# elif temp>=11 and temp<=19:
#     print("the temp is mild cold")
# else:
#     print("the temp i cant measure")

#question 14 print natural no from decending order
# n=int(input("enter the no"))
# for i in range(n,0,-1):
#     print(i)

#question 15 to find the factor   of a no
n=int(input("enter the no"))
for i in range(1,n+1):
    if n%i==0:
        print(i)
        