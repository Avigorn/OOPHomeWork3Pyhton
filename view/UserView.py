import logging


class UserView:
    def __init__(self):
        self.logger = logging.getLogger(UserView.__class__.__name__)

    def sendOnConsole(self, user_list):
        for User in user_list:
            self.logger.info(User.__str__())

    def sendOnConsoleUserGroup(self, student_group):
        self.logger.info(student_group.__str__())

    def sendOnConsoleListStudent(self, students):
        self.logger.info(students.__str__())
