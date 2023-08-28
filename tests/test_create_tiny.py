import requests

from endpoints.create_url_endpoint import CreateUrlEndpoint


def test_create_short_url():
    url = 'https://kasjdfkajshifwqyejhasgdf.com'
    endpoint = CreateUrlEndpoint(url)
    endpoint.post_new_url()
    assert endpoint.status_code_is_200()
    assert endpoint.long_url_is_the_same_as_sent()
    assert endpoint.code_is_not_empty()


def test_custom_short_url():
    endpoint = CreateUrlEndpoint(custom=True)
    endpoint.post_new_url()
    assert endpoint.status_code_is_200()
    assert endpoint.long_url_is_the_same_as_sent()
    assert endpoint.code_is_the_same_as_custom()
