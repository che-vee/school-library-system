def student_profile(current_user_id, current_user_details):
    print("-------------------- Student Profile --------------------")
    print("")
    print("Student ID:", current_user_id)
    print("Name:", current_user_details[0]["name"])
    print("Age:", current_user_details[0]["age"])
    print("Password: ", current_user_details[0]["password"])
    print("Gender:", current_user_details[0]["gender"])
    print("Course:", current_user_details[0]["course"])
    if current_user_details[0]["book_borrowed"] == "":
        print("Current Book: None")
    else:
        print("Current Book: " + current_user_details[0]["book_borrowed"])
    print("_________________________________________________________")
    
def change_student_name(student):
    print("---------------------- Change Name ----------------------")
    print("")
    print("Would you like to change your name -", student["name"])
    choice = input("Y/N : ").upper()
    cont_loop = True
    while cont_loop:
        if choice == "Y":
            new_name = input("Please enter your new name: ")
            student["name"] = new_name.title()
            print("You have successfully changed your name to", student["name"])
            print("_________________________________________________________")
            cont_loop = False
        elif choice  == "N":
            cont_loop = False
        else:
            print("")
            choice = input("Invalid input. Enter Y or N: ").upper()
            print("")
        
    
def change_student_password(student):
    print("-------------------- Change Password --------------------")
    print("")
    print("Would you like to change your password -", student["password"])
    choice = input("Y/N: ").upper()
    cont_loop = True
    while cont_loop:
        if choice == "Y":
            new_password = input("Please enter your new password: ")
            student["password"] = new_password
            print("You have successfully changed your password.")
            print("Your new password is:", student["password"])
            print("_________________________________________________________")
            cont_loop = False
        elif choice  == "N":
            cont_loop = False
        else:
            print("")
            choice = input("Invalid input. Enter Y or N: ").upper()
            print("")

def book_history(student, books):
    print("--------------------- Book History ----------------------")
    print("")
    
    for id in student["book_history"]:
        try:
            print(id,"-", books[id]["title"], "by", books[id]["author"])
        except KeyError:
            print("Book record no longer available.")
    print("_________________________________________________________")