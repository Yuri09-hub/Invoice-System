from models import User,Invoice

def menu():
    print("====================================")
    print("1- Create User                      ")
    print("2- Create Invoice                   ")
    print("3- list invoice                     ")
    print("4- View invoice                     ")
    print("5- Exit                             ")
    print("====================================")


status = True
while status:
    menu()
    choice = int(input("/>"))
    if choice == 1:
        ...
    elif choice == 2:
        ...
    elif choice == 3:
        ...
    elif choice == 4:
        ...
    else:
        status = False