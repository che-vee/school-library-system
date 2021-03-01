def view_books_available(books):
    print("--------------------- Available Books ---------------------")
    print("")
    print("ID         Title                                    Author")
    print("-------------------------------------------------------------------")
    for id, book in books.items():
        if book["available"] == "Yes":
            row = "{:10} {:40} {:18}".format(id,
                book["title"],
                book["author"])
            print(row) 
    print("__________________________________________________________________")  
            
def borrow_book(student, book_details):
    print("--------------------- Borrow a Book ---------------------")
    print("")
    if len(student["book_borrowed"]) == 0:            
        book_id = str(input("Enter Book ID: ")).upper()
        if book_id in book_details and book_details[book_id]["available"] == "Yes":
            book_details[book_id]["available"] = "No"
            student["book_borrowed"] = book_id
            student["book_history"].append(book_id)
            print("")
            print("You have successfully borrowed " + book_details[book_id]["title"] + " by " + book_details[book_id]["author"] + ".")
            print("_________________________________________________________")
        elif book_id not in book_details:
            print("")
            print("Invalid Book ID.")
            print("___________________________________________________________")
            print("")
            view_books_available(book_details)
            print("")
            borrow_book(student, book_details)           
        elif book_details[book_id]["available"] == "No":
            print("")
            print("This book has already been borrowed.")
            print("_________________________________________________________")
            print("")
            borrow_book(student, book_details)
    else:
        print("You only can only borrow one book at a time.")
        print("_________________________________________________________")
        
def return_book(student, book_details):
    print("--------------------- Return a Book ---------------------")
    print("")
    if len(student["book_borrowed"]) != 0:
        print("Would you like to return " + book_details[student["book_borrowed"]]["title"] + " - " + student["book_borrowed"] + "?")                    
        choice = input("Y / N: ").upper()
        cont_loop = True
        while  cont_loop:
            if choice == "Y":
                book_id = str(student["book_borrowed"])
                if book_id in book_details and book_details[book_id]["available"] == "No":
                    book_details[book_id]["available"] = "Yes"
                    student["book_borrowed"] = ""
                    print("")
                    print("You have returned " + book_details[book_id]["title"] + " successsfully!")
                    print("_________________________________________________________")
                    cont_loop = False
            elif choice == "N":
                cont_loop = False
            else:
                print("")
                choice = input("Invalid input. Enter Y or N: ").upper()
                print("")                     
    else:
        print("You have not borrowed any books.")
        print("_________________________________________________________")

