"""
Input validation service for tip calculator.
"""


class ValidationError(Exception):
    """Custom exception for validation errors."""
    pass


class Validator:
    """Service class for validating user inputs."""
    
    @staticmethod
    def validate_bill_amount(bill_amount) -> float:
        """
        Validate bill amount input.
        
        Args:
            bill_amount: The bill amount to validate
            
        Returns:
            Validated bill amount as float
            
        Raises:
            ValidationError: If bill amount is invalid
        """
        try:
            amount = float(bill_amount)
        except (TypeError, ValueError):
            raise ValidationError("Bill amount must be a valid number")
        
        if amount < 0:
            raise ValidationError("Bill amount must be positive")
        
        return amount
    
    @staticmethod
    def validate_tip_percentage(tip_percentage) -> float:
        """
        Validate tip percentage input.
        
        Args:
            tip_percentage: The tip percentage to validate
            
        Returns:
            Validated tip percentage as float
            
        Raises:
            ValidationError: If tip percentage is invalid
        """
        try:
            percentage = float(tip_percentage)
        except (TypeError, ValueError):
            raise ValidationError("Tip percentage must be a valid number")
        
        if percentage < 0 or percentage > 100:
            raise ValidationError("Tip percentage must be between 0 and 100")
        
        return percentage
    
    @staticmethod
    def validate_split_count(split_count) -> int:
        """
        Validate split count input.
        
        Args:
            split_count: The split count to validate
            
        Returns:
            Validated split count as integer
            
        Raises:
            ValidationError: If split count is invalid
        """
        try:
            count = int(split_count)
        except (TypeError, ValueError):
            raise ValidationError("Split count must be a whole number")
        
        if count < 1:
            raise ValidationError("Split count must be at least 1")
        
        return count
    
    @staticmethod
    def validate_all(bill_amount, tip_percentage, split_count) -> dict:
        """
        Validate all inputs at once.
        
        Args:
            bill_amount: The bill amount to validate
            tip_percentage: The tip percentage to validate
            split_count: The split count to validate
            
        Returns:
            Dictionary with validated values
            
        Raises:
            ValidationError: If any input is invalid
        """
        return {
            "bill_amount": Validator.validate_bill_amount(bill_amount),
            "tip_percentage": Validator.validate_tip_percentage(tip_percentage),
            "split_count": Validator.validate_split_count(split_count)
        }
