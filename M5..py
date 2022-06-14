# n=input("entre the no:")
# a=True
# for i in range(2,int(n)):
#         if(int(n)%i==0):
#             a=False
#             break
#
# if a :
#     print("prime")
# else:
#     print("not prime")

#task2
# n=10
# for n in range(2,11):
#     a= True
#     for i in range(2, int(n)):
#         if(int(n)%i==0):
#             a=False
#             break
#
#     if a :
#         print(n)

#task3 wrong question
# `n=int(input("enter the no:"))
# if(n%3==0):
#     print("buzz")
# elif(n%15==0):
#     print(f)

#Task4
# wrong question
#
# #task5
# n=256
# for i in range(n):
#     temp=2**i
#     if(temp==n):
#         print("yes")
#         break
#     elif (temp>n):
#         print("No")
#         break

# #task6 (do in for loop)
# st="1#2##3###hello"
# while "##" in st:
#     st=st.replace("##","#")
# print(st)

#task9
# n=4
# st=""
# z=""
# for i in range(1,n+1):
#     z+=str(i)
#     st=("X"*i)+z
#     print(st)

#task11
# n=str(29013)
# sum=0
# for i in n:
#     sum+=int(i)
# print(sum)
#
# #task12
# list=[10,25,456,67]
# for i in list:
#     sum=0
#     z=str(i)
#     for j in z:
#         sum+=int(j)
#     print(sum)

#task13
# n=8
# z=bin(n).replace("0b","")
# print(z)

#task14
# list=[2,-5,4,12,-7,-9,6,3,-10]
# listt=[]
# z=[]
# for i in list:
#     if(i>=0):
#         listt.append(i)
#     elif(i<=0):
#         z.append(i)
# print(listt+z)

# #task16
# n="10000"
# z=int(n,2)
# print(z)

#task18
# list=[2,0,4,0,6,8,0,0,10,12]
# listt=[]
# z=[]
# for i in list:
#     if (i>0):
#         listt.append(i)
#     elif(i==0):
#         z.append(i)
# print(listt+z)

#task17
# st="1234"
# if (st[-1]=="9"):
#     z=st[-2]


#task17
# val = "589"
# temp = val
# len = len(val)
# st = ""
# while val:
#     if val[-1] !="9":
#         st = chr(ord(val[-1])+1)+st
#         val = val[0:-1]
#         break
#     else:
#         val = val[0:-1]
#         st += "0"
# if val or (len == 1 and temp !="9") :
#     print(val+st)
# else:
#     print("1"+st)

#task15
# list=[1,5,3,8,7,6,4,1,2]
# z=[]
# for  i in range(0,len(list)):
#     for j in range(i+1,len(list)):
#         if(list[i]<list[j]):
#             break
#         if (j+1==len(list)):
#             z.append(list[i])
# if list[-1] not in z:
#     z.append(list[-1])
# print(z)

#task7
# n=83
# z=["zero","one","two","three","four","five","six","seven","eight",
#    "nine","ten","eleven","twelve","thirteen","fourteen","fifteen","sixteen",
#   "seventeen","eighteen","nineteen","twenty" ]
# y=["zero","one","twenty","thirty","fourty","fifty","sixty","seventy","eighty","ninety"]
# if (n<=20):
#     print(z[n])
# else:
#     st = ''
#     st += y[int(str(n)[0])]
#     st +=" "+ z[int(str(n)[1])] if str(n)[1] != '0' else ""
#     print(st)

#task8
# n=110
# st=""
# z=["zero","one","two","three","four","five","six","seven","eight",
#    "nine","ten","eleven","twelve","thirteen","fourteen","fifteen","sixteen",
#   "seventeen","eighteen","nineteen","twenty" ]
# y=["zero","ten","twenty","thirty","fourty","fifty","sixty","seventy","eighty","ninety"]
# x=["zero","one hundred","two hundred","three hundred","four hundred","five hundred","six hundred","seven hundred","eight hundred"
#    "nine hundred"]
# if (n<=20):
#     print(z[n])
# elif n >20 and n < 100:
#     st = ''
#     st += y[int(str(n)[0])]
#     st +=" "+ z[int(str(n)[1])] if str(n)[1] != '0' else ""
#     print(st)
# else:
#     if(str(n)[1]=='0'):
#         st = x[int(str(n)[0])]+" "+z[int(str(n)[2])]
#     elif(str(n)[2]=='0'):
#         st=x[int(str(n)[0])]+" "+y[int(str(n)[1])]
#     else:
#        st= x[int(str(n)[0],)]+" "+y[int(str(n)[1])]+" "+z[int(str(n)[2])]
# print(st)

#task10
# n=2
# x=5
# sum=0
# z=0
# for i in range(1,x+1):
#     # z+=i*n
#     temp = i
#     for j in range(n-1):
#         temp *= i
#     z +=temp
# print(z)
#
