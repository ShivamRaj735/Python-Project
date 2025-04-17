import matplotlib.pyplot as plt

students = {}
def add_student():
    student_id = input("Enter student ID: ")
    name = input("Enter student name: ")
    marks = input("Enter marks: ")
    marks = list(map(int, marks))
    
    students[student_id] = {
        "name": name,
        "marks": marks,
        "gpa": calculate_gpa(marks)
    }
    print("Student added successfully!")

def update_student():
    student_id = input("Enter student ID to update: ")
    if student_id not in students:
        print("Student not found!")
        return
    
    name = input("Enter new name: ")
    marks = input("Enter new marks: ")
    marks = list(map(int, marks))
    
    students[student_id] = {
        "name": name,
        "marks": marks,
        "gpa": calculate_gpa(marks)
    }
    print("Student updated successfully!")

def delete_student():
    student_id = input("Enter student ID to delete: ")
    if student_id in students:
        del students[student_id]
        print("Student deleted successfully!")
    else:
        print("Student not found!")

def view_performance():
    print("\nStudent Performance Summary:")
    for student_id, info in students.items():
        print(f"{info['name']} (ID: {student_id}) - GPA: {info['gpa']:.2f}")

def calculate_gpa(marks):
    return sum(marks) / len(marks) if marks else 0


def class_topper():
    if not students:
        print("No student records available.")
        return
    topper = max(students.values(), key=lambda x: x['gpa'])
    print(f"Class Topper: {topper['name']} (GPA: {topper['gpa']:.2f})")

def visualize_data():
    if not students:
        print("No student records available.")
        return
    
    print("\n--- GPA Distribution ---")
    for student_id, info in students.items():
        print(f"{info['name']} (GPA: {info['gpa']:.2f})")

def main():
    while True:
        print("\n ~~~~Admin System~~~~   ")
        print("1. Add Student")
        print("2. Update Student")
        print("3. Delete Student")
        print("4. View Performance Summary")
        print("5. Class Topper")
        print("6. Visualize Data")
        print("7. Exit")
        
        choice = input("Choose an option: ")
        
        if choice == "1":
            add_student()
        elif choice == "2":
            update_student()
        elif choice == "3":
            delete_student()
        elif choice == "4":
            view_performance()
        elif choice == "5":
            class_topper()
        elif choice == "6":
            visualize_data()
        elif choice == "7":
            print("Exiting...")
            break
        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    main()
