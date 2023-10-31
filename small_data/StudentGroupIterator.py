from abc import ABC

from small_data.Student import Student
from typing import List, Iterable

from small_data.StudentGroup import StudentGroup


class StudentGroupIterator(Student):
    __counter: int

    _students: List[Student]

    def __init__(self, student_group: StudentGroup):
        self._students = student_group.getStudents()
        self.__counter = 0

    def hasNext(self):
        return self.__counter < len(self._students)

    def next(self):
        if not self.hasNext():
            return None
        self.__counter += 1
        return self._students[self.__counter - 1]
