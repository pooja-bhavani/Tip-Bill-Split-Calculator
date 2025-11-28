"""
API routes for tip calculator.
"""
from flask import Blueprint, request, jsonify
from app.services.calculator import CalculatorService
from app.services.validator import Validator, ValidationError

api_bp = Blueprint('api', __name__)


@api_bp.route('/api-us-west-2/prod/ai/data', methods=['POST'])
def calculate_bill():
    """
    Calculate tip, total, and per-person amounts.
    
    Expected JSON body:
    {
        "bill_amount": float,
        "tip_percentage": float,
        "split_count": int
    }
    
    Returns:
        JSON response with calculated values or error message
    """
    try:
        # Get request data
        data = request.get_json()
        
        if data is None:
            return jsonify({
                "success": False,
                "error": "Request body must be JSON"
            }), 400
        
        # Extract inputs
        bill_amount = data.get('bill_amount')
        tip_percentage = data.get('tip_percentage')
        split_count = data.get('split_count')
        
        # Check for missing fields
        if bill_amount is None or tip_percentage is None or split_count is None:
            return jsonify({
                "success": False,
                "error": "Missing required fields: bill_amount, tip_percentage, split_count"
            }), 400
        
        # Validate inputs
        validated = Validator.validate_all(bill_amount, tip_percentage, split_count)
        
        # Perform calculations
        tip_amount = CalculatorService.calculate_tip(
            validated['bill_amount'],
            validated['tip_percentage']
        )
        
        total_amount = CalculatorService.calculate_total(
            validated['bill_amount'],
            tip_amount
        )
        
        per_person_amount = CalculatorService.calculate_per_person(
            total_amount,
            validated['split_count']
        )
        
        breakdown = CalculatorService.calculate_breakdown(
            validated['bill_amount'],
            tip_amount,
            validated['split_count']
        )
        
        # Return success response
        return jsonify({
            "success": True,
            "data": {
                "bill_amount": validated['bill_amount'],
                "tip_percentage": validated['tip_percentage'],
                "tip_amount": tip_amount,
                "total_amount": total_amount,
                "split_count": validated['split_count'],
                "per_person_amount": per_person_amount,
                "breakdown": breakdown
            }
        }), 200
        
    except ValidationError as e:
        return jsonify({
            "success": False,
            "error": str(e)
        }), 400
        
    except Exception as e:
        return jsonify({
            "success": False,
            "error": "An unexpected error occurred"
        }), 500
