import pytest


def pytest_addoption(parser):
    parser.addoption("--url", action="store", default="https://ya.ru", help="Base URL for the test")
    parser.addoption("--status_code", action="store", default=200, type=int, help="Expected status code for the test")


@pytest.fixture
def url(request):
    return request.config.getoption("--url")


@pytest.fixture
def status_code(request):
    return request.config.getoption("--status_code")
