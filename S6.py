#task1
# def countInrange(st):
#     count=0
#     len1=len(st)
#     for i in range(0,len1):
#         ch=st[i]
#         if((ch>="a" and ch<="d" ) or (ch>="A" and ch<="D")):
#             count+=1
#     return ("in range :"+str(count))
#
# def countLRange(list):
#     count=0
#     len1=len(list)
#     for i in range(0,len1):
#         ch=list[i]
#         z=countInrange(ch)
#         print(z)
#
# countLRange(["test","caR","abacas"])

#task3
# def extractsLists(list1,list2):
#     listt=list1+list2
#     sum=0
#     for i in listt:
#         if(i>=25 and i<=75):
#             sum+=1
#     print(sum)
# #task4
# def pattern(n):
#     for i in range(1,n+1):
#         if(i%2==0):
#             z=n*"*"+str(i)
#         elif(i%1==0):
#             z=str(i)+n*"*"
#         print(z)
#
# pattern(4)
#
# def decode(st,n):
#     z=""
#     for i in st:
#         if(n==0):
#             if(i=="#"):
#                 z=z+"a"
#             elif(i=="*"):
#                 z+="e"
#             else:
#                 z=z+i
#         elif(n==1):
#             if(i=="#"):
#                 z=z+"i"
#             elif(i=="*"):
#                 z+="o"
#             else:
#                 z+=i
#         else:
#             z=st
#
#     print(z)
#
# decode("c#r*",)