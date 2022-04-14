def display():
    if age<=14:
        print("drink toddy")
    if age>14 and age<=18:
        print("drink coke")
    if  age>18 and age<=21:
        print("drink beer")
    if age>21:
        print("drink wishky")
age=int(input("enter the number"))
display()
