from service.DataService import DataService
from service.StudentGroupService import StudentGroupService
from view.UserView import UserView


class UserController:

    _data_service: DataService = []

    _student_group_service: StudentGroupService = []

    _user_view: UserView = []
