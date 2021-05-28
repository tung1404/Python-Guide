import requests


def get_my_ip():
    """
    Just my ip adders
    """
    response = requests.get("http://ipinfo.io/json")
    return response


def test_get_my_ip(monkeypatch):
    my_ip = "111.111.111.111"

    class MockResponse:
        def __init__(self, json_body):
            self.json_body = json_body

        def json(self):
            return self.json_body

        monkeypatch.setattr(
            requests, "get", lambda *args, **kargs: MockResponse({"ip": my_ip})
        )

    assert get_my_ip() == my_ip
