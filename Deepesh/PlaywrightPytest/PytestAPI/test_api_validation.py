import json

import pytest
from playwright.sync_api import Playwright, APIRequestContext


def test_api_request_and_verify(playwright: Playwright):
    headers = {
        "Accept": "application/json",
        "Authorization": "token Bearer b9b3492b489c402fe0cd7e9299e6fc7b172ccf67407937d21904aaffba74802e",
    }
    requests_context = playwright.request.new_context(base_url="https://gorest.co.in",
                                                      extra_http_headers=headers)
    response = requests_context.get("/public/v2/users/8075634")
    print(response.json())
    print(response.status)
