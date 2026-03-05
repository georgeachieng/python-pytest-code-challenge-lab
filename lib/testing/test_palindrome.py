import pytest
from lib.palindrome import longest_palindromic_substring

@pytest.mark.parametrize(
    "input_str,expected",
    [
        ("cbbd", "bb"),
        ("a", "a"),
        ("racecar", "racecar"),
        ("", ""),
        ("aaaa", "aaaa"),
        ("1221", "1221"),
        ("abc123321xyz", "123321"),
    ],
)
def test_exact_expected_outputs(input_str, expected):
    assert longest_palindromic_substring(input_str) == expected


@pytest.mark.parametrize(
    "input_str,valid_outputs",
    [
        ("babad", {"bab", "aba"}),
        ("ac", {"a", "c"}),
        ("xyz", {"x", "y", "z"}),
    ],
)
def test_multiple_valid_outputs(input_str, valid_outputs):
    assert longest_palindromic_substring(input_str) in valid_outputs


def test_large_input_size():
    s = ("abc" * 170) + "abbaabba" + ("def" * 170)
    assert longest_palindromic_substring(s) == "abbaabba"


@pytest.mark.parametrize("bad_input", [12345, None, ["a", "b"], {"k": "v"}])
def test_non_string_input_raises_type_error(bad_input):
    with pytest.raises(TypeError):
        longest_palindromic_substring(bad_input)
