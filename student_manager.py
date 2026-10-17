# Simple Student Management App

students = {
    "101": {"name": "Alice", "course": "CSE", "marks": 85},
    "102": {"name": "Bob", "course": "ECE", "marks": 78},
    "103": {"name": "Charan", "course": "MECH", "marks": 90}
}

def add_student(roll, name, course, marks):
    students[roll] = {"name": name, "course": course, "marks": marks}

def display_students():
    print("=== Student Management App: Student Records ===")
    for roll, info in students.items():
        print(f"Roll: {roll} | Name: {info['name']} | Course: {info['course']} | Marks: {info['marks']}")

if __name__ == "__main__":
    display_students()
