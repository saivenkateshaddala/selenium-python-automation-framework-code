import pytest

@pytest.mark.skip
def test_add():
    a=10
    b=20
    assert a+b==30

@pytest.mark.xfail
def test_sub():
    x=20
    y=20
    assert x-y == 0

@pytest.mark.sanity
def test_multi():
    a=10
    b=10

    assert a*b==100
    print("it is working")
