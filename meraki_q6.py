


def cal():
    a=int(input("enter the number"))
    b=int(input("enter the number"))
    operator=(input("enter the operator"))
    if operator=="+":
        print(a+b)
    if operator=="-":
        print(a-b)
    if operator=="*":
        print(a*b)
    if operator=="/":
        print(a//b)
    else:
        print("error")
cal()


# def cal():
#     operator=["1. addittion","2. subtraction","3.multiplication","4. divide"]
#     num=int(input("choose your operator(1/2/3/4"))
#     if num>=1 and num<=4:
#         a=int(input("enter the number"))
#         b=int(input("ente the number"))
#         if num==1:
#             print(a+b)
#         elif num==2:
#             print(a-b)
#         elif num==3:
#             print(a*b)
#         elif num==4:
#             print(a/b)
#         else:
#             print("error")
#     else:
#         print("choose correct answer")
# cal()


# def multiple(a,b):
#     i=0
#     multiply=0
#     x=[]
#     while i<len(a):
#         multiply=a[i]*b[i]
#         x.append(multiply)
#         i=i+1
#     print(x)
# multiple([5,10,50,20],[2,20,3,5])

        
        


def f1():
    s="I love Navgurukul"
    def f2():
        print(s)
    f2()

f1()