import pytest
from endpoints.create_url_endpoint import CreateUrlEndpoint


@pytest.fixture()
def new_url():
    endpoint = CreateUrlEndpoint()
    endpoint.post_new_url()
    return endpoint.long_url, endpoint.code
