#operation for sets 
# question 1 to find the difference between 2 sets we can use - operator

# a={1,2,3,4,5}
# b={4,5,6,7,8}
# print(a-b)
# print(b-a)
# print(a)
# print(b)


#question 2 to find the difference between 2 sets and update them 
# a={1,2,3,4,5}
# b={3,4,5,6,7,}
# a-=b
# print(a)


#question 3 intersection (to find the common items between 2 sets we can use & operator) (& operator )
# a={1,2,3,4,5}
# b={4,5,6,7,8}
# a&=b
# print(a)


#question 4 to check subset 
# a={1,2,3,4,5}
# b={4,5,6,7,8}
# s={1,2,3}
# print(s<=a)
# print (f"the {s} is subset of {a} ")


# question 5 to check the superset 
# a={1,2,3,4,5,}
# b={3,4,5,6,7,8}
# s={1,2,3,}

# print(a>s)
# print(f"{a} is superset of {s}")


# question 6 to find the largest no in an array 
# a=[1,2,3,4,5,6,7,8,9,10]
# lar=0
# for i in a:
#     if i>lar:
#         lar=i
# print(f'the largest no in the array is {[lar]}')

#to find the second largest no in an array 
# a=[1,2,3,4,5,6,7,8,9,10]
# lar=0
# sec_lar=0
# for i in a:
#     if i>lar:
#         sec_lar=lar
#         lar=i
# print(f'the second largest no in the array is {[sec_lar]}')


#question 7 to find the even and odd no in an array
# a=[1,2,3,4,5,6,7,8,9]
# even=[]
# odd=[]
# for i in a:
#     if i%2==0:
#         even.append(i)
#     else:
#         odd.append(i)
# print(f"the odd no in the array is {odd}")
# print(f"the even no in the array is {even}")

#question 8 to find the sum of odd and even no in an array
# a={1,2,3,4,5,6,7,8,9}
# even=0
# odd=0
# for i in a:
#     if i%2==0:
#         even=even+i
#     else:
#         odd=odd+i
# print(f"the sum of odd no in the array is {[odd]}")
# print(f"the sum of even no in the array is {[even]}")


#to find that the word is palindrome or not
# word=input("enter the word ")
# pal=''
# for i in range(len(word)-1,-1,-1):
#     pal+=word[i]
# if pal==word:
#     print(f"the word {word} is palindrome")
# else:
#     print(f"the word {word} is not palindrome")





# to check whether the no is palindrome or not
a=input("enter the no")
rev=""
for i in range(len(a)-1,-1,-1):
    rev+=a[i]
if rev==a:
    print(f"the no {a} is palindrome")
else:
    print(f"the no {a} is not palindrome")