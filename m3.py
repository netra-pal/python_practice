# # #task1
# # mylist=[4,14,6,12,345,5,1]
# # len1=len(mylist)
# # scount=0
# # for i in range(0,len1):
# #     ch=mylist[i]
# #     if(ch>0 and ch<10):
# #         scount=scount+1
# #     else:
# #         scount=scount
# # print("Single Digit:",scount)
# #
# #task2
# # my_list=[4,8,12,20,6]
# # len1=len(my_list)
# # max=my_list[0]
# # newlist=[]
# # if(max<my_list[len1-1]):
# #         max=my_list[len1-1]
# # for i in range(0,len1):
# #     newlist+=[max]
# # print(newlist)
#
# # task3
# # input1=[1,2,3,9,4,5,6]
# # z=0
# # a=0
# # for i in input1:
# #     if(i%2==0):
# #         if a<2:a=0
# #         z+=1
# #     else:
# #         if z<2:z=0
# #         a+=1
# #
# #     if (z >= 2 and a>=2):
# #         print(True)
# #         break
#
#task4
# input1=[1,2,3,4,5,6]
# z=0
# a=0
# for i in input1:
#     if(i%2==0):
#         if a<2:a=0
#         z+=1
#     else:
#         if z<2:z=0
#         a+=1
#
#     if (z >= 2 and a>=2):
#         print(True)
#         break
#
#
# # #task8
# # m=[1,2,3]
# # x=[4,5,6,7]
# # m.extend(x)
# # print(m)
#
#task9
# list=["c","car","bis","going","aaa"]
# len1=len(list)
# count=0
# z=''
# for i in range(0,len1):
#     ch=list[i]
#     if ch.startswith(("a","b","c")):
#         count+=1
#         if(z==""):
#             z+=ch
#         else:
#             z=z+"," +ch
#
# print(count)
# print(z)


#task10
# list1=["Trisect","Java","Man"]
# len1 = len(list1)
# newst = ""
# for i in range(0, len1):
#     ch = list1[i]
#     newst+=ch[0]
# print(newst)

#task13
# list1=[1,2,3,4,5]
# len1=len(list1)
# num=(len1-1)
# newlistt=[]
# for i in range(0,len1):
#     newlistt.append(list1[num])
#     num-=1
# print(newlistt)

# #task14
# list1=[1,2,3,4]
# list2=[5,6,7,8]
# len1=len(list1)
# temp=[]
# for i in range(0,len1):
#     temp.append(list1[i])
#     temp.append(list2[i])
#     print(temp)


#task11
# list1=["trisect","java","maste"]
# len1=len(list1)
# newlistt=[]
# for i in range(0,len1):
#     ch=list1[i]
#     if(ch[-1]=="e" or ch[-1]=="t"):
#             newlistt.append(ch)
# print(newlistt)

# #task12
# list1=["java","master","job","ready","java"]
# while('java' in list1):
#     list1.remove("java")
# print(list1)

#task15
# listt=[1,2,4,5,7,8,10,12]
# len=len(listt)
# for i in range(0,len):
#     if(listt[i]>5):
#         if(listt[i]%5!=0 ):
#             listt[i]=listt[i]-(listt[i]%5)
# print(listt)

#task16
list1=[1,2,3,4,5,6,7,8]
len1=len(list1)
z=''
for i in range(1,len1-1):
    if list1[i-1]%2 !=0 and list1[i+1]%2 !=0 and list1[i]%2==0:
        if (z == ""):
            z += str(list1[i])
        else:
            z = z + "," + str(list1[i])
print("surrounded=",z)