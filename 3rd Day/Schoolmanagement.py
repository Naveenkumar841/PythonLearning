
class SchoolManagementSystem:
    def __init__(self):
        self.students = []  
        self.teachers = []  


    def add_student(self):

        student = {
            "ID": input("Enter Student ID: "),  
            "Name": input("Enter Student Name: "), 
            "Father's Name": input("Enter Father's Name: "),  
            "Class": input("Enter Class: "),
            "Address": input("Enter Address: "),  
            "Age": input("Enter Age: ") , 
            "Fee": input("Enter Fee: ")  
        }

        self.students.append(student)
        print("Student added successfully!\n")  


    def add_teacher(self):

        teacher = {
            "ID": input("Enter Teacher ID: "),  
            "Name": input("Enter Teacher Name: "), 
            "Teacher Age": input("Enter Your Age: ") ,
            "Subject": input("Enter Subject: "),  
            "Experience": input("Enter Years of Experience: ")  
        }

        self.teachers.append(teacher)
        print("Teacher added successfully!\n")  

 
    def view_students(self):

        if not self.students:
            print("No students found.\n")  
        else:
            print("Student List:")  
            
            for student in self.students:
                print(f"ID: {student['ID']}, Name: {student['Name']}, "
                      f"Class: {student['Class']}, Age: {student['Age']}, Fee: {student['Fee']}" )
            print()  


    def view_teachers(self):

        if not self.teachers:
            print("No teachers found.\n")  
        else:
            print("Teacher List:")  
            
            for teacher in self.teachers:
                print(f"ID: {teacher['ID']}, Name: {teacher['Name']}, "
                      f"Subject: {teacher['Subject']}, Experience: {teacher['Experience']} years")
            print()  


    def delete_student(self):

        student_id = input("Enter the Student ID to delete: ")
        for student in self.students:
            if student["ID"] == student_id:
                self.students.remove(student)
                print("Student deleted successfully!\n")
                return
        print("Student ID not found.\n")  


    def delete_teacher(self):

        teacher_id = input("Enter the Teacher ID to delete: ")
        for teacher in self.teachers:
            if teacher["ID"] == teacher_id:
                self.teachers.remove(teacher)
                print("Teacher deleted successfully!\n")
                return
        print("Teacher ID not found.\n")  
        
    def run(self):
        
        while True:
        
            print("1. Add Student")
            print("2. Add Teacher")
            print("3. View Students")
            print("4. View Teachers")
            print("5. Delete Student")
            print("6. Delete Teacher")
            print("7. Exit")
            
        
            choice = input("Enter your choice: ")
            
        
            if choice == "1":  
                self.add_student()
            elif choice == "2":  
                self.add_teacher()
            elif choice == "3":  
                self.view_students()
            elif choice == "4":  
                self.view_teachers()
            elif choice == "5":  
                self.delete_student()
            elif choice == "6":  
                self.delete_teacher()
            elif choice == "7":  
                print("Exiting the system. Goodbye!")
                break  
            else:  
                print("Invalid choice. Please try again.\n")

if __name__ == "__main__":

    sms = SchoolManagementSystem()

    sms.run()
