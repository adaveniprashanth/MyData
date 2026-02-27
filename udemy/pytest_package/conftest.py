import pytest
from .my_classes import *



@pytest.fixture
def my_circle():
    print("hello")
    return Circle("circle",10)