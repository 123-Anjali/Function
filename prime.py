def prime():
    a=int(input("enter the number"))
    i=1
    while i<=a:
        c=0
        j=1
        while j<=i:
            if i%j==0:
                c=c+1
            j=j+1
        if c==2:
            print(i)
        i=i+1
prime()

