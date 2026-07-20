#some of the revised question that i hacve done from my side 

#find the sum of factorial of a no 
# n=int(input("enter the no "))
# fact=1
# for i in range(1,n+1):
#     fact=fact*i
# print(f'the factorial of a {n} is {fact}')

#fin the sum of the first n natural no 
# n=int(input('enter the no '))
# sum=0
# for i in range(1,n+1):
#     sum+=i
# print(f'the sum of first {n} natural no is {sum}')


#find the sum of the first first n odd no 
# n=int(input("enter the no "))
# sum=0
# for i in range(1,n+1):
#     if i%2!=0:
#         sum+=i
# print(f'the sum of first {n} odd no is {sum}')


#find the sum of odd and even no from 1 to n
# n=int(input("enter the no"))
# odd_sum=0
# even_sum=0
# for i in range(1,n+1):
#     if i%2==0:
#         even_sum+=i
#     else:
#         odd_sum+=i
# print(f'the sum of odd no is {odd_sum}')    
# print(f'the sum of even no is {even_sum}')


#to reverse a string
# a="himanshu"
# end=""
# for i in range(len(a)-1,-1,-1):
#     end+=a[i]
# print(end)

#to print a table of any no 
# n=int(input('enter the no'))
# for i in range(n,n*10+1,n):
#     print(i)



#to find the second largest no from the list
a=[1,2,3,4,5,6,7,8,9]
a.sort()
print(a[-2])


#alternate
a=[1,2,3,4,5,6,7,8,9]
lar=0
sec_lar=0
for i in a :
    if i>lar:
        sec_lar=lar
        lar=i
print(f'the second largest no is {sec_lar}')


#to add something in dictionary
a={1:10,2:20}
a[3]=30
print(a)

#to merge two dictq
a={1:10,2:20}
b={3:30,4:40}
a.update(b)
print(a)