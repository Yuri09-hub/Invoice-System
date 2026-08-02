from function import *

from models import session


def menu():
    print("====================================")
    print("1- Create User                      ")
    print("2- Create Invoice                   ")
    print("3- list invoice                     ")
    print("4- View invoice                     ")
    print("5- View users                       ")
    print("6- Exit                             ")
    print("====================================")


status = True
while status:
    menu()
    choice = int(input("/>"))
    if choice == 1:
        name = input("name: ")
        email = input("email: ")
        user = create_user(name,email,session)
        print(user)
    elif choice == 2:
        id = int(input("user id: "))
        price = float(input("price: "))
        invoice = creat_invoice(id,price,session)
        print(invoice)
    elif choice == 3:
        list_invoice(session)
    elif choice == 4:
        id = int(input("invoice id: "))
        result =view_invoice(id,session)
        print(result)

    elif choice == 5:
        view_user(session)
    else:
        status = False