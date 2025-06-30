students = {'Naveen':99,'Dileep':99}
student_name = input("Enter the student's name: ")
if(student_name in students):
    print(f"{student_name}'s marks: {students[student_name]}")
else:
    print('Student not found.')