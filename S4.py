# def multipleOf3(n):
#     z=""
#     if(n%3==0):
#         z=str(n)+": yes"
#     else:
#         z=str(n)+": no"
#     return z
#
#
# def func2(my_list):
#     len1=len(my_list)
#     for i in range(0,len1):
#         element=my_list[i]
#         print(multipleOf3(element))
#
# func2([21,4,23,434,44])

#task2
# list=[10,0,3,4,5]
# len1=len(list)
# count=0
# mylist=[]
# for i in range(0,len1):
#     ch=list[i]
#     if(ch//5==0):
#         count+=1
#     else:
#         count=count
# print("size :",count)
# for i in range(0,len1):
#     ch = list[i]
#     if(ch==0):
#         list[i]=99
#         print(list)
#
#task3
# def grades(n):
#     if(n>=90):
#         z="Grade A"
#     elif(n>=75):
#         z="Grade B"
#     elif(n>=40):
#         z="Grade C"
#     else:
#         z="Fail"
#
#     return z
#
# def subFunc(list):
#     len1=len(list)
#     for i in range(0,len1):
#         element=list[i]
#         t=grades(element)
#         print("subject#"+str(i+1)+'\n',t)
#
# subFunc([78,75,40,39,99])

#task4
# st="tool"
# b1=st[len(st)//2:]
# b2=st[0:len(st)//2]
# z=b1+"#"+st+"#"+b2
# print(z)

