# def number():
#     l=[2,4]
#     i=0
#     while i<len(l):
#         if l[i]%2==0:
#             print(" both are even",l)
#         else:
#             print(" both are not even",l)
#         i=i+1
#         break
# number()

def number():
    l=[2,6,18,10,3,75]
    a=[6,19,24,12,3,87]
    i=0
    while i<len(l):
        if (l[i])%2==0 and (a[i])%2==0:
            print("both are even",l[i],a[i])
        else:
            print("both are not even",l[i],a[i]) 
        i=i+1
number()  