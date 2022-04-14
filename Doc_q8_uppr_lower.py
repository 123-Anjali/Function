def upp(a):
    i=0
    coun=0
    coun1=0
    while i<len(a):
        if a[i]>="A"and a[i]<="Z":
            coun=coun+1
        elif a[i]>="a"  and a[i]<="z":
            coun1=coun1+1
        i=i+1
    print("upper case",coun)
    print("lower case",coun1)
upp("The quick Brow Fox")






