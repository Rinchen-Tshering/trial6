# Initialize empty lists, sets, and dictionary
student_list = []
student_dict = {}

#prompt the user to input their name, age, grade
name = input("Enter student's name: ")
age = input("Enter student's age: ")
grade = input("Enter student's grade: ")

student_list.append(name)
student_dict[name] = {age , grade}
print("info added succesfully")

#searching the student info
search_name = input("Enter the name of the student you are looking for: ")
if search_name in student_list:
    print(f"the student is {age} of age and is in grade {grade}")
else:
    print("student not found")

#Display all books
print("List of of students enrolled: ")
for students in student_list:
    print(students)

    #remove a book
remove_student = input("Enter the name of the student to remove or else enter to skip: ")
if remove_student in student_list:
    remove_student = student_dict[remove_student]
    student_list.remove(remove_student)
    student_dict.remove(remove_student)
    del student_dict[remove_student]
    print("Student removed successfully")
    print("Student available: ", student_list)

else:
    print("Student not found")