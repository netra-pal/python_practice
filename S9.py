#task1
# listt=[10,20,35,25,30,55]
# len1=len(listt)
# count=0
# z=''
# for i in range(0,len1):
#     ch=listt[i]
#     if(ch%5==0 and ch%10!=0):
#         count+=1
#         if (z == ""):
#             z += str(ch)
#         else:
#             z = z + "," + str(ch)
#
# print("size:",count)
# print(z)

#task2
listt=["hello","how","are","you!!"]
st=""
len1=len(listt)
for i in range(0,len1):
    ch=listt[i]
    for j in ch:
        if j not in st:
            st+=j
print(st)

#tassk3
# list1=[10,20,30,20,40,50]
# len1=len(list1)
# z=""
# myset=set()
# for i in range(0,len1):
#     ch=list1[i]
#     if ch in myset:
#         z+=str(ch)
#     myset.add(ch)
# print(z)
