import requests
from endpoints.endpoint_handler import Endpoint


class GetUrlEndpoint(Endpoint):
    long = None

    def __init__(self, code):
        self.code = code

    def get_short_info(self):
        response = requests.get(f'https://gotiny.cc/api/{self.code}')
        self.status = response.status_code
        self.long = response.text

    def long_url_is_as_expected(self, expected):
        return self.long == expected
