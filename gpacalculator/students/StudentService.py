class StudentService:
    def init(self):
        self.students = {}  # id -> name

    def register_student(self):
        sid = input("Enter Student ID: ")
        name = input("Enter Student Name: ")

        self.students[sid] = name
        print("Student registered successfully!")

    def list_students(self):
        print("\nRegistered Students:")
        for sid, name in self.students.items():
            print(f"{sid} - {name}")

    def menu(self):
        print("\n--- STUDENTS MENU ---")
        print("1. Register Student")
        print("2. List Students")

        ch = input("Choose: ")

        if ch == "1":
            self.register_student()
        elif ch == "2":
            self.list_students()
        else:
            print("Invalid choice.")