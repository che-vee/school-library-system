import json
from inputdata import populate_library
from bookrecords import view_books, add_book, delete_book
from studentrecords import view_student_details, add_new_student, remove_student
from adminprofile import view_admin_profile, change_admin_name, change_admin_password
from studentlibrary import view_books_available, borrow_book, return_book
from studentaccount import  student_profile, change_student_name, change_student_password, book_history

try:
    with open('library.json', 'r') as json_file:
        library = json.load(json_file)
        librarian_details = library["librarian"]
        student_details = library["student"]
        book_details = library["book"]
except:
    library = populate_library()
    librarian_details = library["librarian"]
    student_details = library["student"]
    book_details = library["book"]

print("-------------------------------")
print("  Welcome to Taylor's Library  ")  
print("-------------------------------")
print("")

user_id = input("ID: ")
password = input("Password: ")
num_of_tries = 3

found_user = False
current_user_id = ""
current_user_details = []

if user_id.startswith("2") and user_id in librarian_details:
    for id, librarian in librarian_details.items():
        while user_id == id and not password == librarian["password"] and num_of_tries > 1:
            print("")
            num_of_tries -= 1
            print("Incorrect password. Input password again. You have", num_of_tries, "tries left.")
            password = input("Password: ")


        if user_id == id and password == librarian["password"]:
            found_user = True
            current_user_id = user_id
            current_user_details.append(librarian)
            print("_______________________________")
            print("")
            print("Welcome " + current_user_details[0]["name"] + "!")
            print("Your access level is Librarian.")

            while found_user:
                print("""
-------------------------------
           Main Menu
-------------------------------
1. Book Records
2. Student Records
3. Admin Account
0. Save and Exit
"""
                        )   
                try:
                    action = int(input("Select an option: "))
                    if action == 1:
                        print("""
-------------------------------
        Book Records
-------------------------------
1. View Book List
2. Add New Book
3. Delete Book
0. Back to Main Menu
                        """)
                    
                        action = input("Select an option: ")
                        while action != "0":
                            try:
                                action = int(action)
                                print("")
                                if action == 1:
                                    view_books(book_details)
                                elif action == 2:
                                    add_book(library, book_details)
                                elif action == 3:
                                    delete_book(book_details)
                                else:
                                    print("Invalid option, enter a number between 0 - 3.")
                            except ValueError:
                                print("Invalid input, enter a number between 0 - 3.")
                            print("""
-------------------------------
        Book Records
-------------------------------
1. View Book List
2. Add New Book
3. Delete Book
0. Back to Main Menu
                        """)
                            action = input("Select an option: ")

                    elif action == 2:
                        print("""
-------------------------------
        Student Records
-------------------------------
1. View Student Details
2. Add New Student
3. Remove Student
0. Back to Main Menu
                        """)
                    
                        action = input("Select an option: ")
                        while action != "0":
                            try:
                                action = int(action)
                                print("")
                                if action == 1:
                                    view_student_details(student_details)
                                elif action == 2:
                                    add_new_student(library, student_details)
                                elif action == 3:
                                    remove_student(library, student_details)
                                else:
                                    print("Invalid option, enter a number between 0 - 3.")
                            except ValueError:
                                print("Invalid input, enter a number between 0 - 3.")
                            print("""
-------------------------------
        Student Records
-------------------------------
1. View Student Details
2. Add New Student
3. Remove Student
0. Back to Main Menu
                        """)
                            action = input("Select an option: ")

                    elif action == 3:
                        print("""
-------------------------------
        Admin Page
-------------------------------
1. View Admin Profile
2. Change Name
3. Change Password
0. Back to Main Menu
                        """)
                        action = input("Select an option: ")
                        while action != "0":
                            try:
                                action = int(action)
                                print("")
                                if action == 1:
                                    view_admin_profile(current_user_id, current_user_details)
                                elif action == 2:
                                    change_admin_name(librarian)
                                elif action == 3:
                                    change_admin_password(librarian)
                                else: 
                                    print("Invalid option, enter a number between 0 - 4.")
                            except ValueError:
                                print("Invalid input, enter a number between 0 - 4.")
                            print("""
-------------------------------
        Admin Page
-------------------------------
1. View Admin Profile
2. Change Name
3. Change Password
0. Back to Main Menu
                        """)
                            action = input("Select an option: ")

                    elif action == 0:
                        found_user = False
                        print("_______________________________")
                        print("")
                        print("Exiting program...")
                        print("Goodbye.")
                        print("")
                except ValueError:
                    print("")
                    print("Invalid input, enter a number between 0 - 3.")
                    print("_______________________________")


elif user_id.startswith("1") and user_id in student_details:
    for id, student in student_details.items():
        while user_id == id and not password == student["password"] and num_of_tries > 1:
            print("")
            num_of_tries -= 1
            print("Incorrect password. Input password again. You have", num_of_tries, "tries left.")
            password = input("Password: ")

        if user_id == id and password == student["password"]:
            found_user = True
            current_user_id = user_id
            current_user_details.append(student)
            print("_______________________________")
            print("")
            print("Welcome " + current_user_details[0]["name"] + "!")
            print("Your access level is Student.")

            while found_user:
                print("""
-------------------------------
           Main Menu
-------------------------------
1. Library 
2. Student Account
0. Save and Exit
"""
                            ) 
                try:
                    action = int(input("Select an option: "))
                    if action == 1:
                        print("""
-------------------------------
           Library
-------------------------------
1. View Available Books
2. Borrow a Book
3. Return a Book
0. Return to Main Menu
"""                             
                                    ) 
                        action = input("Select an option: ")
                        while action != "0":      
                            try:
                                action = int(action)
                                print("")
                                if action == 1:
                                    view_books_available(book_details)
                                elif action == 2:
                                    borrow_book(student, book_details)
                                elif action == 3:
                                    return_book(student, book_details)
                                else:
                                    print("Invalid option, enter a number between 0 - 3.")
            
                            except ValueError :
                                print("Invalid input, enter a number between 0 - 3.")
                            print("""
-------------------------------
           Library
-------------------------------
1. View Available Books
2. Borrow a Book
3. Return a Book
0. Return to Main Menu
"""                             
                                    ) 
                            action = input("Select an option: ")
                            
                    elif action == 2:
                        print("""
-------------------------------
         Student Account
-------------------------------
1. Book History
2. Student Profile
3. Change Name
4. Change Password
0. Return to Main Menu 
"""
                                )
                        action = input("Select an option: ")
                        while action != "0":
                            try:
                                action = int(action)
                                print("")
                                if action == 1:
                                    book_history(student, book_details)
                                elif action == 2:
                                    student_profile(current_user_id, current_user_details)
                                elif action == 3:
                                    change_student_name(student)
                                elif action == 4:
                                    change_student_password(student)                           
                                else:
                                    print("Invalid option, enter a number between 0 - 4.")
                            except ValueError :
                                print("Invalid input, enter a number between 0 - 4.")
                            print("""
-------------------------------
         Student Account
-------------------------------
1. Book History
2. Student Profile
3. Change Name
4. Change Password
0. Return to Main Menu 
"""
                                )
                            action = input("Select an option: ")
                    elif action == 0:
                        found_user = False
                        print("_______________________________")
                        print("")
                        print("Exiting program...")
                        print("Goodbye.")
                        print("")   
                    else:
                        print("")
                        print("Invalid option, enter a number between 0 - 2.")                    
                except ValueError:
                    print("")
                    print("Invalid input, enter a number between 0 - 2.")      
else:
    print("")
    print("User not found. Access denied!")
    print("")

with open('library.json', 'w') as json_file:
    json.dump(library, json_file)
