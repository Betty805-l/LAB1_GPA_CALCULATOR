from students.StudentService import StudentService
from courses.CourseService import CourseService
from results.ResultService import ResultService
from gradereports.GradeReport import GradeReport

students = StudentService()
courses = CourseService()
results = ResultService()
report = GradeReport()

def main_menu():
    while True:
        print("\n===== GPA CALCULATOR MENU =====")
        print("1. Students")
        print("2. Courses")
        print("3. Results")
        print("4. Grade Reports")
        print("5. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            students.menu()

        elif choice == "2":
            courses.menu()

        elif choice == "3":
            results.menu(students, courses)

        elif choice == "4":
            report.generate_report(students, courses, results)

        elif choice == "5":
            print("Goodbye!")
            break

        else:
            print("Invalid input. Try again.")

if name == "main":
    main_menu()