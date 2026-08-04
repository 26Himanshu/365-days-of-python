# Random no guessing game

# import random 

# com=random.randint(1,100)
# trie=0

# while True:
#     trie = trie + 1
#     hum=int(input("guess your no between 1 to 100"))

#     if hum==com:
#             print (f"you won the game in {trie}")
#             break
#     elif hum>com:
#             print("sorry wrong guess go lower")
#     elif hum<com:
#             print("sorry wrong guess go higher")



#
# import random 
# com=random.randint(1,100)
# tries=0


# while True:
#     hum=int(input("guess your no between 1 to 100"))
#     count+=1
#     if hum==com:
#         print (f"you won the game in {tries} count")
#         break
#     elif hum>com:
#         print('sorry wroong guess go lower')
#     elif hum<com:
#         print("sorry wrong guess go higher")
        

#creating file management system CRUD operations
#create file , read file , update file , delete file

# from pathlib import Path
# import os
# def createfile():
#     try:
#         name=input("enter the file name:-")
#         path=Path(name)
#         if not path.exists():
#             with open(path,"w") as fs:
#                 data=input("what you want to write")
#                 fs.write(data)
#             print("file created successfully")
#         else:
#             print("file already exists")
#     except Exception as err:
#         print(f"error is {err}")            
# def readfile():
#     try:
#         name=input("enter the file name:-")
#         path=Path(name)
#         if path.exists():
#             with open(path,"r") as fs:
#                 content=fs.read()
#                 print(f"the content of the file is {content}")
#         else:
#             print("file does not exists")
#     except Exception as err:
#         print(f"error is {err}")
# def updatefile():
#     try:
#         name=input("enter the file name")
#         path=Path(name)
#         if path.exists():
#             print("operations")
#             print("1.rename file")
#             print("2.appending file content")
#             print("3.overwrite file content")
#             choice=int(input("enter your option"))
#             if choice==1:
#                 new_name=input("enter the new namne")
#                 new_path=path(new_name)
#                 if not new_path.exists():
#                     path.rename(new_path)
#                 else:
#                     print("file already exists")
#             elif choice==2:
#                 with open(path,"a") as fs:
#                     data=input("enter the data to append")
#                     fs.write("\n" + data)
#                 print("data appended successfully")
#             elif choice==3:
#                 with open(path,"w") as fs:
#                     data=input("enter the data to overwrite")
#                     fs.write(data)
#                 print("data overwritten successfully")
#     except Exception as err:
#         print(f"error is {err}")
# def deletefile():
#     try:
#         name=input("enter the file name")
#         path=Path(name)
#         if path.exists():
#             path.unlink()
#             print("file deleted successfully")
#         else:
#             print("file does not exists")
#     except Exception as err:
#         print(f"error is {err}")
# print("press 1 for creating a file")
# print("press 2 for reading a file")
# print("press 3 for updating a file")
# print("press 4 for deleting a file")
# a=int(input("\n enter your choice:-"))
# if a==1:
#     createfile()
# if a==2:
#     readfile()
# if a==3:
#     updatefile()
# if a==4:
#     deletefile()