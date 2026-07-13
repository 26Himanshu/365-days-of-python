# question 1 to print all posiive and negative elements in list
# a=[12,34,-546,232,-45,3454,68,-4534]
# pos=[]
# neg=[]
# for i in a:
#     if i>0:
#         pos.append(i)
#     else:
#         neg.append(i)
# print (f'positive value are {pos}')
# print(f'negative values are {neg}')


# question 2 find the mean of the list
# a=[10,20,30,40]
# sum=0
# for i in a:
#     sum=sum+i
#     mean=sum/len(a)
# print(f'the mean of the list is {mean}')


#question 3 find the greatest element in the list
# a=[10,20,30,40,50]
# greatest=a[0]
# for i in a :
#     if i > greatest:
#         greatest=i
# print(f'the greatest element in the list is {greatest}')


#question 4 find the greatest element in the list using sort
# a=[10,20,30,40,50]
# a.sort()
# print(f'the greatest element in the list is {a[-1]}')

#question 5 find the second last element in the list
# a=[10,20,30,434,353,6546,2354235,4632343]
# larg=0
# sec_larg=0
# for i in a :
#     if i>larg:
#         sec_larg=larg
#         larg=i
#     elif i>larg:
#         sec_larg=i
# print(f'the second largest element in the list is {sec_larg}')


#questrion 6 find the second largest element in the list using sort
# a=[10,20,30,434,353,6546,2354235,4632343]
# a.sort()
# print(f'the second largest element in the list is {a[-2]}') 


#question 7  check if list is already soreted or not
# a=[10,20,3345345,234,23464356,76435234234235]
# copy=a.copy()
# a.sort()
# if a==copy:
#     print("the list is sorted")
# else :
#     print("the list is not sorted")


#question 8 check if list is already sorted or not using function
# a=[10,20,333523,56423,5423535,474523535]
# for i in range(len(a)-1):
#     if a[i]>a[i+1]:
#         print("the list is not sorted")
#         break
# else:
#     print("the list is sorted")


#question 9 reverse a list 
# a=[10,20,30,40,50]
# a.reverse()
# print(a)


#question 10 reverse a list without usiong reverse function
# a=[10,20,30,40,50]
# rev=[]
# for i in range(len(a)-1,-1,-1):
#     rev.append(a[i])
# print(rev)


#question 11 remove all duplicate elements
# a=[10,20,30,40,50,10,20,30]
# b=[]
# for i in a:
#     if i not in b:
#         b.append(i)
# print(b)


# question12 find the no of elements in the list
# a=[32,235,235,6573,234,35,346]
# len(a)
# print(len(a))


#question 13 find the sum of all elements in the list
# a=[32,235,235,6573,234,35,346]
# sum=0
# for i in a:
#     sum=sum+i
# print(f"the sum of all the elements are {sum}")


#question 14 find the product of all elements in the list
# a=[32,235,235,6573,234,35,346]
# pro=1
# for i in a:
#     pro=pro*i
# print(f"the product of all the elements are {pro}")


# question 15 print even and odd elements in the list seperately
# a=[32,235,235,6573,234,35,346]
# even=[]
# odd=[]
# for i in a:
#     if i%2==0:
#         even.append(i)
#     else:
#         odd.append(i)
# print(f'the even elements are {even}')
# print(f'the odd elements are {odd}')


