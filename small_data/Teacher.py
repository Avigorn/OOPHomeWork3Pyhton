from small_data.User import User


class Teacher(User):

    __teacher_id: int

    def __init__(self, first_name, surname, patronymic):
        super().__init__(first_name, surname, patronymic)

    def getTeacherId(self):
        return self.__teacher_id

    def setTeacherId(self, teacher_id):
        self.__teacher_id = teacher_id

    class TeacherComparator:
        @staticmethod
        def compare(o1, o2):
            return 0
