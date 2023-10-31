from typing import List

from datetime import date

from small_data.Student import Student
from small_data.User import User


class DataService:

    __users: List[User]

    def __init__(self):
        self.__users = []

    def getAll(self):
        return self.__users

    def create(self, first_name, second_name, patronymic, date_of_birth: date):
        count_max_id = 0
        for user in self.__users:
            if isinstance(user, Student):
                if user.getStudentId() > count_max_id:
                    count_max_id = user.getStudentId()
        count_max_id += 1

        student: Student = Student(first_name, second_name, patronymic, date_of_birth, count_max_id)
        self.__users.append(student)
