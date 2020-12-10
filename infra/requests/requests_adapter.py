import requests

from infra.requests.base_get_requester import BaseGetRequester


class RequestsAdapter(BaseGetRequester):

    def get(self, url):
        return requests.get(url)
