from app.fizzbuzz import fizzbuzz
import pytest

@pytest.mark.parametrize("test_input,expected",[(3, "Fizz"), (5, "Buzz"), (15, "FizzBuzz")])
def test_fizzbuzz(test_input, expected):
    assert fizzbuzz(test_input) == expected