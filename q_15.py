# def employee(name,salary=20000):
#     print(name,"your salary is:-",salary)
# employee("kartik",300000)
# employee("deepak")


def greet(*names):
    for name in names:
        print("hello",name)
greet("sonu","kartik","umesh","devendra")