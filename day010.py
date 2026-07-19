#revision of last day questions 
#to add sometthing in the dictionary
# a={1:10,2:20}
# a.update({3:30})
# print(a)


#merge two dictionary 
# a={1:10,2:20}
# b={3:30,4:40}
# a.update(b)
# print(a)


#sum of all values in dictionary 
# a={1:10,2:20,3:30}
# sum=0
# for i in a:
#    sum+=a[i]
# print(sum)

#finding the frequency of each element in the list 
# a=['a','b','c','a','b','a']
# d={}
# for i in a:
#    if i in d.keys():
#          d[i]=d[i]+1
#    else:
#          d[i]=1
# print(d)


#check the list is soprted or not 
# a=[1,2,3,4,5,354,35,46,47,3,43623,621,267,45745,8458,234,634,1241,125]
# for i in range(len(a)-1):
#      if a[i]>a[i+1]:
#          print(f'list is not sorted')
#          break
# else:
#     print(f'list is sorted')

# a.sort()
# print(a)


#to check set a is subset of b or not
# a={1,2,3,4,5,6,7}
# b={1,2,3,4,5,6,7,8,9,10}
# if a<=b:
#     print(f'set a is subset of set b')
# else: 
#     print(f'set a is not subset of set b')


#print hello words n time 
# n=int(input('enter the no '))
# for i in range(n):
#     print("hello world")



#print natural no n times
# n=int(input('enter the no '))
# for i in range(1,n+1):
#       print(i)

#print reverse loop from n to 1
# n=int(input('enter the no'))
# for i in range(n,0,-1):
#       print(i)



#print the sum of n natural no
# n=int(input("enter the no"))
# sum=0
# for i in range(1,n+1):
#     sum+=i
# print(f'the sum of n natural no is {sum}')

#factorial of a no 
# n=int(input('enter the no'))
# fact=1
# for i in range(1,n+1):
#       fact=fact*i
# print(f'the factorial of {n} is {fact}')


#print the multiplication of a table
n=int(input("enter the no"))
for i in range(n,n*10+1,n):
      print(i)


#find the second largest  element in the list
a=[1,2,3,4,5,6,7,8,9]
lar=0
sec_lar=0
for i in a:
      if i>lar:
            sec_lar=lar
            lar=i
      
print(f'the second largest no is {sec_lar}')