import pytest

from ..krtc import KerberosTicket


class FakeException(Exception):
    ...


def test_instantiate():
    with pytest.raises(FakeException):  # what will it actually raise?
        KerberosTicket("HTTP@example.com")
