def populate_library():
    library = {
    "librarian": {},
    "student": {},
    "book": {}
    }
    librarian_details = {}
    student_details = {} 
    book_details = {}

    print("---------------------- Add New Librarian ----------------------")
    print("")

    l_id = 2001
    print("Librarian ID:", l_id)
    l_name = input("Name: ")
    l_age = input("Age: ")
    l_password = input("Password: ")
    l_gender = input("Gender: ")

    librarian_details[l_id] = dict({"name": l_name, "age": l_age, "password": l_password, "gender" : l_gender })
    library["librarian"] = librarian_details

    print("_______________________________________________________________")
    print("")
    print("---------------------- Add New Students ----------------------")
    print("")

    student_no = int(input("How many students would you like to input? "))
    student_id = 1001
    while student_no != 0:
        s_id = student_id
        print("Student ID:", s_id)
        s_name = input("Name: ")
        s_age = input("Age: ")
        s_password = input("Password: ")
        s_gender = input("Gender: ")
        s_course = input("Course: ")
        s_borrowed = ""
        s_history = []

        student_details[s_id] = dict({"name": s_name, "age": s_age, "password": s_password, "gender" : s_gender, "course": s_course, "book_borrowed": s_borrowed,  "book_history": s_history})
        library["student"] = student_details
        student_no -= 1
        student_id += 1
        print("")
    print("_______________________________________________________________")
    print("")
    print("------------------------ Add New Books ------------------------")
    print("")

    book_no = int(input("How many books would you like to input? "))
    book_id = 1
    while book_no != 0:
        b_id = "BK" + "{:03}".format(book_id)
        print("Book ID:", b_id)
        b_title = input("Title: ")
        b_author = input("Author: ")
        b_available = "Yes"

        book_details[b_id] = dict({"title": b_title, "author": b_author, "available": b_available})
        library["book"] = book_details
        book_no -= 1
        book_id += 1
        print("")
    print("_______________________________________________________________")
    print("")

    return library