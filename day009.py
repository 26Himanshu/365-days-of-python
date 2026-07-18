#to add something in dictionary 
# d={1:10,2:20,3:30}
# d[4]=40
# print(d)
#to read the value of key in dictionary
# d={1:10,2:20,3:30}
# print(d[2])
#to update the value of key in dictionary
# d={1:10,2:20,3:30}
# d[1]=100
# print(d)

#to clear in dictionary 
# d={1:10,2:20,3:30}
# d.clear()
# print(d)

# to make a new dictionary 
# d={1:10,2:20,3:30}
# a=d.fromkeys([1,2,3],0)
# print(a)
# print(d)


# d={1:10,2:20,3:30}
# print(d.get(1))
# print(d)
# print(d.pop(1))
# print(d.items())
# print(d.keys())
# a=d.fromkeys([1,2,3,4],550)
# print(a)
# print(d)

# a={1:10,2:20,3:30}
# for i in a:
#     print(f'key {i}:value {a[i]}')



#merge two dictionaries into one
d1={"a":1}
d2={"b":2}
# d1.update({"b":2})
# print(d1)
# print(d2)
#alternate
# d1={"a":1}
# d2={"b":2}
# for i in d2:
#     d1[i]=d2[i]
# print(d1)


#sum of all values in dictionary 
# d={"a":1,"b":2,"c":3}
# sum=0
# for i in d:
#     sum+=d[i]
# print(sum)

#question 3 counting the frequency of each and put hem into dictionary 
# a=['a','b','c','a','b','a']
# d={}
# for i in a:
#     if i in d.keys():
#         d[i]=d[i]+1
#     else:
#         d[i]=1
# print(d)


#question 
d1={"a":1,"b":2,"c":3}
d2={"c":4,"e":5,"f":6}
for i in d2:
    if i in d1.keys():
        d1[i]=d1[i]+d2[i]
    else:
        d1[i]=d2[i]
print(d1)