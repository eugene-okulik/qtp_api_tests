import requests
from endpoints.get_url_endpoint import GetUrlEndpoint


def test_get_existing(new_url):
    url, code = new_url
    endpoint = GetUrlEndpoint(code)
    endpoint.get_short_info()
    assert endpoint.status_code_is_200()
    assert endpoint.long_url_is_as_expected(expected=url)
