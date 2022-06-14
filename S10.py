# list1=[1,2,3,4,5,6]
# list2=[9,8,7,6,5]
# list1.extend(list2)
# for i in list1:
#     print(i)

# list1=[9,9,9,9,1,2,3,9]
# length=len(list1)
# listt=set()
# for i  in range(0, length):
#     n=list1[i]
#     listt.add(n)
# print(listt)

#task4
list1=[1,2,3,2,4,5,1,6,1]
myset=set()
st=""
for i in range(0,len(list1)):
    ch=list1[i]
    if ch in myset:
        if str(ch) not in st:
            st+=str(ch)
    myset.add(ch)
print(st)


