#to find the sum of odd no in the array 
a=[1,2,3,4,5,6,7,8,9]
sum=0
for i in a :
    if i%2!=0:
        sum=sum+i
print(f'the sum of odd no in the array is {sum}')

#find the sum of  the array
a=[1,2,3,4,5,6,7,8,9]
sum=0
for i in a :
    sum=sum+i
print(f'the sum of the array is {sum}')


#to fin the largest no in the array 
a=[1,2,3,4,5,6,7,8,9]
larg=0
for i in a:
    if i>larg:
        larg=i
print(f'the largest no in the array is {larg}')

#find the square of each of the element and print them in listt 

a=[1,2,3,4,5,6,7,8,9]
square=[]
for i in a:
    square.append(i**2)
print(f'the square of the array is {square}')

#to  find the factorial of a no 
no=int(input("enter the no"))
fact=1
for i in range(1,no+1):
    fact=fact+i
print(f'the factorial of the no is {fact}')
