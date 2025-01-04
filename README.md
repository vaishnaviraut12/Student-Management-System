# 📚 Student Management System  

A simple **Student Management System (SMS)** built using **Python**. This program allows you to manage student records efficiently by adding, updating, deleting, and viewing data. The student data is stored persistently using a JSON file for easy retrieval and modification.  

## ✨ Features  

- ➕ **Add a Student**: Add a new student record with roll number, name, age, and class.  
- ✏️ **Update a Student**: Modify existing student details using their roll number.  
- ❌ **Delete a Student**: Remove a specific student record from the database.  
- 📋 **View All Students**: Display all stored student records in a user-friendly format.  
- 💾 **Persistent Storage**: Save all data to a JSON file (`students.json`) for long-term access.  

## 🛠️ Installation  

1. **Clone the repository**:  
   ```bash
   git clone https://github.com/<your-username>/<repository-name>.git
   cd <repository-name>
   ```  

2. **Run the program**:  
   Execute the script using Python:  
   ```bash
   python <filename>.py
   ```  

## 📂 File Structure  

```
📦 <repository-name>
 ┣ 📜 students.json      # File where student data is stored
 ┣ 📜 <filename>.py      # Main Python script
 ┗ 📜 README.md          # Documentation file
```  
## 🚀 How to Use  

1. 🏗️ **Start the Program**:  
   Run the Python script to launch the Student Management System.  

2. 🎛️ **Interactive Menu**:  
   - `1. Add Student`: Input details to add a new student.  
   - `2. Update Student`: Modify details of an existing student.  
   - `3. Delete Student`: Remove a student from the system.  
   - `4. View Students`: Display all stored student records.  
   - `5. Exit`: Save data to the file and exit the program.  

3. 💾 **Persistent Storage**:  
   All changes are automatically saved in students.json.

## 🖼️ Example  

**Interactive Menu:**  
```plaintext
--- Student Management System ---
1. Add Student
2. Update Student
3. Delete Student
4. View Students
5. Exit
Enter your choice: 
```  

**Sample Output for Viewing Students:**  
```plaintext
--- Student Records ---
Roll Number: 101, Name: John Doe, Age: 18, Class: 12A
Roll Number: 102, Name: Jane Smith, Age: 19, Class: 12B
```  
