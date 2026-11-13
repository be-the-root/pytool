import random
import string
import time

def gen_basic(length):
    lower = string.ascii_lowercase
    upper = string.ascii_uppercase
    pool = lower + upper

    time.sleep(2)

    pw = ""
    for i in range(length):
        pw = pw + random.choice(pool)


    return pw

def menu():
    while True:
    
        print()
        print()
        print("========== P Y  T O O L ==========")
        print()
        print("chose your desired option")
        print()
        print("|| 1. enter my name")
        print()
        print("|| 2. generate password")
        print()
        print("|| 3. exit")

        cmd = input(">>> ")
        if cmd == "1":
            name = input("enter your name: ")
            print("hello " + name)
            continue

    
        elif cmd == "2":
            len_txt = input("lenth (8 - 64): ").strip()

            if not len_txt.isdigit():
                print("submit a valid digit between 8 and 64")
                continue

            length = int(len_txt)


            if length < 8 or length > 64:
                print("submit a valid digit between 8 and 64")
                continue
            pw = gen_basic(length)

            print()
            print("your password:  " + pw)



        elif cmd == "3":
            print("byeeeee")
            break



menu()