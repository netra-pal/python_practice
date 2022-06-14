# #task2
# # st="trisect"
# # len1=len(st)
# # z="first3:"+(st[0:3])
# # x="last3:"+(st[-3:])
# # print(z)
# # print(x)
#
# #task3
# # st="ABC"
# # len1=len(st)
# # if len1%2!=0:
# #     print("First half: "+ st[0:len1//2])
# #     print("Middle half :"+st[len1//2])
# #     print("Last half :"+st[len1//2+1:])
# #
# #
# # else:
# #     print("First half:"+st[0:len1//2])
# #     print("Second half:"+st[len1//2:])
#
# #task4
# # st="trisect"
# # len1=len(st)
# # x=(st.find("t"))
# # y=(st.find("t",x+1))
# # print("first:"+str(x))
# # print("second:"+str(y))
#
# #task5wrong
# st="00"
# a=True
# x=(st.find("0"))
# y=(st.find("0",x+1))
# z=(st.find("0",y+1))
#
#
#
# if x !=-1:print("first:"+str(x))
# else:print("not found")
#
# if y !=-1 and x != -1:print("first:"+str(y))
# elif x!=-1 and y ==-1:print("not found")
#
# if z !=-1 and y !=-1:print("first:"+str(z))
# elif x!=-1 and y !=-1 and z ==-1:print("not found")
# print("ap II \n\n")
# if "0" in st:
#     print("first : ",x)
#     if "0" in st[x+1:]:
#         print(y)
#         if "0" in st[y+1:]:print(z)
#         else:print("not found")
#     else:print("not found")
# else:print("not found")
#task6
# st = "A+X=20"
# lst = st.split("X")
# len = len(lst)
# print("First ",end = "")
# if len>=1:
#     print(lst[0])
# else:
#     print("")
#
# # print("First : ",lst[0] if len>=1 else "")
# print("Second  : ",lst[1] if len>=2 else "")

#task9.2
# n=(input("Enter the Alphabet:"))
# if n=="a":
#     print("apple")
# elif n=="b":
#     print("boy")
# elif n=="c":
#     print("cat")
# else:
#     print("none")
#task10
# st1="1234568"
# st2="1234567"
# if len(st1)>len(st2):
#     print (st1)
# elif len(st2)>len(st1):
#     print(st2)
# else:
#     for i in range(0,len(st1)):
#         if(ord(st1[i])>ord(st2[i])):
#             print(st1)
#             break
#         elif(ord(st1[i])<ord(st2[i])):
#             print(st2)
#             break

#task11
# st="I am fine"
# s=""
# z=st.split(" ")
# count=len(z)
# print("no of words:"+str(count))
# for i in z:
#     s=str(i)+"="+str(len(i))
#     print(s,end=" ")

#task12
# st="1234"
# for i in st:
#     print(i,end="")

#task14
# st="HELLO"
# a=False
# for i in range(0,len(st)-1):
#     if st[i]==st[i+1]:
#         a=True
#         break
# if a:
#     print("consecutive:"+"True")
# else:
#     print("consecutive:"+"False")

#task8
# n=8
# z=["zero","one","two","three","four","five","six","seven","eight","nine"]
# print(z[n])

#task9
# n=5
# z={1:"jan",2:"feb",3:"mar",4:"april",5:"may",6:"june",7:"july",8:"aug",9:"sept",10:"oct",11:"nov",12:"dec"}
# print(z[n])