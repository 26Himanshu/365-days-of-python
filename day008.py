#  all the questions of video 2
#question 1 find all positive and negative element separately
# a=[1,2,3513,46346,235125,-454,-46,2342,-35123,-43564636]
# pos=[]
# neg=[]
# for i in a:
#     if i>0:
#         pos.append(i)
#     else:
#         neg.append(i)
# print(f'positive elements: {pos}')
# print(f'negative elements: {neg}')

#question 2 find the mean of the list 
# a=[1,2,3,4,5,6,7,8,9,10]
# sum=0
# for i in a:
#     sum=sum+i
#     mean=sum/len(a)
# print(f'the mean is {mean}')


#find the greatest element and print its index
# a=[1,2,3,4,5,6,7,8,9,10]
# gre=0
# for i in a:
#     if i>gre:
#         gre=i
# print(f'the greatest element is {gre} and its index is {a.index(gre)}')


# a=[3423,3523,23523,232,43562352]
# gre=a[0]
# index=0
# for i in range(len(a)):
#     if a[i]>gre:
#         gre=a[i]
#         index=i
# print(f'the gretest no is {a[i]} and the index is {index}' )


#find the second greatest element
# a=[213,3542,123412,431221,231231,2342,231,23145,151251,25]
# a.sort()
# print(a[-2])

# a=[12332,124,351,2346,34,3,3,23652,46,57243,74374,6723523]
# larg=0
# sec_larg=0
# for i in a:
#     if i>larg:
#         sec_larg=larg
#         larg=i
# print(f'the second largest no is {sec_larg}')

#check the list is sorted or not
# a=[123,343,435,34634,234,23426,4635,453,4534,534564,563634,63636]

# for i in range(len(a)-1):
#     if a[i]>a[i+1]:
#         print (f'your list is not sorted')
#         break
# else:
#         print(f'your list is sorted')

#to check set a is subset of b or not
# a={1,2,3,4,5,6,7}
# b={1,2,3,4,5,6,7,8,9,10}

# if a<=b:
#       print(f'set a is subset of set b')
# else:    
#       print(f'set a is not subset of set b')

#to check a is superset of b
# a={1,2,3,4,5,6}
# b={1,2,3}
# if a>=b:
#       print(f'set a is superset of set b')
# else:
#       print(f'set a is not superset of set b')

#to add something in set
# a={1,2,3,4,5}
# a.add(6)
# print(a)

# a={1,2,3,4,5}
# a.discard(3)
# print(a)

# a={1,2,3,4,5}
# a.pop()
# print(a)


# a={1,2,3,4,5}
# b={4,5,6,7,8}
# print(a-b)
# print(b-a)

# a={1,2,3,4,5}
# b={4,5,6,7,8}
# print(a|b)#print all the elements in both set
# print(a&b) #prints common in both set
# print(a^b) #prints elements in either set but not in both


#merge two dictionaries inbto one\
d1={"a":1,"b":2,"c":3}
d2={"d":4,"e":5,"f":6}
# d1.update(d2)
# print(d1)


for i in d2:
    d1[i]= d2[i]
print(d1)


#sum of all the values in dictionary
d1={"a":1,"b":2,"c":3}
sum=0
for i in d1:
    sum+=d1[i]
print(f'the sum of all the values in dictionary is {sum}')
   