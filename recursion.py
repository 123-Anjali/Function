# def sum(number):
#     if number==1:
#         return 1
#     return 2 * sum(number-1)

# index=1
# while(index<10):
#     print(sum(index))
#     index+=1


# def add(number):
#     if number == 1:
#         return 1
#     else:
#         return add(number-1) + 3
# index=1
# while (index<10):
#     print(add(index))
#     index+=1




def sum(number):
    if number == 1:
        return 10
    elif number % 2 == 0:
        return sum(number - 1) + 1
    else:
        return sum(number - 1) * 10
index=1
while(index<10):
    print(sum(index))
    index+=1


# def factorial(number):
#     if number==1:
#         return 1
#     return number * factorial(number - 1)

# print (factorial(5))




# def sum_list(lis):
#     if len(lis)==1:
#         return lis[0]
#     return lis[0] + sum_list(lis[1:])

# print (sum_list([1, 4, 7, 10]))




# def palindrome(string):
#     if string == "":  # BASE CASE CONDITION
#         return True
#     elif len(string) == 1:  # BASE CASE CONDITION
#         return True
#     elif string[0] == string[len(string)-1]:  # RECURSION
#         return palindrome(string[1:][:-1])
#     else:
#         return False
# print(palindrome(input("enter the string")))







# def fib(number):
#     if number == 1:
#         return 0
#     elif number == 2:
#         return 1
#     else:
#         return fib(number-1) + fib(number-2)

# def get(number):
#     fib_list = []
#     key = 1
#     while (key < number + 1):
#         fib_list.append(fib(key))
#         key += 1
#     return fib_list

# print(get(10))





