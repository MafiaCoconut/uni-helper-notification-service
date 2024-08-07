from enum import Enum


class ErrorCodes(Enum):
    INCORRECT_DATA = "Incorrect data"


class JobException(Exception):
    pass


class JobInvalidData(JobException):
    def __init__(self, message=ErrorCodes.INCORRECT_DATA.value):
        self.message = message
        super().__init__(self.message)

