def view_books(books):
    print("----------------------------- Book List -----------------------------")
    print("")
    print("ID       Available          Title                                Author")
    print("---------------------------------------------------------------------------------")
    for id, book in books.items():
        
        row = "{:10} {:10} {:40} {:18}".format(id,
            book["available"],
            book["title"],
            book["author"])
        print(row) 
    print("_________________________________________________________________________________")
        

def add_book(library, books):
    print("---------------------------- Add New Book ----------------------------")
    print("")
    id_list = []
    for id, book in books.items():
        id_list.append(id)

    last_id = id_list[-1]
    increased_id = int(last_id[2:5]) + 1

    b_id = "BK" + "{:03}".format(increased_id)
    print("Book ID:", b_id)
    b_title = input("Title: ").title()
    b_author = input("Author: ").title()
    b_available = "Yes"

    books[b_id] = dict({"title": b_title, "author": b_author, "available": b_available})
    library["book"] = books
    print("")
    print("You have successfully added " + b_id + " - " + b_title + " by " + b_author + " to the library." )

    print("_____________________________________________________________________")

def delete_book(books):
    print("----------------------------- Delete Book -----------------------------")
    print("")
    id = input("Book ID: ").upper()
    print("")
    if id in books and books[id]["available"] == "Yes":
        print("Are you sure you would like to delete " + id + " - " + books[id]["title"] + " by " + books[id]["author"] + "?")
        choice = input("Y / N: ").upper()
        cont_loop = True
        while cont_loop:
            if choice == "Y":
                del books[id] 
                print("")
                print("Book successfully deleted.")
                print("______________________________________________________________________")
                cont_loop = False
            elif choice == "N":
                print("")
                print("Book has not been deleted.")
                print("______________________________________________________________________")
                cont_loop = False
            else:
                print("")
                choice = input("Invalid input. Enter Y or N: ").upper()
                print("")
    elif id in books and books[id]["available"] == "No":
        print("Unsuccessful. Book currently borrowed by a student.")
        print("______________________________________________________________________")
    else:
        print("Book ID doesn't exist.")
        print("______________________________________________________________________")