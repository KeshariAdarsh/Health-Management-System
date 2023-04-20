import datetime

def gettime():
    return datetime.datetime.now()

def take(k):
    if k==1:
        c=int(input("\nEnter 1 for exercise and 2 for food"))
        if c==1:
            value=input("Type Here\n")
            with open ("Hari-ex.txt","a") as f:
                f.write(str(gettime())+":"+value+"\n")
            print("Successfully written")
        elif c==2:
            value=input("Type Here\n")
            with open("Hari-fd.txt","a") as f:
                f.write(str(gettime())+":"+value+"\n")
            print("Successfully written")
        else:
            print("Please enter valid input")

    elif k==2:
        c=int(input("\nEnter 1 for exercise and 2 for food"))
        if c==1:
            value=input("Type here\n")
            with open("Rama-ex.txt","a") as f:
                f.write(str(gettime())+":"+value+"\n")
            print("Successfully written")
        elif c==2:
            value=input("Type here\n")
            with open("Rama-fd.txt","a") as f:
                f.write(str(gettime())+":"+value+"\n")
            print("Successfully written")

        else:
            print('Please enter valid input')

    elif k==3:
        c = int(input("\nEnter 1 for exercise and 2 for food"))
        if c == 1:
            value = input("Type here\n")
            with open("Krishna-ex.txt", "a") as f:
                f.write(str(gettime())+":"+value+"\n")
            print("Successfully written")
        elif c == 2:
            value = input("Type here\n")
            with open("Krishna-fd.txt", "a") as f:
                f.write(str(gettime())+":"+value+"\n")
            print("Successfully written")
        else:
            print("Please enter valid input")

    else:
        print("\nPlease enter valid input(1-Hari,2-Rama,3-Krishna)")


def retrieve(k):
    if k==1:
        c=int(input("\nEnter 1 for exercises and 2 for food"))
        if (c==1):
            with open("Hari-ex.txt") as f:
                print(f.read())
        elif(c==2):
            with open("Hari-fd.txt") as f:
                print(f.read())

        else:
            print("Please enter valid input")

    elif k==2:
        c=int(input("\nEnter 1 for exercises and 2 for food"))
        if (c==1):
            with open("Rama-ex.txt") as f:
                print(f.read())
        elif(c==2):
            with open("Hari-fd.txt") as f:
                print(f.read())
        else:
            print("Please enter valid input")

    elif k==3:
        c=int(input("\nEnter 1 for exercises and 2 for food"))
        if (c==1):
            with open("Krishna-ex.txt") as f:
                print(f.read())
        elif(c==2):
            with open("Krishna-fd.txt") as f:
                print(f.read())
        else:
            print("Please enter valid input")

    else:
        print("\nPlease enter valid input(1-Hari,2-Rama,3-Krishna)")

if __name__ == '__main__':
    print("HEALTH MANAGEMENT SYSTEM")
    while True:
        a=int(input("\nPress 1 for log the value and 2 for retrieve and 3 for quit"))
        if a==1:
            b=int(input("\nPress"+"\n"+"1 for Hari"+"\n"+"2 for Rama"+"\n"+"3 for Krishna"))
            take(b)
        elif a==2:
            b=int(input("\nPress"+"\n"+"1 for Hari"+"\n"+"2 for Rama"+"\n"+"3 for Krishna"))
            retrieve(b)
        elif a==3:
            print("\nCLosed Management System")
            break
        else:
            print("PLease enter valid input")



