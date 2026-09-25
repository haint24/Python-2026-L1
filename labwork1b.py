student_list = []
course_list = []

def input_students():
    count = int(input("Enter the number of students: "))
    for i in range(count):
        print(f"\n--- Student #{i + 1} ---")
        student_id = input("Enter id: ")
        name = input("Enter name: ")
        dob = input("Enter date of birth: ")
        student_data = {"id": student_id, "name": name, "dob": dob}
        student_list.append(student_data)
    print("Finished list of students!\n")

def input_courses():
    number_of_courses = int(input("Enter the number of courses: "))
    for i in range(number_of_courses):
        print(f"\n--- Course #{i + 1} ---")
        course_id = input("Enter id of the course: ")
        course_name = input("Enter name of the course: ")
        course_data = {"id": course_id, "name": course_name, "marks": {}}
        course_list.append(course_data)
    print("Finished list of courses!\n")

def list_courses():
    if not course_list:
        print("No courses available.")
        return
    print("\n--- Course List ---")
    for course in course_list:
        print(course["id"], "-", course["name"])

def list_students():
    if not student_list:
        print("No students available.")
        return
    print("\n--- Student List ---")
    for student in student_list:
        print(student["id"], "-", student["name"], "-", student["dob"])

def input_marks():
    list_courses()
    course_id = input("Choose course ID: ")
    found = False
    for course in course_list:
        if course["id"] == course_id:
            found = True
            for student in student_list:
                mark = float(input(f"Mark for {student['name']}: "))
                course["marks"][student["id"]] = mark
            break
    if not found:
        print("Course not found")

def show_marks():
    list_courses()
    course_id = input("Choose course ID: ")
    found = False
    for course in course_list:
        if course["id"] == course_id:
            found = True
            print(f"\n--- Marks for {course['name']} ---")
            for student in student_list:
                if student["id"] in course["marks"]:
                    print(student["name"], ":", course["marks"][student["id"]])
                else:
                    print(student["name"], ": no mark yet")
            break
    if not found:
        print("Course not found")

while True:
    print("\n================== MENU ==================")
    print("1. Input students")
    print("2. Input courses")
    print("3. Input marks")
    print("4. List courses")
    print("5. List students")
    print("6. Show marks")
    print("0. Exit")
    print("==========================================")
 
    choice = input("Choose: ")
 
    if choice == "1":
        input_students()
    elif choice == "2":
        input_courses()
    elif choice == "3":
        input_marks()
    elif choice == "4":
        list_courses()
    elif choice == "5":
        list_students()
    elif choice == "6":
        show_marks()
    elif choice == "0":
        break
    else:
        print("Invalid choice")
 
print("Goodbye!")
