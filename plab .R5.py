#task2
my_list1=[1,2]
my_list2=[3,4,5]
count=0
my_listt=my_list1+my_list2
len1=len(my_listt)
new_listt=[]
for i in range(0,len1):
    st=my_listt[i]
    if(st%2!=0 and st%3!=0):
        count=count +1
    if(st%2!=0 and st%3!=0):
        new_listt.append(st)
    print("New list size :", count)
    print(st)



# #task2
# n=4
# pattern=""
# z=""
# num=n+
