from main import cw1

class c:
    while (True):
        try:
            #main menu for the users to choose
            print(" welcome to my library management system ")
            print("-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-")
            print("enter 1 to display list of available books")
            print("enter 2 to request a book")
            print("enter 3 to return the requested book")
            print("enter 4 to exit the program")
            a = int(input("enter your choice from 1-4: "))
            print("---------------------------------------")
            if (a == 1):
                with open("stock.txt", "r") as file:
                    print(file.read())
            elif (a == 2):
                cw1.borrowcode()

            elif (a == 3):
                cw1.returning()

            elif (a == 4):
                print("thank you for using my library management system")
                exit()
                break
            else:
                print("choose a number between 1 and 4")
        except:
            print("please input a number")





