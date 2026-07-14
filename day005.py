# to find the sum of nn nnatural nno 
# a=[23,23,4,45,46,57,584]
# sum=0
# for i in a:
#     sum+=i
# print(f'the sum of the array is {sum}')

# to find the average of the array
# a=[23,23,4,45,46,57,584]
# sum=0
# for i in a:
#     sum+=i
#     avg=sum/len(a)
# print(f'the avg of an arraay is {avg}')

#to find the square of every element in an array
# a=[23,23,4,45,46,57,584]
# square=[]
# for i in a:
#     square.append(i**2)
# print(f'the square of the array is {square}')


#to check whether i am eligible for afcat or not 
# age=int(input("enter your age"))
# height=int(input("enter your height in cm"))
# if age>18 and height>170:
#     print("you are eligible for afcat")
# else:
#     print("you are not eligible for afcat")

#to check whether the given no is odd or even 
# no=int(input("ennter the nno"))
# if no%2==0:
#     print(f"{no} is even")
# else:
#     print(f"{no} is odd")

#accept two no and print the greatest
# n1=int(input("enter the first no"))
# n2=int(input("ennter the second no"))
# if n1>n2:
#     print(f'{n1}>{n2}')
# else:
#     print(f'{n2}>{n1}')

#accept gender from user and print a greeting message 
# gender=input("enter the gender")
# if gender== "male":
#     print("Good morning sir")
# elif gender=="female":
#     print("Good morning ma'am")
# else:
#     print("Good morning")

#accept an integer and check whether it is odd or even
# a=int(input("enter the no"))
# if a%2==0:
#     print(f"{a} is even")
# else:
#     print(f"{a} is odd")

#acccept a year and check whether it is a leap year or not
# year=int(input("enter the year"))
# if year%400==0 or year%4==0:
#     print(f"{year} is a leap year")
# elif year%100!=0:
#     print(f"{year} is not a leap year")


#temp ladder
# tem=int(input("enter the temperature"))
# if tem<0 and tem>-10:
#     print("freezing weather")
# elif tem>0 and tem<=10:
#     print("very cold weather")
# else :
#     print("temp is hot")


#print hello world n time 
# n=int(input("enter the number of times you want to print hello world"))
# for i in range(n):
#     print("hello world")


# print natural no from 1 to n
# n=int(input("enter the time of no"))
# for i in range(1,n+1):
#     print(i)

#reverse for loop n to 1
# n=int(input("ennter the no"))
# for i in range(n,0,-1):
#     print(i)

#print the multiplicationn of a table 
n=int(input("enter the no"))
for i in range(1,11):
    print (f'{n}x{i}={n*i}')