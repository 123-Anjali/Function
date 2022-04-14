def reverse_list():
    l=["Z","A","T","E","L","G","U"]
    i=len(l)-1
    b=[]
    while i>=0:
        b.append(l[i])
        i=i-1
    print(b)
reverse_list()
