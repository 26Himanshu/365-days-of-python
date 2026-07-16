#revision of all the 1st video questions

#1st 
# print("Hello himanshu")

#2nd comments
# thhis is used for comments
''' this also used for comments'''

#varisable mmaking
# num=10
# name='himanshu' 

#data types
#int
# no=10
# print(type(no))
#float
# a=1.765
# print(type(a))
#complex
# b=a+2j
# print(type(b))
#string
# c="hello23241253@#$%^&()"
# print(type(c))
#boolean
# a=True
# b=False
# print(type(a))
# print(type(b))

#ascii value
# a="j"
# print(ord(a))

#to print only one char
# a='COLLEGE'
# print(a[4])
# print(a[0:4:1]) #a[start:stop:steps]
# print(a[0:7:2])

#convert data type
# a="1234"
# a= int(a)

# print (type(a))


# name=input('enter the name')
# no=int(input('enter the no'))
# print('name is',name)
# print('no is',no)

#short 
# a=10
# a=a+10
# a=a+10
# a+=10

#print table of 5

# for i in range(5,51,5):
#     print(i)


#break continue else

# for i in range(1,11):
#     if i==5:
#         break
#     print(i)
# else:
#     print('loop is completed')






# accept two no and check which is greater and print it
# no1=int(input("enter first no:-"))
# no2=int(input("enter second no:-"))
# if no1>no2:
#     print(f'{no1} is greater than {no2}')
# elif no1==no2:
#     print(f'{no1} is equal to {no2}')
# else:
#      print(f'{no2} is greater than {no1}')


#accept gender from user and print message according to gender
# gen=input("enter your gender:-")
# if gen=="male":
#     print("Good morning sir")
# elif gen=='female':
#     print("Good morning mam")
# else:
#     print("good morning")


#accept an integer and check whether it is even or odd
# a=int(input('enter the no'))
# if a%2==0:
#     print(f'the no is even ')
# else:
#     print(f'the no is odd')


#accept name and age check user is valid to vote or not
# name=input('enter the name')
# age=int(input('enter the age'))
# if age>=18:
#     print(f'{name} you are eligible for voting')
# else:
#     print(f'{name} you are not eligible for voting')


#accept a year and check whether it is leap year or not
# year=int(input('enter thee year'))
# if year%4==0 and year%100!=0:
#     print(f'{year} is a leap year')
# elif year%400==0:
#     print(f'{year} is a leap year')
# else:
#     print(f'{year} is not a leap year')


#accept temp in celcius and convert it into fahrenheit
# temp=int(input('enter the temp in celcius'))
# temp=temp*9/5+32
# print(f'the temp in fahrenheit is {temp}')


#accept temmp in degree and print a description according to temp
# temp=int(input('enter the temp in degree'))
# if temp<0 and temp>-10:
#     print('freezing weather')
# elif temp>0 and temp<15:
#     print('cold weather')
# elif temp>15 and temp<25:
#     print('normal in temp')
# elif temp>25 and temp<35:
#     print('hot')
# elif temp>35:
#     print('very hot')


# print hello world n time 
# n=int(input("enter the word "))
# for i in range(n):
#     print("hello world")


#print natural no 1 to n time 
# n=int(input('enter the no'))
# for i in range(1,n+1):
#     print(i)


#reverse for loop print n to 1
# n=int(input("enter the no"))
# for i in range(n,0,-1):
#     print(i)


#print the multipllictaion of a no 
# n=int(input("enter the no"))
# for i in range (n,n*10+1,n):
#     print(i)


#sum of first n natural no 
# n=int(input('enter the no'))
# sum=0
# for i in range(1,n+1):
#     sum=sum+i
# print(f'the sum of first {n} natural numbers is {sum}')


#factorial of a no 
# n=int(input('enter the no'))
# fact=1
# for i in range(1,n+1):
#     fact=fact*i
# print(f'the factorial of {n} is {fact}')


#print sum of all even and odd no seperately 
# a=int(input("enter the no"))
# oddsum=0
# evensum=0
# for i in range(1,a+1):
#     if i%2==0:
#         evensum=evensum+i
#     else:
#         oddsum=oddsum+i
# print(f'the sum even no is {evensum} and the sum of odd no is {oddsum}')


#print all factor of a no
# no=int(input('enter the no'))
# for i in range(1,no+1):
#     if no%i==0:
#         print(i) 


#check if a no is perfect (sum of factor=the no itself)
# a=int(input("enter the no"))
# s=0
# for i in range(1,a):
#     if a%i==0:
#         s=s+i
# if s==a:
#     print(f'{a} is a perfect no')
# else:
#     print(f'{a} is not a perfect no')


#check the no is prime or not
# n=int(input("enter the no"))
# count=0
# for i in range (1,n+1):

#  if n%i==0:
#   count=count+1
# if count==2:
#   print(f'{n} is a prime no')
# else:
#     print(f'{n} is not a prime no')


#reverse a string without using function
# a="himanshu"
# rev=""
# for i in range(len(a)-1,-1,-1):
#     rev= rev+a[i]
# print(rev)


# a="himanshu"
# print(a[::-1])


#to check the word is plindrom or not

# a=input("enter the word")
# rev=""
# for i in range(len(a)-1,-1,-1):
#     rev+=a[i]
# if a==rev:
#         print(f'{a} is a plindrom')
# else:
#         print(f'{a} is not a plindrom')


# count letter words aplphabet in a string
# a="JBJ^%^%$^&^4567686789"
# char=0
# spchar=0
# digit=0
# for i in a:
#     if i.isdigit():
#         char+=1
#     elif i.isalpha():
      
#       digit+=1
#     else:
#         spchar+=1
# print(f'char={char} digit={digit} spchar={spchar}')


#reverse interger  accpet a no and print its reverse
# a=int(input("enter the no"))
# rev=0
# while a>0:
#     rev=rev*10+a%10
#     a=a//10
# print(f'the reverse of the no is {rev}')


#check if the no is palidrome or no
# a=int(input("enter the no"))
# copy=a
# rev=0
# while a>0:
#     rev=rev*10+a%10
#     a=a//10
# if rev==copy:
#         print(f'the no is palidrome')

# else:
#         print(f'the no is not palidrome')


##pyhton game using random no ##
import random 

computer=random.randint(1,100)

while True:
    human=int(input("enter the no between 1 to 100"))

    if human==computer:
      print('you won the game')
      break

    elif human>computer:
      print('go down ')
      
    elif human<computer:
     print('go up')


