from enum import Enum


class ErrorCodes(Enum):
    INCORRECT_DATA = "Incorrect data"
    NOT_FOUND = "Job not found"


class JobException(Exception):
    pass


class JobInvalidData(JobException):
    def __init__(self, message=ErrorCodes.INCORRECT_DATA.value):
        self.message = message
        super().__init__(self.message)


class JobNotExisted(JobException):
    def __init__(self, message=ErrorCodes.NOT_FOUND.value):
        self.message = message
        super().__init__(self.message)



