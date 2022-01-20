import pytest
from Test_1 import *
# test_value = ["Яна", "Артём", "Я", "A","AB"]
test_value = ["Яна", "Артём"]

@pytest.mark.parametrize("test_input", test_value)
def test_eval(test_input):
    x = main_Test(test_input, "form_errors", "div")
    assert x == True