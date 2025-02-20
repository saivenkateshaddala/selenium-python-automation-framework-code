import pytest


@pytest.fixture(autouse="True")
def loginsuccess():
    print("Searching for the browser")
    print("login to the web site ")
    yield
    print("Logout for the browser")

def test_additems():
    print("Search the product")
    print("Add it into the cart")

def test_remove():
    print("Go to cart")
    print("Remove the item into the cart")

