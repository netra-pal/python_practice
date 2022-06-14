
def largestA(my_list):
    max=my_list[0]
    length=len(my_list)
    for i in range(0,length):
        element=my_list[i]
        if(max>element):
            max=element
        print(max)

def printTotalA(my_list):
    length =len(my_list)
    count =0
    for i in range(0 ,length) :
        element =my_list[i]
        count +=getTotalA(element)
    print(count)

def getTotalA(st):
    count=0
    length=len(st)
    for i in range(0,length):
        ch=st[i]
        if ch=="a":
            count+=1
    return count


printTotalA(["a","abef","abaca","bcd"])



