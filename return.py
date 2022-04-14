def menu(day):
    if day=="monday":
        return"Butter chicken"
    elif day=="tuesday":
        return "mutton chaap"
    else:
        return "chole bhature"
    print("will i be able to print ?:-(")
mon_menu=menu("monday")
print(mon_menu)
tues_menu=menu("tuesday")
print(tues_menu)
fri_menu=menu("friday")
print(fri_menu)



def menu(day):
    if day=="monday":
        food="butter chicken"
    elif day=="tuesday":
        food="mutton chaap"
    else:
        food="chole bhature"
    print("will i be able to print?:-(")
    return food
    print("but I m not sure will print?:-(")
print(menu("monday"))