"""
Basic tests for calculator service.
"""
import pytest
from app.services.calculator import CalculatorService


def test_calculate_tip():
    """Test tip calculation."""
    result = CalculatorService.calculate_tip(100.0, 15.0)
    assert result == 15.0


def test_calculate_total():
    """Test total calculation."""
    result = CalculatorService.calculate_total(100.0, 15.0)
    assert result == 115.0


def test_calculate_per_person():
    """Test per person calculation."""
    result = CalculatorService.calculate_per_person(115.0, 4)
    assert result == 28.75


def test_rounding():
    """Test rounding to 2 decimal places."""
    result = CalculatorService.calculate_tip(100.0, 15.5)
    assert result == 15.5
    
    result = CalculatorService.calculate_per_person(100.0, 3)
    assert result == 33.33
