import requests
import random
import string
from endpoints.endpoint_handler import Endpoint


class CreateUrlEndpoint(Endpoint):
    long = None
    code = None

    def __init__(self, long_url=None, custom=False):
        if long_url:
            self.long_url = long_url
        else:
            self.long_url = f'https://{"".join(random.choice(string.ascii_lowercase) for _ in range(10))}.com'
        if custom:
            self.custom = "".join(random.choice(string.ascii_lowercase) for _ in range(10))
        else:
            self.custom = custom

    def post_new_url(self):
        header = {'Content-Type': 'application/json'}
        if self.custom:
            data = {
                'long': self.long_url,
                'custom': self.custom
            }
        else:
            data = {
                'input': self.long_url
            }
        response = requests.post('https://gotiny.cc/api', json=data, headers=header)
        response_json = response.json()[0]
        self.long = response_json['long']
        self.code = response_json['code']
        self.status = response.status_code

    def long_url_is_the_same_as_sent(self):
        return self.long_url == self.long

    def code_is_not_empty(self):
        return len(self.code) > 0

    def code_is_the_same_as_custom(self):
        return self.code == self.custom
