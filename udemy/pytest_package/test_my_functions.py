import math
import time

import pytest
import unittest.mock as mock

from .my_functions import *

# For reference --> https://www.youtube.com/watch?v=cHYq1MRoyI0&t=967s

# Function based tests

def test_add():
    result = add(1, 2)
    assert result == 3

def test_add_strings():
    result=add("hello ","world")
    assert result == "hello world"

def test_divide():
    result=divide(3,2)
    assert result == 1.5

def test_divide_with_zero():
    with pytest.raises(ZeroDivisionError): #for handling errors
        divide(3, 0)

from .my_classes import *
# class based tests
class Testclass:
    # setter and teardwon methods will work on all test cases
    # command to activate setter and teardown methods ==> pytest -s

    def setup_method(self,method): #method name should be like "setup_method"
        print(f"starting the {method}")
        self.circle=Circle("circle",10) #creating the circle object
        self.rectanlge=Rectangle("rectanbgle",10,20)

    # this method will work as cleaning method
    def teardown_method(self,method): #method name should be like "setup_method"
        print(f"completed the {method}")
        del self.circle
        del self.rectanlge

    def test_circle_area(self):
        assert self.circle.area()==math.pi *self.circle.radius **2

    def test_rectangle_perimeter(self):
        assert self.rectanlge.perimeter() == 2*(self.rectanlge.length+self.rectanlge.width)

    def test_circle_perimeter(self):
        result=self.circle.perimeter()
        expected = 2* math.pi * self.circle.radius
        assert result == expected


# ==> Fixtures

# by using fixtures, No need to create the objects multiple times
@pytest.fixture
def my_rectangle():
    return Rectangle("rectangle",10,20)

# added other fixtures in conftest.py to available globally

def test_rect_perimeter(my_rectangle):
    assert my_rectangle.perimeter() == 2*(10+20)

def test_rect_area(my_rectangle):
    assert my_rectangle.area() == my_rectangle.length * my_rectangle.width

def test_circle_area(my_circle):
    assert my_circle.area() == math.pi* my_circle.radius**2


#  ==> Marking and parameterize

# marking the test as slow test
# to run pytest -m <filename>
@pytest.mark.slow
def test_add_slow():
    time.sleep(5)#adding the sleep
    result=add(3,4)
    assert result == 7


# skipping the testcase due to to issue
@pytest.mark.skip(reason="broken functionality as of now")
def test_add():
    result = add(1,2)
    assert result == 3

# making the testcase as failed
# so no  need to test the functionality
@pytest.mark.xfail(reason="cannot divide by 0")
def test_dicide_fail():
    result = divide(10,0)
    assert True


# testing the single test case with multiple values
@pytest.mark.parametrize("side,expected_area",[(5,25),(6,36),(10,100),(7,49)])
def test_find_multiple_areas(side,expected_area):
    assert Square(side).area() == expected_area

@pytest.mark.parametrize("length,width,expected_perimeter,expected_area",[(5,10,30,50),(2,3,10,6),(4,5,18,20)])
def test_find_perimeter_area(length,width,expected_perimeter,expected_area):
    assert Rectangle("rectangle",length,width).perimeter()==expected_perimeter
    assert Rectangle("rectangle",length,width).area() == expected_area


#  ==> Mocking
import pytest_package.my_mock_data as my_mock_data

# testing without mocing the data
def test_data_without_mock():
    result=my_mock_data.get_user_from_id(1)
    expected_result="ram"
    assert result == expected_result

# testing with mock data
@mock.patch("pytest_package.my_mock_data.get_user_from_id")#mocing the function i.e overriding the function result
def test_data_with_mock(mock_get_user_from_id):
    mock_get_user_from_id.return_value="mocked_ram" #creating the mocked result
    result = my_mock_data.get_user_from_id(1) #so it returns mocked value instead of original value
    assert result == "mocked_ram"


# mocking the API requests
