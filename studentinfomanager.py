# Initialize empty lists, sets, and dictionary
student_list = []
student_dict = {}

#prompt the user to input their name, age, grade
name = input("Enter student's name: ")
age = input("Enter student's age: ")
grade = input("Enter student's grade: ")

student_list.append(name)
student_dict[name] = {'age' : age , 'grade' : grade}
print("info added succesfully")

#searching the student info
search_name = input("Enter the name of the student you are looking for: ")
if search_name in student_list:
    print(f"the student is {age} of age and is in grade {grade}")
else:
    print("student not found")

#Display all student info
print("List of of students enrolled: ")
for students in student_list:
    print(students)

#remove a student  info
remove_student = input("Do you want to remove a student info? if yes enter students name: ")
if remove_student in student_list:
    student_list.remove(remove_student)
    del student_dict[remove_student]
    print("Student removed successfully")
    print("Student available: ", student_list)

elif remove_student == "no":
    print("Thank you for your time")

else:
    print("Student not found")