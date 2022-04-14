def meal(day,time):
    if day=="sunday":
        if time=="breakfast":
            return "dosa"
        if time=="lunch":
            return "daal rice"
        if time=="dinner":
            return "paneer roti"
        else:
            return "time not found"
    elif day=="monday":
        if time=="breakfast":
            return "poha"
        if time =="lunch":
            return "daal rice roti sbji"
        if time=="dinner":
            return "rajma rice"
        else:
            return "time not found"
    elif day=="other":
        if time=="breakfast":
            return "maggi"
        if time=="lunch":
            return "fried rice"
        if time=="dinner":
            return "nonveg"
        else:
            return "time not found"
print(meal("monday","lunch"))
print(meal("other","dinner"))
