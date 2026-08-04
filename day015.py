#to find the differenece between two sets

# a={1,2,3,4,5}
# b={1,2,3,4,5,6,7,8}
# (a-b)
# print(a)
# print(b)


#to check the subset 
# a={1,2,3,4,5}
# b={1,2,3,4,5,6,7,8}
# if a<=b:
#     print(f'a is subset of b')
# else:
#     print(f'a is not subset of b')


#to check the superset 
# a={1,2,3,4,5}
# b={1,2,3}
# if a>=b:
#     print(f'a is superset of b')
# else:
#     print(f'a is not superset of b')


#to find that the word is palindrome or not
# word=input('enter the word:-')
# rev=''
# for i in range(len(word)-1,-1,-1):
#     rev+=word[i]
    
# if word==rev:
#     print(f'{word} is a palindrome')
# else:
#     print(f'{word} is not a palindrome')


#to find the square of every no
# a=[1,2,3,4,5,6,7,8,9]
# squ=[]
# for i in a:
#     squ.append(i**2)
# print(squ)


#print both elements of both sets
# a={1,2,3,4,5}
# b={342,35,6,36,27,474,83,58}
# a|=b
# print(a)
# print(a&b)


#find the sum of all the values in dict
# a={"a":1,"b":2, "c":3}
# sum=0
# for i in a:
#     sum=sum+a[i]
# print(f'the sum of all the values in dict is {sum}')


# merge two dictionary 
a={"a":1,"b":2, "c":3}
b={"d":4,"e":5, "f":6}
a.update(b)
print(a)


#
a={"a":1,"b":2, "c":3}
sum=0
for i in a:
    sum+=a[i]
print(f'the sum of all the values in dict is {sum}')
