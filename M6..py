#task1
# # n=5
# st=""
# for i in range(1,n+1):
#     st+=str(i)
#     print(st)

#task2
# n=5
# st=""
# for i in range(1,n+1):
#     if(i%2==0):
#         st+="0"
#     else:
#         st+="1"
#     print(st)

#task3
# n=5
# st=""
# st1=""
# for i in range(1,n+1):
#     st+=str(i)
#     st1="*"*i
#     print(st+st1)

#task4
# n=4
# st=""
# num=n+1
# z=""
# for i in range(1,n+1):
#     st+=str(i)
#     print(st)
# for j in range(1,n+1):
#     st=(int(st)-(num-i))
#     print(st)

#task 5
# n=5
# for i in range(n):
#     for j in range (i+1):
#         print(n-j,end=" ")
#     print()

#task6
# n=5
# for i in range(n):
#     for j in range(i+1,0,-1):
#         print(j,end="")
#     print()

# #task7
# n=5
# for  i in range(n):
#     for j in range(i+1):
#         print(n-j,end="")
#     print()
#task8
# n=5
# for i in range(n):
#     for j in range(i+1):
#         print(i+1,end="")
#     print()`
#task9
# n=5
# for i in range(5,0,-1):
#     for j in range(1,i+1):
#         print(j,end="")
#     print()
# #task10
# n=5
# for i in range(n):
#     for j in range(n,i,-1):
#         print(j,end="")
#     print()

#task11
# n=5
# for i in range(n):
#     for j in range(n,i,-1):
#         print(j-i,end="")
#     print()

#task12
# n=5
# for i in range(1,n+1):
#     for j in range(i,i+n):
#         if j%2!=0:
#             print('1',end="")
#         else:
#             print("0",end="")
#     print()

#task13
n=5
# for i in range(1,n+1):
#     for j in range(i,i+n):
#         if j<=5:
#             print(j,end="")
#         else:
#             print(j-5,end="")
#     print()

#task14
# n=5
# for i in range(1,n+1):
#     for j in range(n):
#         if j<n-i:
#             print(1,end="")
#         else:
#             print(i,end="")
#     print()

#task15
n=5
for i in range(1,n+1):
    for j in range(1,n+1):
        if i==j:
            print(i,end="")
        else:
            print(0,end="")
    print()


