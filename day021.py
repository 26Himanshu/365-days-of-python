#code with harry 
print("hello himanshu this side \n I am learning python from code with harry")


print("hello himanshu this side'and i am himanshu'")

#random no guessing game

import random
com=random.randint(1,100)
tries=0

while True:
    tries+=1
    hum=int(input("enter the no between 1 to 100:-"))
    if com==hum:
        print(f"you won the game in {tries} tries")
        break
    elif com>hum:
        print("sorry wrong guess go higher")
    elif com<hum:
        print("sorry wrong guess go lower")


<<<<<<< HEAD


=======
>>>>>>> fb60c22 (copy past)
#how to print table 

n=int(input("enter the no"))
for i in range(n,n*10+1,n):

print(i)