import datetime


class BaseModel:
    def __init__(self, *args):
        self._id = None
        if len(args) > 0:
            self._id = args[0]
        self._created_at = datetime.datetime.now()
        self._updated_at = datetime.datetime.now()
