# i=1
# while i<=10:
#     i=i+1
#     print(i)

# i=1
# while i<=10:
#     print(i)
#     i=i+1



# i=int(input("enter the number"))
# org=i
# sum=0
# l=len (str(i))
# while i>0:
#     sum+=(i%10)**len
#     i=i//10
# if org==sum:
#     print("armstrong number")
# else:
#     print("not armstrong number")



def add(a=int(input("enter the number"))):
    l=[1,2,3,4,5,6,7,8]
    i=0
    sum=0
    while i<len(l):
        if l[i]>a:
            sum+=l[i]
        i=i+1
    print(sum)
add()


# def name(a=input("enter the name")):
#     n=int(input("enter the number"))
#     i=0
#     while i<len(a):
#         i=i+1
#     print(n*a)       
# name()