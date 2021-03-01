def view_student_details(student):
    print("ID         Name           Age       Password          Gender          Course            Book Borrowed")
    print("------------------------------------------------------------------------------------------------------")
    print("")
    for id, student in student.items():
        row = "{:10} {:15} {:10} {:15} {:15} {:20} {:10}".format(id,
            student["name"],
            student["age"],
            student["password"],
            student["gender"],
            student["course"],
            "None" if student["book_borrowed"] == "" else student["book_borrowed"])
        print(row)
    print("____________________________________________________________________________________________________")

def add_new_student(library,student_details):
    print("-------------------------- Add New Student --------------------------")
    print("")
    id_list = []
    for id, student in student_details.items():
        id_list.append(id)
    
    last_id = id_list[-1]
    s_id = str(int(last_id) + 1)
    print("Student ID:", s_id)
    s_name = input("Name: ").title()
    while True:
        try:
            s_age = int(input("Age: "))
            break
        except ValueError:
            print("Input age in number. e.g 21.") 

    s_password = input("Password: ")
    gender = input("Gender: M or F ? ").upper()
    cont_loop = True
    while cont_loop:
        if gender == "M":
            s_gender = "Male"
            cont_loop = False
        elif gender == "F":
            s_gender = "Female"
            cont_loop = False
        else:
            print("")
            gender = input("Invalid input. Enter M or F: ").upper()
            print("")
    s_course = input("Course: ").title()
    s_borrowed = ""
    s_history = []

    student_details[s_id] = dict({"name": s_name, "age": str(s_age), "password": s_password, "gender" : s_gender, "course": s_course, "book_borrowed": s_borrowed,  "book_history": s_history})
    library["student"] = student_details
    print("")
    print("You have successfully added " + s_id + " - " + s_name + " to the student records.")
    print("_____________________________________________________________________")
    
def remove_student(library, student_details):
    print("----------------------------- Delete Student -----------------------------")
    print("")
    id = input("Student ID: ").upper()
    print("")
    if id in student_details:
        print("Are you sure you would like to delete " + id + " - " + student_details[id]["name"] + "?")
        choice = input("Y / N: ").upper()
        cont_loop = True
        while cont_loop:
            if choice == "Y":
                del student_details[id]
                print("")
                print("Student successfully deleted.")
                print("______________________________________________________________________")
                cont_loop = False
            elif choice == "N":
                print("")
                print("Student has not been deleted.")
                print("______________________________________________________________________")
                cont_loop = False
            else:
                print("")
                choice = input("Invalid input. Enter Y or N: ").upper()
                print("")
    else:
        print("Unsuccessful. Student ID doesn't exist.")
        print("______________________________________________________________________")
    