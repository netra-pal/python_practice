# #task1
# st="#@$%^&:[]=@hbQ"
# length=len(st)
# count=0
# for i in range(0,length):
#     ch=st[i]
#     if(ch>="a"and ch<="z"):
#         count=count
#     elif(ch>="A" and ch<="Z"):
#         count=count
#     elif(ch>="0" and ch<="9"):
#         count=count
#     else:
#         count+=1
#
# print("special :" , count)

# #task3
# st="1234567890"
# len1=len(st)
# newstr=""
# for i in range(0,len1):
#     ch=st[i]
#     if(ch=="1" ):
#         newstr=newstr+"A"
#     elif(ch=="2"):
#         newstr+="b"
#     elif(ch=="3"):
#         newstr+="c"
#     elif(ch>="4" and ch<="9"):
#         newstr+="x"
#     else:
#         newstr+=ch
# print(newstr)

#task4
# st="BAD CAR"
# len1=len(st)
# newst=""
# for i in range(0,len1):
#     ch=st[i]
#     if(ch=="A"):
#         newst+="B"
#     elif(ch=="B"):
#         newst+="A"
#     elif(ch=="C" or ch=="D"):
#         newst=newst
#     else:
#         newst+=ch
# print(newst)

#TASK6
# st="AbCdEf"
# newstr=""
# newst=""
# len1=len(st)
# for i in range(0,len1):
#     ch=st[i]
#     if(i%2==0):
#         newst=newst+ch
#     else:
#         newstr+=ch
# print("odd :",newstr)
# print("even :",newst)

# task8
# str="job ready"
# val=str.split()
# for i in val:
#      print(i)

# task9
# str="java ready go"
# val=str.split()
# for i in val:
#     print(i)

#task10
st="My Name is"
len1=len(st)
z=""
for i in range(0,len1):
    ch=st[i]
    if(ch>="A" and ch<="Z"):
        z=z+chr(ord(ch)+32)
    else:
        z=z+ch
print(z)

#task11
st="Hello"
len1=len(st)
z=""
for i in range(0,len1):
    ch=st[i]
    if(ch>="a" and ch<="z"):
        z=z+chr(ord(ch)-32)
    else:
        z=z+ch
print(z)

#task12
st="Trisect"
len1=len(st)
z=""
for i in range(0,len1):
    ch=st[i]
    if(ch>="a" and ch<="z"):
        z = z + chr(ord(ch) - 32)
    elif(ch>="A" and ch<="Z"):
        z=z+chr(ord(ch)+32)
    else:
        z+=ch
print(z)

#task7
b="dada"
b1=b[len(b)//2:]             #b[2:]
b2=b[0:len(b)//2]            #b[0:2]
if(b1+b1==b):
    print("Yes")
else:
    print("No")

#task2

a,b,c = '123','','' # 1#12#123#
for i in a:b += c+"#"
print(b)

s = 'java'
len = len(s)
if len%2:
    print(s[(len//2)+1:]+s[(len//2)]+s[0:len//2])
else:
    print(s[len//2:]+s[0:len//2])
