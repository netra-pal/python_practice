# def power(n,m):
#     z=''
#     if(m%2==0):
#         z=n*n*n
#     else:
#         z=n*n
#     return z
#
# def powerfun(list1):
#     len1=len(list1)
#     for i in range(0,len1):
#         ch=list1[i]
#         m=power(ch,ch)
#         return m
#
# def sumpower(listt):
#     sum=0
#     len1=len(listt)
#     for i in range(0,len1):
#         ch=listt[i]
#         m=power(listt[i],int(i))
#         sum+=m
#     print(sum)
#
# sumpower([3,4])
#
# def moveChar(st,n):
#     len1=len(st)
#     str=""
#     val=''
#     for i in range(0,len1):
#         ch=st[i]
#         if(ch==n):
#             val+=ch
#         else:
#             str+=ch
#     return (str+val)
#
# def movefun(list1):
#     len1=len(list1)
#     z=""
#     for i in range(0,len1):
#         ch=list1[i]
#         z=moveChar(ch,ch[0])
#         print(z)
# movefun(["dad","car"])
