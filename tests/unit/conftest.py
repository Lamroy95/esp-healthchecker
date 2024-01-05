import pytest


@pytest.fixture()
def i2c_mock(mocker):
    return mocker.MagicMock()
