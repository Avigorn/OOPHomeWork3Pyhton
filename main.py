from typing import List

from small_data.Student import Student
from small_data.StudentGroup import StudentGroup
from small_data.StudentGroupIterator import StudentGroupIterator
from small_data.Teacher import Teacher


def testIterator(student_group: StudentGroup):
    group_iterator = StudentGroupIterator(student_group)
    while group_iterator.hasNext():
        print(group_iterator.next())


class Main:
    student1 = Student("Ivan", "Ivanov", "Ivanovich", 1)
    student2 = Student("Alexandr", "Alexandrovich", "Alexandrov", 2)
    teacher = Teacher("Vasiliy", "Smirnov", "Petrovich")
    group: List[Student] = [student1, student2]
    group_of_students = StudentGroup(teacher, group)
    testIterator(group_of_students)
