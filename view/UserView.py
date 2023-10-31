import logging


class UserView:
    def __init__(self):
        self.logger = logging.getLogger(UserView.__class__.__name__)
