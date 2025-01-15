# Class definition for the School Management System
class SchoolManagementSystem:
    def __init__(self):
        # Constructor to initialize the system
        # Initializes two lists: one for storing student details and another for teacher details
        self.students = []  # List to store student details
        self.teachers = []  # List to store teacher details

    # Method to add a new student
    def add_student(self):
        # Prompt user for student details and store them in a dictionary
        student = {
            "ID": input("Enter Student ID: "),  # Get student ID
            "Name": input("Enter Student Name: "),  # Get student name
            "Class": input("Enter Class: "),  # Get the class of the student
            "Age": input("Enter Age: ")  # Get the age of the student
        }
        # Add the student dictionary to the students list
        self.students.append(student)
        print("Student added successfully!\n")  # Confirm successful addition

    # Method to add a new teacher
    def add_teacher(self):
        # Prompt user for teacher details and store them in a dictionary
        teacher = {
            "ID": input("Enter Teacher ID: "),  # Get teacher ID
            "Name": input("Enter Teacher Name: "),  # Get teacher name
            "Subject": input("Enter Subject: "),  # Get the subject taught by the teacher
            "Experience": input("Enter Years of Experience: ")  # Get years of experience
        }
        # Add the teacher dictionary to the teachers list
        self.teachers.append(teacher)
        print("Teacher added successfully!\n")  # Confirm successful addition

    # Method to view all students
    def view_students(self):
        # Check if there are no students in the system
        if not self.students:
            print("No students found.\n")  # Inform the user if no students exist
        else:
            print("Student List:")  # Display header
            # Loop through each student in the students list and print their details
            for student in self.students:
                print(f"ID: {student['ID']}, Name: {student['Name']}, "
                      f"Class: {student['Class']}, Age: {student['Age']}")
            print()  # Add a newline for formatting

    # Method to view all teachers
    def view_teachers(self):
        # Check if there are no teachers in the system
        if not self.teachers:
            print("No teachers found.\n")  # Inform the user if no teachers exist
        else:
            print("Teacher List:")  # Display header
            # Loop through each teacher in the teachers list and print their details
            for teacher in self.teachers:
                print(f"ID: {teacher['ID']}, Name: {teacher['Name']}, "
                      f"Subject: {teacher['Subject']}, Experience: {teacher['Experience']} years")
            print()  # Add a newline for formatting

    # Method to delete a student by ID
    def delete_student(self):
        # Prompt the user for the ID of the student to delete
        student_id = input("Enter the Student ID to delete: ")
        for student in self.students:
            if student["ID"] == student_id:
                self.students.remove(student)
                print("Student deleted successfully!\n")
                return
        print("Student ID not found.\n")  # Inform the user if the student is not found

    # Method to delete a teacher by ID
    def delete_teacher(self):
        # Prompt the user for the ID of the teacher to delete
        teacher_id = input("Enter the Teacher ID to delete: ")
        for teacher in self.teachers:
            if teacher["ID"] == teacher_id:
                self.teachers.remove(teacher)
                print("Teacher deleted successfully!\n")
                return
        print("Teacher ID not found.\n")  # Inform the user if the teacher is not found

    # Main method to run the system
    def run(self):
        # Loop continuously until the user decides to exit
        while True:
            # Display the menu options
            print("1. Add Student")
            print("2. Add Teacher")
            print("3. View Students")
            print("4. View Teachers")
            print("5. Delete Student")
            print("6. Delete Teacher")
            print("7. Exit")
            
            # Prompt the user to enter their choice
            choice = input("Enter your choice: ")
            
            # Perform actions based on the user's choice
            if choice == "1":  # Add a student
                self.add_student()
            elif choice == "2":  # Add a teacher
                self.add_teacher()
            elif choice == "3":  # View all students
                self.view_students()
            elif choice == "4":  # View all teachers
                self.view_teachers()
            elif choice == "5":  # Delete a student
                self.delete_student()
            elif choice == "6":  # Delete a teacher
                self.delete_teacher()
            elif choice == "7":  # Exit the system
                print("Exiting the system. Goodbye!")
                break  # Exit the loop
            else:  # Handle invalid choices
                print("Invalid choice. Please try again.\n")

# Run the School Management System if the script is executed directly
if __name__ == "__main__":
    # Create an instance of the SchoolManagementSystem class
    sms = SchoolManagementSystem()
    # Call the run method to start the program
    sms.run()
