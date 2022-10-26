class NotFoundException(Exception):
    def __init__(self, *args):
        if args:
            self.message = args[0]
        else:
            self.message = "Not found"

class UnprocessableEntityException(Exception):
    def __init__(self, *args):
        if args:
            self.message = args[0]
        else:
            self.message = "Cannot process request"

class NotAuthorizedException(Exception):
    def __init__(self, *args):
        if args:
            self.message = args[0]
        else:
            self.message = "Not authorized to perform this action"

class NotAuthenticatedException(Exception):
    def __init__(self, *args):
        if args:
            self.message = args[0]
        else:
            self.message = "Request is not authenticated"
