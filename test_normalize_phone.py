import pytest
from normalize_phone import normalize_phone

# Valid Cases
@pytest.mark.parametrize("phone, expected", [
    ("+9779841234567", "+9779841234567"),  # Starts with +977 and 10 digits
    ("09841234567", "+9779841234567"),    # Starts with 0 and length 11
    ("9841234567", "+9779841234567"),     # Exactly 10 digits starting with 98
    ("9741234567", "+9779741234567"),     # Exactly 10 digits starting with 97
])
def test_valid_phone_numbers(phone, expected):
    assert normalize_phone(phone) == expected

# Invalid Cases
@pytest.mark.parametrize("phone", [
    ("1234567890"),       # 10 digits but doesn't start with 98 or 97
    ("+977984123456"),    # Starts with +977 but only 9 digits after it
    ("0984123456"),       # Starts with 0 but length 10
    ("984123456"),        # Only 9 digits
    ("abc1234567"),       # Non-numeric characters
])
def test_invalid_phone_numbers(phone):
    with pytest.raises(ValueError, match="Invalid phone number"):
        normalize_phone(phone)

# Edge Cases
@pytest.mark.parametrize("phone, expected", [
    ("98-4123-4567", "+9779841234567"),   # Contains dashes
    ("98 4123 4567", "+9779841234567"),   # Contains spaces
    (" 98-4123 4567 ", "+9779841234567"), # Mixed spaces and dashes with leading/trailing spaces
])
def test_edge_cases(phone, expected):
    assert normalize_phone(phone) == expected