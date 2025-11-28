"""
Calculator service for tip and bill split calculations.
"""


class CalculatorService:
    """Service class for performing bill, tip, and split calculations."""
    
    @staticmethod
    def calculate_tip(bill_amount: float, tip_percentage: float) -> float:
        """
        Calculate tip amount based on bill amount and tip percentage.
        
        Args:
            bill_amount: The pre-tip bill amount
            tip_percentage: The tip percentage (0-100)
            
        Returns:
            Tip amount rounded to 2 decimal places
        """
        tip_amount = bill_amount * (tip_percentage / 100)
        return round(tip_amount, 2)
    
    @staticmethod
    def calculate_total(bill_amount: float, tip_amount: float) -> float:
        """
        Calculate total amount including tip.
        
        Args:
            bill_amount: The pre-tip bill amount
            tip_amount: The calculated tip amount
            
        Returns:
            Total amount rounded to 2 decimal places
        """
        total = bill_amount + tip_amount
        return round(total, 2)
    
    @staticmethod
    def calculate_per_person(total_amount: float, split_count: int) -> float:
        """
        Calculate per person amount when splitting the bill.
        
        Args:
            total_amount: The total amount including tip
            split_count: Number of people splitting the bill
            
        Returns:
            Per person amount rounded to 2 decimal places
        """
        per_person = total_amount / split_count
        return round(per_person, 2)
    
    @staticmethod
    def calculate_breakdown(bill_amount: float, tip_amount: float, split_count: int) -> dict:
        """
        Calculate detailed breakdown of bill per person and tip per person.
        
        Args:
            bill_amount: The pre-tip bill amount
            tip_amount: The calculated tip amount
            split_count: Number of people splitting the bill
            
        Returns:
            Dictionary with bill_per_person and tip_per_person
        """
        bill_per_person = round(bill_amount / split_count, 2)
        tip_per_person = round(tip_amount / split_count, 2)
        
        return {
            "bill_per_person": bill_per_person,
            "tip_per_person": tip_per_person
        }
