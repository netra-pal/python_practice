#task7
# count=0
# def check(st):
#     global count
#     if st and st[0]>="a"  and st[0]<="z":
#         count+=1
#
#     if st:
#         check(st[1:])
#     else:
#         print(count)
#
# check("x1x2x3x")

#task8
# count=0
# def check(st):
#      global count
#      if st and st[0]>="a" and st[0]<="z":
#          count+=1
#      if st:
#         check(st[1:])
#      else:
#          print(count)
# check("x1Y12ab")

#task9
# count=0
# def checkc(st):
#     global count
#     if st and (st[0]=="a" or st[0]=="b"):
#         count+=1
#     if st:
#         checkc(st[1:])
#     else:
#         print(count)
#
# checkc("abcd123gfh")

#task11
# count=0
# def checkc(st):
#     global count
#     if st and st[0]=="5":
#         count+=1
#     if st:
#         checkc(st[1:])
#     else:
#         print(count)
#
# checkc("55555")

# #task10
# sum=0
# def summ(n):
#     global sum
#     if n:
#         m=n%10
#         n=n//10
#         sum=sum+m
#         summ(n)
#     else:
#         print(sum)
#
# summ(409)

#task12
# st2=""
# def check(st):
#     global st2
#
#     if st and (st[0]>="1" and st[0]<="9"):
#         pass
#     elif st:
#         st2+=st[0]
#     if st:
#         check(st[1:])
#     else:
#         print(st2)
#
# check("x1Y2Zqw#")

#task13
# st2=""
# def check(st):
#     global st2
#
#     if st and (st[0]>="1" and st[0]<="9"):
#         st2+="#"
#     elif st:
#         st2+=st[0]
#     if st:
#         check(st[1:])
#     else:
#         print(st2)
#
# check("@4mn8")

#task14
# st2=""
# def check(st):
#     global st2
#
#     if st:
#         st2+=st[0]+"#"
#     if st:
#         check(st[1:])
#     else:
#         print(st2)
#
# check("java")

#task15
# st2=""
# st3=""
# def check(st):
#     global st2
#     global st3
#
#     if st and (st[0]>="1" and st[0]<="9"):
#         st3+=st[0]
#     elif st:
#         st2+=st[0]
#     if st:
#         check(st[1:])
#     else:
#         print(st2+st3)

# check("@#34**5")

#task17
# st2=""
# def check(st):
#     global st2
#
#     if st and st[0]=="1":
#         st2+="x"
#     elif st and st[0] == "2":
#         st2+="y"
#     elif st and st[0] == "3":
#         st2+="z"
#     elif st:
#         st2+=st[0]
#     if st:
#         check(st[1:])
#     else:
#         print(st2)
#
# check("9812398123")

#task18
# st2=""
# def check(st):
#     global st2
#     if st:
#         st2=st[0]+st2
#     if st:
#          check(st[1:])
#     else:
#         print(st2)
#
# check("12345")

#task


