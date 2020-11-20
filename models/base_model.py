import datetime


class BaseModel:
    def __init__(self, model_id):
        self._id = model_id
        self._created_at = datetime.datetime.now()
        self._updated_at = datetime.datetime.now()
