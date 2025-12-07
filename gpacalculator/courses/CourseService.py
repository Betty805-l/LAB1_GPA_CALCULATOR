class CourseService:
    def init(self):
        self.courses = {}  # code -> (title, credit)

    def register_course(self):
        code = input("Enter Course Code: ")
        title = input("Enter Course Title: ")
        credit = int(input("Enter Credit Hours: "))

        self.courses[code] = (title, credit)
        print("Course registered successfully!")

    def list_courses(self):
        print("\nAvailable Courses:")
        for code, data in self.courses.items():
            print(f"{code} - {data[0]} ({data[1]} credits)")

    def menu(self):
        print("\n--- COURSES MENU ---")
        print("1. Register Course")
        print("2. List Courses")

        ch = input("Choose: ")

        if ch == "1":
            self.register_course()
        elif ch == "2":
            self.list_courses()
        else:
            print("Invalid choice.")