class GradeReport:

    def grade_point(self, letter):
        table = {
            "A": 4.0,
            "B+": 3.5,
            "B": 3.0,
            "C+": 2.5,
            "C": 2.0,
            "D": 1.0,
            "F": 0.0
        }
        return table.get(letter.upper(), 0.0)

    def generate_report(self, students, courses, results):
        sid = input("Enter Student ID: ")

        if sid not in students.students:
            print("Student not found!")
            return

        print(f"\nGRADE REPORT FOR {students.students[sid]}")

        total_points = 0
        total_credits = 0

        for (st_id, code), grade in results.results.items():
            if st_id == sid:
                title, credit = courses.courses[code]
                gp = self.grade_point(grade)

                print(f"{code} - {title}: Grade {grade}, Credit {credit}")

                total_points += gp * credit
                total_credits += credit

        if total_credits == 0:
            print("No courses found for this student.")
            return

        gpa = total_points / total_credits
        print(f"\nTotal Credits: {total_credits}")
        print(f"GPA: {gpa:.2f}")