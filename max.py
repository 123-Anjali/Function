def max():
    a=[1,5,2,8,7,9,2,4]
    i=0
    maxx=0
    while i<len(a):
        if a[i]>maxx:
            maxx=a[i]
        i=i+1
    print(maxx)
max()
