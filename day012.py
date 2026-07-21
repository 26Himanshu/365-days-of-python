#questions 
#print hello world 
# print('hello himanshu welcome to the python')

#print your name and age
# name=input('enter the name:- ')
# age=int(input('enter the age:- '))
# print(f'Hello my name is {name} and my age is {age}')


#adding two no 
# no1=int(input('enter the no1:-'))
# no2=int(input('enter the no2:-'))
# sum=no1+no2
# print(f'the sum of two no is {sum}')


#cheking whether a no is divisible by 2 or no 
# n=int(input('enter the no:-'))
# if n%2==0:
#     print(f'the no is divisible by 2')
# else:
#     print(f'the no is not divisible by 2')


# check whether a person is eligible for voting or not 
# name=input('enter the name')
# age=int(input('enter the age'))
# if age>=18:
#     print(f'hello {name} , you are eligible for vote')
# else:
#     print(f'hello {name} , you are not eligible for vote')


#to find the sum of first n natural no 
# n=int(input("entert the no"))
# sum=0
# for i in range(1,n+1):
#     sum+=i
# print(f'the sum opf first n natural no is {sum}')


#to find the factorial of a no
# n=int(input('enter the no'))
# fact=1
# for i in range(1,n+1):
#     fact=fact*i
# print(f'the factorial of a no is {fact}')


#to print table of any no 
# n=int(input('enter the no:-'))
# for i in range(n,n*10+1,n):
#     print(i)

#print the table in form of like( 5x1=5) this form
# n=int(input('enter the no:-'))
# for i in range (1,11):
#     print(f'{n} x {i} = {n*i}')


#find whiose fact is greater between two no
# n1=int(input('enter the no1:-'))
# n2=int(input('enter the no2:-'))
# fact1=1
# for i in range(1,n1+1):
#      fact1=fact1*i
# fact2=1
# for i in range(1,n2+1):
#         fact2=fact2*i      
# if fact1>fact2:
#     print(f'the factorial of {n1} is greater than {n2}') 
# else:
#     print(f'the factorial of {n2} is greater than {n1}')


#print natural no from decending order
# n=int(input('enter the no'))
# for i in range(n,1,-1):
#     print(i)


#find the factor of a no 
# n=int(input('enter the no'))
# for i in range(1,n+1):
#     if n%i==0:
#         print(i)


#to print all the positive and negative no from the list
# a=[-1,-2,3,4,-5,6,7,-8,9]
# pos=[]
# neg=[]
# for i in a:
#     if i>0:
#         pos.append(i)
#     else:
#         neg.append(i)
# print(f'positive values are {pos}')
# print(f'negative values are {neg}')


#find the mean of  a list
# a=[123,352,62,473,4235,12,45125,473,7427]
# sum=0
# for i in a:
#     sum+=i
#     mean=sum/len(a)
# print(f'the mean of the list is {mean}')

#find teh greatest element in the list
# a=[123,352,62,473,4235,12,45125,473,7427]
# greatest=a[0]
# for i in a :
#     if i>greatest:
#         greatest=i
# print(f'the greatest element in the list is {greatest}')


#reverse a list
# a=[123,352,62,473,4235,12,45125,473,7427]
# a.reverse()
# print(f'the reverse of the list is {a}')

# rev=[]
# for i in range(len(a)-1,-1,-1):
#     rev.append(a[i])
# print(f'the reverse of the list is {rev}')


#print even and odd no from the list
# a=[123,352,62,473,4235,12,45125,473,7427]
# even=[]
# odd=[]
# for i in a :
#     if i%2==0:
#         even.append(i)
#     else:
#         odd.append(i)
# print(f'the even no from the list is {even}')
# print(f'the odd no from the list is {odd}')


#to add a no in the list
# a=[123,352,62,473,4235,12,45125]
# a.append(424141)
# print(a)
# a.insert(2,12)
# print(a)


# #to remove a no from the list

# a=[123,352,62,473,4235,12,45125]
# b=a.pop(3)
# print(a)
# print(b)

#to remove a no from the list
a=[123,352,62,473,4235,12,45125]
a.remove(62)
print(a)