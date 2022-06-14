#task1
n=2
z=""
st=""
for i in range(1,n+1):
    st=st+str(i)
    print(st)
num=n+1
for i in range(1,n+1):
    z=str(z)+str(num-i)
    print(z)

#task2
n=5
st=""
num=n+1
for i in range(1,n+1):
    st=st+"#"+str((num-i)*2)
    print(st)

#task3
my_list1=[1,5]
my_list2=[9,7]
my_list3=my_list1 +my_list2
len1=len(my_list3)
new_list=[]
max=my_list3[0]
min=my_list3[0]
for i in range(0,len1):
    st=my_list3[i]
    if(max<st):
        max=st
    if(min>st):
        min=st
print(min+max)

#task4
my_list=[9,44,100,104]
len1=len(my_list)
z=''
for i in range(0,len1):
    st=my_list[i]
    if(st>=3 and st<=99):
        if(st%3==0)or (st%4==0) or (st%12!=0):
            if (z == ""):
                z +=str(st)
            else:
                z = z + "," + str(st)
print(z)



