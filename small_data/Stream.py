from abc import ABC
from typing import Iterable

from small_data.StudentGroup import StudentGroup


class Stream(Iterable, ABC, StudentGroup):

    __stream_id = []

    def __init__(self, stream_name, stream_id=None):
        self.stream_name = stream_name
        self.__stream_id = stream_id

    def getStreamName(self):
        return self.stream_name

    def getStreamID(self):
        return self.__stream_id

    def __str__(self):
        return f"Stream {{stream_id='{self.__stream_id}', stream_name='{self.__stream_id}}}"

    def __lt__(self, other):
        return self.__stream_id.compare_to.other.__stream_id
