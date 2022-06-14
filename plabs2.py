#taask1
# def sumSquarecube(n):
    sumSquarecubeN=n*n+n*n*n
    print(sumSquarecubeN)

sumSquarecube(2)
sumSquarecube(9)
sumSquarecube(11)

task2
def power4(n):
    power4=n*n*n*n
    return power4
def power5(n):
    power5=n*n*n*n*n
    return power5
list=[3,5,8]
length=len(list)
for i in range(0,length):
    ch=list[i]
    z=power4(ch)
    d=power5(ch)

    print("4thpower-",ch,"=",z)
    print("5thpower-",ch,"=",d)

