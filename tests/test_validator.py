"""
Basic tests for validator service.
"""
import pytest
from app.services.validator import Validator, ValidationError


def test_valid_bill_amount():
    """Test valid bill amount."""
    result = Validator.validate_bill_amount(100.0)
    assert result == 100.0


def test_invalid_bill_amount_negative():
    """Test negative bill amount is rejected."""
    with pytest.raises(ValidationError, match="must be positive"):
        Validator.validate_bill_amount(-10.0)


def test_invalid_bill_amount_non_numeric():
    """Test non-numeric bill amount is rejected."""
    with pytest.raises(ValidationError, match="must be a valid number"):
        Validator.validate_bill_amount("abc")


def test_valid_tip_percentage():
    """Test valid tip percentage."""
    result = Validator.validate_tip_percentage(15.0)
    assert result == 15.0


def test_invalid_tip_percentage_out_of_range():
    """Test tip percentage out of range is rejected."""
    with pytest.raises(ValidationError, match="between 0 and 100"):
        Validator.validate_tip_percentage(150.0)


def test_valid_split_count():
    """Test valid split count."""
    result = Validator.validate_split_count(4)
    assert result == 4


def test_invalid_split_count_zero():
    """Test zero split count is rejected."""
    with pytest.raises(ValidationError, match="at least 1"):
        Validator.validate_split_count(0)


def test_invalid_split_count_non_integer():
    """Test non-integer split count is rejected."""
    with pytest.raises(ValidationError, match="whole number"):
        Validator.validate_split_count("abc")
