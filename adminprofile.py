def view_admin_profile(current_user_id, current_user_details):
    print("-------------------- Admin Profile --------------------")
    print("")
    print("Admin ID:", current_user_id)
    print("Name:", current_user_details[0]["name"])
    print("Age:", current_user_details[0]["age"])
    print("Password:", current_user_details[0]["password"])
    print("Gender:", current_user_details[0]["gender"])
    print("_________________________________________________________")

def change_admin_name(librarian):
    print("---------------------- Change Name ----------------------")
    print("")
    print("Would you like to change your name -", librarian["name"])
    choice = input("Y/N : ").upper()
    cont_loop = True
    while cont_loop:
        if choice == "Y":
            new_name = input("Please Enter your new name: ")
            librarian["name"] = new_name.title()
            print("You have successfully changed your name to", librarian["name"])
            print("_________________________________________________________")
            cont_loop = False
        elif choice  == "N":
            cont_loop = False
        else:
            print("")
            choice = input("Invalid input. Enter Y or N: ").upper()
            print("")


def change_admin_password(librarian):
    print("-------------------- Change Password --------------------")
    print("")
    print("Would you like to change your password -", librarian["password"])
    choice = input("Y/N: ").upper()
    cont_loop = True
    while cont_loop:
        if choice == "Y":
            new_password = input("Please enter your new password: ")
            librarian["password"] = new_password
            print("You have successfully changed your password.")
            print("This is your new password -", librarian["password"])
            print("_________________________________________________________")
            cont_loop = False
        elif choice == "N":
            cont_loop = False
        else:
            print("")
            choice = input("Invalid input. Enter Y or N: ").upper()
            print("")
