import pytest
from palindrome import is_palindrome


@pytest.mark.parametrize("text", (
        "Borrow or rob?",
        "Al lets Della call Ed \"Stella\""
))
def test_is_palindrome(text):
    assert is_palindrome(text)


@pytest.mark.parametrize("text", (
        "hello",
        "Momm"
))
def test_is_not_palidrome(text):
    assert not is_palindrome(text)
