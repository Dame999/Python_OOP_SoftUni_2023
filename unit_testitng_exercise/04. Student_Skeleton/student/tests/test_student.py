from unittest import TestCase, main

from project.student import Student


class TestStudent(TestCase):
    def setUp(self) -> None:
        self.student = Student("Peter")
        self.student_with_courses = Student("Peter", {"math": ["note"]})

    def test_if_initialization_is_correct(self):
        self.assertEqual(self.student.name, "Peter")
        self.assertEqual(self.student.courses, {})
        self.assertEqual(self.student_with_courses.courses, {"math": ["note"]})

    def test_enroll_if_course_name_exists_in_courses_list_returns_correct_text(self):
        result = self.student_with_courses.enroll("math", ["second note"])
        self.assertEqual(self.student_with_courses.courses, {"math": ["note", "second note"]})
        self.assertEqual("Course already added. Notes have been updated.", result)

    def test_enroll_adds_course_name_and_course_notes_returns_correct_text(self):
        result = self.student.enroll("math", ["note", "second note"], "Y")
        self.assertEqual(self.student.courses, {"math": ["note", "second note"]})
        self.assertEqual(result, "Course and course notes have been added.")

    def test_enroll_adds_course_name_and_course_notes_without_third_parameter_returns_correct_text(self):
        result = self.student.enroll("math", ["note", "second note"])
        self.assertEqual(self.student.courses, {"math": ["note", "second note"]})
        self.assertEqual(result, "Course and course notes have been added.")

    def test_enroll_adds_only_the_course_without_the_notes_and_returns_the_correct_message(self):
        result = self.student.enroll("math", ["note", "second note"], "N")
        self.assertEqual(self.student.courses, {"math": []})
        self.assertEqual(result, "Course has been added.")

    def test_add_notes_to_the_course_notes_if_course_name_in_courses_than_returns_correct_message(self):
        result = self.student_with_courses.add_notes("math", "algebra")
        self.assertEqual(self.student_with_courses.courses, {"math": ["note", "algebra"]})
        self.assertEqual(result, "Notes have been updated")

    def test_add_notes_raises_exception_when_the_course_does_not_exists_in_the_student_courses(self):
        with self.assertRaises(Exception) as error:
            self.student.add_notes("math", ["algebra"])

        self.assertEqual(str(error.exception), "Cannot add notes. Course not found.")

    def test_leave_course_removes_course_from_courses_and_returns_correct_message(self):
        result = self.student_with_courses.leave_course("math")
        self.assertEqual(self.student_with_courses.courses, {})
        self.assertEqual(result, "Course has been removed")

    def test_leave_course_raises_exception_when_the_course_does_not_exists_in_the_courses(self):
        with self.assertRaises(Exception) as error:
            self.student.leave_course("math")

        self.assertEqual(str(error.exception), "Cannot remove course. Course not found.")


if __name__ == "__main__":
    main()
