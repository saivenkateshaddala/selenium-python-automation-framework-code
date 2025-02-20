import pytest

@pytest.mark.sanity
def test_login():
    print("Loginsuccess")
@pytest.mark.sanity
def test_logout():
    print("logout successfully")
@pytest.mark.xfail
def test_multi():
    a=10
    b=30
    assert a*b==300