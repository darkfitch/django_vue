
class Baseresponse(object):
    def __init__(self):
        self.code = 1000
        self.error = None
        self.data = None

    @property
    def dict(self):
        return self.__dict__
