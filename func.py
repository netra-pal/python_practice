# def largestA(st):
#     max = 0
#     string = ''
#     for i in st:
#         if i.count('a')>max:
#             string = i
#     return string
#
#
# def getTotalA(st,prob=1):
#     count =0
#     for i in range(len(st)):
#         if prob == 1:
#             if st[i] == 'a':
#                 count+=1
#         elif prob == 2:
#             for j in range(len(st[i])):
#                 if st[i][j] == 'a':
#                     count +=1
#         elif prob == 3:
#             count = largestA(st)
#     return count
#
# # print(getTotalA('asdf'))
# # print(getTotalA(['a','aesd','dgdhe','aaaaa'],2))
# print(getTotalA(['a','aesd','dgdhe','aaaaa'],3))

def largestA(st):
    max = 0
    string = ''
    for i in st:
        if i.count('b')>max:
            string = i
            return string


def getTotalA(st,prob=1):
    count =0
    for i in range(len(st)):
        if prob == 1:
            if st[i] == 'a':
                count+=1
        elif prob == 2:
            for j in range(len(st[i])):
                if st[i][j] == 'a':
                    count +=1
        elif prob == 3:
            count = largestA(st)
    return count

# print(getTotalA('asdf'))
# print(getTotalA(['a','aesd','dgdhe','aaaaa'],2))
print(getTotalA(['a','awse','abdbf','bbbbb'],3))