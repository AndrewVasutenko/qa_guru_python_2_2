import pytest

@pytest.fixture(scope="session", autouse=True)
def open_browser():
    print("Я вызываюсь перед тестом!")
    yield
    print("Я выполняюсь после теста")