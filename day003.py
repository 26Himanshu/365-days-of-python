#question 1 find the largest no in the list
#METHOD 1
# a=[34,6,234,4634,23,432,54,5574,87645,2342,34]
# a.sort()
# print(f'the largest no is {a[-1]}')


#METHOD 2
# lar=0
# for i in a:
#     if i>lar:
#         lar=i
# print(f'the largest no is {lar}')


#QUESTION 2 TO ADD A NO IN THE LIST 
# A= [10,20,30,40,50]
# A.append(60)
# print(A)

#question 3 to add a no in the list to a position (index)
# a=[2412,3523,123523,235235,54,32542,3446745,72]
# a.insert(2,3456)   # 2 is the index no and 3456 is the value to be added in the list
# print(a)

#question 4 to remove a no from the list
# a=[10,20,30,40,50]
# a.pop() #pop laat value will be removed from the list
# print(a)


#question 5 to remove a no from the list 
# a=[213,43256,2365,2354,35313,23421365,2]
# a.remove(213)
# print(a) 


#question 6 to remove all the element in the list
# a=[10,20,30,40,50]
# a.clear()
# print(a)


#question 7 to find the second largest no in the list
#method 1
# a=[10,20,45456,35235,64364,233,46376,67237]
# a.sort()
# print(f'the second larget no is {a[-2]}')

#method 2
# a=[10,20,45456,35235,64364,233,46376,67237]
# larg=0
# sec_larg=0
# for i in a:
#     if i>larg:
#         sec_larg=larg
#         larg=i
# print(f'the second largest no is {sec_larg}')


#question 8 to print sum of odd and even no in the list seperately
# a=[10,20,30,40,50,45345,46346,2352,5627,54,574235,57457457,54575745]
# odd=[]
# even=[]
# for i in a:
#     if i%2==0:
#         even.append(i)
#     else:
#         odd.append(i)

# print(f'the sum of even no is {sum(even)}')
# print(f'the sum of odd no is {sum(odd)}')

# print(f'the even list is {even}')
# print(f'the odd list is {odd}')


# question 9 to print all the positive and negative no in the list`
# a=[4214,45646,235235,-5636,-64325,35423,-6536236]
# pos=[]
# neg=[]
# for i in a:
#     if i>0:pos.append(i)
#     else:neg.append(i)
# print(f'the positive no in the list are {pos}')
# print(f'the negative no in the list are {neg}')

# print(f'the sum of positive no are {sum(pos)}')
# print(f'the sum of negative no are {sum(neg)}')


#question 10 to find the heightest no and print the square of it 

# a=[10,20,30,40,50,60,70,80,90,100]
# highest=0
# for i in a: 
#     if i>highest:
#         highest=i
#         i=i*i       
# print(i)


#uestion 11 to find the lowest no and how much it is less from heightes no 
# a=[10,20,30,40,50,60,70,80,90,100]
# a.sort()
# print(f'the lowest no is {a[0]}  top  no is {a[9]}')
# print (f"the difference is {a[9]-a[0]}")

#to check how many time tuesday is coming in the tuple
# a=["monday","tuesday",244,25235,4646 ,1,1,1,1,2,2,3,53,6,856,"tuesday"]
# a.count("tuesday")
# print(a.count("tuesday"))