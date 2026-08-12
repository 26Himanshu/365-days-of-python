# Data type in pyhton 
# e="i can write anything inside the string"
# a=45
# b=3.14
# c=a+9j
# d=True
# print(type(a))
# print(type(b))
# print(type(c))
# print(type(d))
# print(type(e))

# print(a)
# print(b)
# print(c)
# print(d)
# print(e)

#order of any string

# a="HIMANSHU"
# b='college'
# print(a[0])
# print(a[0:4:1])
# print(a[-1:-8:-2])
# print(a[0:9:2])
# print(a[2:5:1])
# print(b[0:7:2])

#type conversion in python
# a=45
# print(float(a))


# a='12'
# b=int(a)
# print(a)
# print(b)
# print(type(a))
# print(type(b))


# a=123.45
# b=int(a)
# print(a)
# print(b)

#input , output 
# a="Himanshu"
# age = 20
# print(f"My name is {a} and my age is {age}")
# print("My name is",a,"and my age is",age,)


# a=int(input("enter the no:-"))
# b=input("enter the text:-")
# print(f"the no is:-{a}\nand the text is:-{b}")


#arithmetic operator
# a=10
# b=5
# print(a+b)
# print(a-b)
# print(a*b)
# print(a/b)
# print(a//b)
# print(a%b)
# print(a**b)

#comparison operator
# a=10
# b=56
# print(a==b)
# print(a>b)
# print(a!=b)

#logical operator and or not 
# a=10
# b=12
# print(10==10 and 12<9)
# print(10==10 or 23<3253 or 3252>23423235)
# print(not 10==10)


#confitional statement if else elif
# age=int(input("Enter the Age:-"))
# if age>=18:
#     print(f"your are eligible for voting")
# else:
#     print(f"your are not eligible for voting")

# rupee=int(input("enter the money amount:-"))
# if rupee==10:
#     print(f"i will buy a choclate")
# elif rupee==15:
#     print(f"i will buy a sandwich")
# else:
#     print(f"i will buy a burger")

#question 1
# no1=int(input("Enter the no:-"))
# no2=int(input("Enter the no:-"))
# if no1>no2:
#     print(f"{no1}")
# elif no1<no2:
#     print(f"{no2}")
# else:
#    print(f"both are equal")


#question 2
# gender=input("enter the gender:-")
# if gender=="male":
#     print(f"good morning sir")
# elif gender=="female":
#     print(f"good morning ma'am")
# else:
#     print("hey good morning")

#question 3
# a=int(input("enter the no:-"))
# if a%2==0:
#     print(f"{a} is even")
# else:
#     print(f"{a} is odd")

#question 4

# name=input("enter thee name:-")
# age=int(input("enter the age:-"))
# if age>=18:
#     print(f'Hello{name} you are eligible for voting')
# else:
#     print(f"you are not eligible for voting and you have to wait for {18-age} years to vote")


#question 5
# year=int(input("enter the year:-"))
# if year%100==0 and year%400==0:
#     print("leap year")
# elif year%100!=0 and year%4==0:
#     print("leap year")
# else:
#     print("not a leap year")


#question 6
# temp=int(input("Enter the temp"))
# if temp>0 and temp<15:
#     print("it is cold")
# elif temp<0 and temp>-10:
#     print("it is freezing")
# elif temp>15 and temp<25:
#     print("it is normal")
# elif temp>25:
#     print("it is hot")


#for loop 
# n=int(input("enter the no:-"))
# for i in range(n,n*10+1,n):
#     print(i) 



# a="HIMANSHU"
# for i in range(len(a)):
#     print(f"{a[i]}-{i}")


#break continue else
# for i in range (1,11):
#     if i==12:
#         break
#     print(i)
# else:
#     print("no break was encountered")

#print hello world nn time 
# n=int(input("enter the no"))
# for i in range(n):
#     print("hello world")

#print natural no from 1 to 10
# n=int(input("enter the no:-"))
# for i in range(1,n+1):
#     print(i)

#revverse for loop n to 1
# n=int(input("enter the no"))
# for i in range(n,0,-1):
#     print(i)

#print the multiplication table of a no

# n=int(input("enter the no:-"))
# for i in range(n,n*10+1,n):
#     print(i)

# n=int(input("enter the no:-"))
# for i in range(1,11):
#     print(f"{n}x{i}={n*i}")
    

#sum of first n natural no
# n=int(input("enter the no:-"))
# sum=0
# for i in range(1,n+1):
#     sum+=i
# print(f"the sum is {sum}")

#factorial of a no 
# n=int(input("enter the no:-"))
# fact=1
# for i in range(1,n+1):
#     fact*=i
# print(f"the factorial is {fact}")

#print sum of all even and odd no seperately
# n=int(input("enter the no:-"))
# evensum=0
# oddsum=0
# for i in range(1,n+1):
#     if i%2==0:
#         evensum+=i
#     else:
#         oddsum+=i
# print(f"the sum of even no is {evensum}\nand the sum of odd no is {oddsum}")

#print all factor of a no
# n=int(input("enter the no:-"))
# for i in range(1,n+1):
#     if n%i==0:
#         print(i)

#check if a no is perfect no or not
# n=int(input("enter the no:-"))
# sum=0
# for i in range(1,n):
#     if n%i==0:
#         sum+=i
# if sum==n:
#     print("perfect no")
# else:
#     print("not a perfect no")


#check if a no is prime or not
# n=int(input("enter the no:-"))
# count=0
# for i in range (1,n+1):
#     if n%i==0:
#         count+=1
# if count==2:
#     print("prime no")
# else:
#     print("not a prime no")

#reverse a string 
# a="HIMANSHU"
# rev=" "
# for i in range(len(a)-1,-1,-1):
#     rev=rev+a[i]
# print(rev)


#check palindrome
# a="himanshu"
# rev=""
# for i in range(len(a)-1,-1,-1):
#     rev=rev+a[i]
# if rev==a:
#     print("palindrome")
# else:
#     print("not a palindrome")


# n=input("enter the no:-")
# rev=""
# for i in range(len(n)-1,-1,-1):
#     rev=rev+n[i]
# if rev==n:
#     print("palindrome")
# else:
#     print("not a palindrome")


#count letter digits and special char
# a="214yfn75-34m92067483fm823982^&*()*&$%^&*()"
# lett=0
# char=0
# dig=0
# for i in a:
#     if i.isalpha():
#         lett+=1
#     elif i.isdigit():
#         dig+=1
#     else:
#         char+=1
# print(f"letters: {lett}, digits: {dig}, special characters: {char}")



#while loop 
# a=1
# while a!=3000:
#     print(a)
#     a+=1


#question
# n=int(input("enter the no:-"))
# while n>0:
#     print(n%10)
#     n=n//10
# print(n)
 

#accept a no and print its no

# n=int(input("enter the no:-"))
# rev=0
# while n>0:
#     rev=rev*10+n%10
#     n=n//10
# print(rev)


#check a no is palindrome or not
# n=int(input("enter the no:-"))
# copy=n
# rev=0
# while n>0:
#     rev=rev*10+n%10
#     n=n//10
# if rev==copy:
#     print("palindrome")
# else:
#     print("not a palindrome")



#game creating 

import random
com=random.randint(1,100)
count=0
while True:
    count+=1
    hum=int(input("enter the no:-"))
    if hum==com:
        print("you won in {count} attempts")
        break
    elif hum>com:
        print("you are greater than computer no")
    else:
        print("you are smaller than computer no")
