import os
import json

# File to store student data
FILE_NAME = "students.json"

def load_data():
    """Load student data from the file."""
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, 'r') as file:
            return json.load(file)
    return []

def save_data(students):
    """Save student data to the file."""
    with open(FILE_NAME, 'w') as file:
        json.dump(students, file, indent=4)

def add_student(students):
    """Add a new student record."""
    roll_number = input("Enter Roll Number: ").strip()
    if any(student["roll_number"] == roll_number for student in students):
        print("Student with this roll number already exists!")
        return
    name = input("Enter Name: ").strip()
    age = int(input("Enter Age: ").strip())
    student_class = input("Enter Class: ").strip()
    
    students.append({"roll_number": roll_number, "name": name, "age": age, "class": student_class})
    print("Student added successfully!")

def update_student(students):
    """Update an existing student record."""
    roll_number = input("Enter Roll Number to Update: ").strip()
    for student in students:
        if student["roll_number"] == roll_number:
            print(f"Current Details: {student}")
            student["name"] = input("Enter New Name: ").strip()
            student["age"] = int(input("Enter New Age: ").strip())
            student["class"] = input("Enter New Class: ").strip()
            print("Student record updated successfully!")
            return
    print("Student with this roll number not found.")

def delete_student(students):
    """Delete a student record."""
    roll_number = input("Enter Roll Number to Delete: ").strip()
    for student in students:
        if student["roll_number"] == roll_number:
            students.remove(student)
            print("Student record deleted successfully!")
            return
    print("Student with this roll number not found.")

def view_students(students):
    """View all student records."""
    if not students:
        print("No student records found.")
    else:
        print("\n--- Student Records ---")
        for student in students:
            print(f"Roll Number: {student['roll_number']}, Name: {student['name']}, Age: {student['age']}, Class: {student['class']}")

def main():
    """Main function to run the Student Management System."""
    students = load_data()
    
    while True:
        print("\n--- Student Management System ---")
        print("1. Add Student")
        print("2. Update Student")
        print("3. Delete Student")
        print("4. View Students")
        print("5. Exit")
        
        choice = input("Enter your choice: ").strip()
        if choice == "1":
            add_student(students)
        elif choice == "2":
            update_student(students)
        elif choice == "3":
            delete_student(students)
        elif choice == "4":
            view_students(students)
        elif choice == "5":
            save_data(students)
            print("Exiting... Data saved successfully.")
            break
        else:
            print("Invalid choice! Please try again.")

if __name__ == "__main__":
    main()
