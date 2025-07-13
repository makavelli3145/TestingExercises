from app.fizzbuzz import fizzbuzz
import pytest

@pytest.mark.parametrize("test_input,expected",[(3, "Fizz"), (5, "Buzz"),
                        (15, "FizzBuzz"),(7, "7"),(30, "FizzBuzz"),(14, "14"),
                        (23, "23"),(21, "Fizz"),])
def test_fizzbuzz(test_input, expected):
    assert fizzbuzz(test_input) == expected