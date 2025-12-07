class ResultService:
    def init(self):
        self.results = {}  # (studentID, courseCode) -> letterGrade

    def register_result(self, student_service, course_service):
        sid = input("Enter Student ID: ")
        if sid not in student_service.students:
            print("Student not found!")
            return

        code = input("Enter Course Code: ")
        if code not in course_service.courses:
            print("Course not found!")
            return

        grade = input("Enter Letter Grade (A-F): ").upper()

        self.results[(sid, code)] = grade
        print("Result recorded successfully!")

    def list_results(self):
        print("\nRecorded Results:")
        for key, grade in self.results.items():
            sid, code = key
            print(f"Student {sid} | Course {code} | Grade {grade}")

    def menu(self, students, courses):
        print("\n--- RESULTS MENU ---")
        print("1. Record Result")
        print("2. List Results")

        ch = input("Choose: ")

        if ch == "1":
            self.register_result(students, courses)
        elif ch == "2":
            self.list_results()
        else:
            print("Invalid choice.")