def min():
    l=[8,9,7,6,5,4,3]
    i=0
    minn=l[0]
    while i<len(l):
        if l[i]<minn:
            minn=l[i]
        i=i+1
    print(minn)
min()
    