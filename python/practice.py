import random

def odd_or_even(num):
    if num % 2 == 0:
        return "even"
    else:
        return "odd"
    
print(odd_or_even(random.randint(0, 100)))

def count_till_num(num):
    total = 0
    for i in range(1, num + 1):
        total +=i
    return total

print(count_till_num(3))

def login():
    username = input("Enter your username: ")
    password = input("Enter your password: ")

    if username != "admin":
        return "user not found"
    elif username == "admin" and password != "admin":
        return "incorerrect password"
    else: 
        return "successful login"
    
print(login())

