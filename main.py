#importing date and time
from datetime import date, datetime

class cw1():
    global booklist
    booklist = []
    books = open("stock.txt", "r")
    x = books.readlines()
    books.close()

    for i in x:
        bookline = i.replace("\n", "").split(",")
        booklist.append(bookline)

    def bookdisplay():                #displaying the stock file to the user
        disp = open("stock.txt", "r")
        print(disp.read())
        disp.close()

    def borrowcode():           #separating into modules to make the code accessible
        borrow_money = 0
        borrow_note = ""
        borrowed_books = ""
        books_entered = []

        name = str(input("Enter your name:"))

        newlist = "borrow-"+name+".txt"             #creating the borrow note after the user borrows
        with open(newlist,"w+")as f:
            f.write("library management system:\n")
            f.write("borrowed by: " +name+ "\n")
            f.write("date: " + str(date.today()) + ", " "time: " + str(datetime.now())+ "\n")
            f.write("Book name: ")

        borrow_date = date.today()
        borrow_date1 = str(borrow_date.strftime("%d/%m/%Y"))
        borrow_time = datetime.now()
        borrow_time1 = str(borrow_time.strftime("%H:%M"))
        borrowmore = "yes"
        borrow_note = name + "," + borrow_date1 + "," + borrow_time1
        newbook = ""

        while borrowmore.lower() == "yes":      #creating a loop until the user borrows the book
            print("choose the respective number to borrow the book")
            print("1 for Harry potter")
            print("2 for lord of the rings")
            print("3 for Eragon")
            book_no = int(input("Choose the number: "))

            if book_no == 1:
                if len(books_entered) > 1:          #checking if the user has borrowed same book twice
                    for i in range(len(books_entered)):
                        if books_entered[i] == 1:
                            print("The book has already been borrowed")
                            break
                else:
                    if int(booklist[0][2]) > 0:       #checking if the book is in stock
                        booklist[0][2] = str(int(booklist[0][2]) - 1)
                        print(booklist[0][3])
                        books_entered.append(book_no)
                        borrow_money = borrow_money + int(booklist[0][3].replace("Rs",""))
                        borrowed_books = borrowed_books + "harry potter" + ","

                    else:
                        print("The book is not in stock")

            elif book_no == 2:
                if len(books_entered) > 1:
                    for i in range(len(books_entered)):
                        if books_entered[i] == 2:
                            print("The book has already been borrowed")
                            break
                else:
                    if int(booklist[1][2]) > 0:
                        available = 0
                        booklist[1][2] = str(int(booklist[1][2]) - 1)
                        print(booklist[1][3])
                        books_entered.append(book_no)
                        borrow_money = borrow_money + int(booklist[1][3].replace("Rs",""))
                        borrowed_books = borrowed_books + "lord of the rings" + ","

                    else:
                        print("The book is not in stock")

            elif book_no == 3:
                if len(books_entered) > 1:
                    for i in range(len(books_entered)):
                        if books_entered[i] == 3:
                            print("The book has already been borrowed")
                            break
                else:
                    if int(booklist[2][2]) > 0:
                        booklist[2][2] = str(int(booklist[2][2]) - 1)
                        print(booklist[2][3])
                        books_entered.append(book_no)
                        borrow_money = borrow_money + int(booklist[2][3].replace("Rs",""))
                        borrowed_books = borrowed_books + "eragon" + ","

                    else:
                        print("The book is not in stock")
            else:
                print("enter value between 1 and 3")
                break

            borrowmore = str(input("Are more book being borrowed?Input yes or no: ")) #asking the user if they want to borrow multiple books
        if borrowmore.lower() == "no":
            for i in range(len(booklist)):  # to convert the list into string to overwrite in stock.txt
                word = ""
                for j in range(len(booklist[i])):
                    if j == len(booklist[i]) - 1:
                        word = word + booklist[i][j] + "\n"
                    else:
                        word = word + booklist[i][j] + ","
                newbook = newbook + word
            print(newbook)
            borrow_note = borrow_note + "," + "Rs" + str(borrow_money) + "," + borrowed_books + "\n"
            print(borrow_note)
            stockread = open("stock.txt", "w")
            stockread.write(newbook)
            stockread.close()

            with open(newlist,"a") as f:        #writing the details into the note
                f.write(borrowed_books)


    def returning():
        returnmore = "y"
        return_books = []      #creating empty list to check books returned
        returnnote = ""
        returnmoney = 0
        returned_books = ""
        returninfo = ""

        re_date = date.today()
        issue_date2 = str(re_date.strftime("%d/%m/%Y"))
        re_time = datetime.now()
        issue_time2 = str(re_time.strftime("%H:%M"))




        name = str(input("enter the name of the borrower: "))

        newlist2 = "return-"+name+".txt"            #creating return note after returning books
        with open(newlist2,"w+") as f:
            f.write("Library management system" "\n")
            f.write("returners name: "+name+"\n")
            f.write("date: " + str(date.today()) + ", " "time: " + str(datetime.now()) + "\n")
            f.write("books returned: ")


        returnnote = name + "," + issue_date2 + "," + issue_time2
        yes = input("has the borrow date been 10 days: press y for yes and n for no: ")
        days = int(input("by how many days has the date expired: "))
        fine = 2 * days
        print("----------------------------------")

        while returnmore == "y":
            print("which book would you like to return:")
            print("press 1 to return harry potter")
            print("press 2 to return lord of the rings")
            print("press 3 to return eragon")
            inpu = int(input("enter the book number: "))
            if inpu == 1:
                booklist[0][2] = str(int(booklist[0][2])+1)       #adding the stock of the respective book 
                print("harry potter has successfully been returned")
                returnmoney = returnmoney + int(booklist[0][3].replace("Rs",""))
                returned_books = returned_books + "harry potter"+ ","


            elif inpu == 2:
                booklist[1][2] = str(int(booklist[1][2])+1)
                print("the shining has successfully been returned")
                returnmoney = returnmoney + int(booklist[1][3].replace("Rs",""))
                returned_books = returned_books + "lord of the rings" + ","

            elif inpu == 3:
                booklist[2][2] = str(int(booklist[2][2])+1)
                print("the lord of the rings has successfully been returned")
                returnmoney = returnmoney + int(booklist[2][3].replace("Rs",""))
                returned_books = returned_books + "eragon" + ","

            else:
                print("enter number between 1 and 4")
                break

            returnmore = str(input("are more books going to be returned? y for yes and n for no: "))
        if returnmore.lower() == "n":
            for i in range(len(booklist)):
                n = ""
                for j in range(len(booklist[i])):
                    if j == len(booklist[i])+1:
                        n= n + booklist[i][j] +"\n"
                    else:
                        n = n + booklist[i][j] + ","
                returninfo = returninfo + n
            print(returninfo)
            returnnote = returnnote + "," + "Rs" + str(returnmoney)+ f + "," + returned_books + "," "\n"
            print(returnnote)
            returnread1 = open("stock.txt","w")
            returnread1.write(returninfo)
            returnread1.close()

            with open(newlist2,"a") as f:
                f.write(returned_books +"\n")
                f.write(str(returnmoney))

           





