def menu():
    print()
    print()
    print("==========PYTOOL==========")
    print("chose your desired option")
    print()
    print("|| 1. enter my name")
    print()
    print("|| 2. exit")

    cmd = input(">>> ")
    if cmd == "1":
        name = input("enter your name: ")
        print("hello " + name)
        return menu()
    elif cmd == "2":
        print("byeeee")
        exit()