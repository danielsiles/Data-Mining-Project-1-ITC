import datetime


class BaseModel:
    def __init__(self, *args):
        print(args)
        if len(args) > 0:
            self._id = args[0]
        else:
            self._id = None
        self._created_at = datetime.datetime.now()
        self._updated_at = datetime.datetime.now()
