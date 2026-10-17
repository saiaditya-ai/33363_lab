# Simple Student Management App

students = {
    "101": {"name": "Aditya", "course": "CSE", "marks": 85},
    "102": {"name": "Surya", "course": "ECE", "marks": 78}
}

def display_students():
    print("--- Student Details ---")
    for roll, info in students.items():
        print(f"Roll: {roll} | Name: {info['name']} | Course: {info['course']} | Marks: {info['marks']}")

if __name__ == "__main__":
    display_students()
