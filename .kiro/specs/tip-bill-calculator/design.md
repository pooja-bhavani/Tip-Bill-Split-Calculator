# Design Document

## Overview

The Tip & Bill Split Calculator is a full-stack web application built with Python Flask backend and a modern glassmorphism-styled frontend. The application provides real-time bill calculations, tip computations, and bill splitting functionality with visual data representations through charts and graphs. The architecture follows a client-server model where the frontend sends calculation requests to Flask API endpoints, and the server responds with computed values in JSON format.

## Architecture

### System Architecture

The application follows a three-tier architecture:

1. **Presentation Layer (Frontend)**
   - HTML/CSS/JavaScript interface with glassmorphism styling
   - Chart.js or similar library for data visualization
   - Responsive design for mobile and desktop
   - Real-time input validation and UI updates

2. **Application Layer (Backend)**
   - Flask web server running on port 8000
   - RESTful API endpoints at `/api-us-west-2/prod/ai/data`
   - Business logic for calculations
   - Input validation and error handling

3. **No Persistence Layer**
   - Stateless API design
   - No database required
   - All calculations performed on-demand

### Technology Stack

- **Backend**: Python 3.x with Flask framework
- **Frontend**: HTML5, CSS3 (with glassmorphism effects), Vanilla JavaScript
- **Visualization**: Chart.js for pie charts and bar graphs
- **Environment**: Python virtual environment (venv)
- **API Format**: JSON for request/response payloads

## Components and Interfaces

### Backend Components

#### 1. Flask Application (`app.py`)
Main application entry point that initializes the Flask server and registers routes.

```python
# Pseudo-interface
class FlaskApp:
    def __init__(self):
        # Initialize Flask app
        # Configure CORS for frontend access
        # Register blueprints/routes
    
    def run(self, host='0.0.0.0', port=8000):
        # Start the Flask development server
```

#### 2. Calculation Service (`services/calculator.py`)
Core business logic for all calculations.

```python
class CalculatorService:
    def calculate_tip(self, bill_amount: float, tip_percentage: float) -> float:
        # Returns tip amount
    
    def calculate_total(self, bill_amount: float, tip_amount: float) -> float:
        # Returns total amount
    
    def calculate_per_person(self, total_amount: float, split_count: int) -> float:
        # Returns per person amount
    
    def validate_inputs(self, bill_amount: float, tip_percentage: float, split_count: int) -> dict:
        # Returns validation result with errors if any
```

#### 3. API Routes (`routes/api.py`)
Defines the REST API endpoints.

```python
# POST /api-us-west-2/prod/ai/data
def calculate_bill():
    # Request body: { bill_amount, tip_percentage, split_count }
    # Response: { tip_amount, total_amount, per_person_amount, breakdown }
```

### Frontend Components

#### 1. Main Calculator Interface (`static/index.html`)
Primary user interface with input fields and result displays.

#### 2. Glassmorphism Styles (`static/css/styles.css`)
CSS styling with:
- `backdrop-filter: blur()` for frosted glass effect
- Semi-transparent backgrounds with `rgba()`
- Subtle borders and shadows
- Smooth transitions and animations

#### 3. Calculator Logic (`static/js/calculator.js`)
JavaScript module handling:
- User input capture
- API communication
- Real-time updates
- Chart rendering

#### 4. Chart Visualization (`static/js/charts.js`)
Manages chart creation and updates:
- Pie chart for bill/tip breakdown
- Bar chart for per-person amounts

### API Interface Specification

#### Calculate Bill Endpoint

**Endpoint**: `POST /api-us-west-2/prod/ai/data`

**Request Body**:
```json
{
  "bill_amount": 100.00,
  "tip_percentage": 15,
  "split_count": 4
}
```

**Success Response** (200 OK):
```json
{
  "success": true,
  "data": {
    "bill_amount": 100.00,
    "tip_percentage": 15,
    "tip_amount": 15.00,
    "total_amount": 115.00,
    "split_count": 4,
    "per_person_amount": 28.75,
    "breakdown": {
      "bill_per_person": 25.00,
      "tip_per_person": 3.75
    }
  }
}
```

**Error Response** (400 Bad Request):
```json
{
  "success": false,
  "error": "Invalid input: bill_amount must be a positive number"
}
```

## Data Models

### CalculationRequest
Input data structure for calculation requests.

```python
{
    "bill_amount": float,      # Must be > 0
    "tip_percentage": float,   # Must be 0-100
    "split_count": int         # Must be >= 1
}
```

### CalculationResponse
Output data structure for successful calculations.

```python
{
    "success": bool,
    "data": {
        "bill_amount": float,
        "tip_percentage": float,
        "tip_amount": float,           # Rounded to 2 decimals
        "total_amount": float,         # Rounded to 2 decimals
        "split_count": int,
        "per_person_amount": float,    # Rounded to 2 decimals
        "breakdown": {
            "bill_per_person": float,  # Rounded to 2 decimals
            "tip_per_person": float    # Rounded to 2 decimals
        }
    }
}
```

### ErrorResponse
Output data structure for validation errors.

```python
{
    "success": bool,           # Always false
    "error": str              # Human-readable error message
}
```

### ChartData
Frontend data structure for chart rendering.

```javascript
{
    pieChart: {
        labels: ["Bill Amount", "Tip Amount"],
        values: [100.00, 15.00],
        colors: ["#4A90E2", "#50C878"]
    },
    barChart: {
        labels: ["Person 1", "Person 2", "Person 3", "Person 4"],
        values: [28.75, 28.75, 28.75, 28.75],
        color: "#9B59B6"
    }
}
```


## Correctness Properties

*A property is a characteristic or behavior that should hold true across all valid executions of a system—essentially, a formal statement about what the system should do. Properties serve as the bridge between human-readable specifications and machine-verifiable correctness guarantees.*

### Property 1: Invalid bill amounts are rejected
*For any* non-numeric or negative bill amount input, the validation function should reject the input and return an error.
**Validates: Requirements 1.2**

### Property 2: Tip calculation formula
*For any* valid bill amount and tip percentage, the calculated tip amount should equal bill_amount × (tip_percentage / 100).
**Validates: Requirements 1.3**

### Property 3: Tip amount rounding
*For any* calculated tip amount, the displayed value should be rounded to exactly two decimal places.
**Validates: Requirements 1.4**

### Property 4: Total amount formula
*For any* valid bill amount and tip amount, the total amount should equal bill_amount + tip_amount.
**Validates: Requirements 1.5**

### Property 5: Custom tip percentage validation
*For any* custom tip percentage input, the validation should accept values between 0 and 100 (inclusive) and reject all others.
**Validates: Requirements 2.3**

### Property 6: Split count validation
*For any* split count input, the validation should accept positive integers only and reject zero, negative numbers, and non-integers.
**Validates: Requirements 3.1**

### Property 7: Per person calculation formula
*For any* valid total amount and split count, the per person amount should equal total_amount / split_count.
**Validates: Requirements 3.3**

### Property 8: Per person amount rounding
*For any* calculated per person amount, the displayed value should be rounded to exactly two decimal places.
**Validates: Requirements 3.4**

### Property 9: Bill amount change triggers recalculation
*For any* change to the bill amount with valid tip percentage and split count, all dependent values (tip amount, total amount, per person amount) should be recalculated.
**Validates: Requirements 4.1**

### Property 10: Tip percentage change triggers recalculation
*For any* change to the tip percentage with valid bill amount and split count, all dependent values (tip amount, total amount, per person amount) should be recalculated.
**Validates: Requirements 4.2**

### Property 11: Split count change triggers recalculation
*For any* change to the split count with valid bill amount and tip percentage, the per person amount should be recalculated.
**Validates: Requirements 4.3**

### Property 12: Numerical stability across operations
*For any* sequence of valid input changes, the final calculated values should match direct calculation from the final inputs without accumulated rounding errors.
**Validates: Requirements 4.5**

### Property 13: Currency formatting
*For any* monetary value displayed, the format should include appropriate currency symbol and exactly two decimal places.
**Validates: Requirements 6.5**

### Property 14: Bar chart data generation
*For any* valid split count greater than 1, the bar chart data should contain exactly split_count entries, each with the per person amount.
**Validates: Requirements 7.2**

### Property 15: Chart updates on split count change
*For any* change to split count, the chart data structures should be regenerated to reflect the new distribution.
**Validates: Requirements 7.3**

### Property 16: API calculation correctness
*For any* valid POST request to /api-us-west-2/prod/ai/data with bill_amount, tip_percentage, and split_count, the response should contain correctly calculated tip_amount, total_amount, and per_person_amount.
**Validates: Requirements 8.3**

### Property 17: API error handling
*For any* invalid POST request to /api-us-west-2/prod/ai/data, the server should return HTTP 400 status with a descriptive error message.
**Validates: Requirements 8.4**

### Property 18: API JSON response format
*For any* request to /api-us-west-2/prod/ai/data, the response should be valid JSON with the specified structure (success, data/error fields).
**Validates: Requirements 8.5**

## Error Handling

### Input Validation Errors

1. **Invalid Bill Amount**
   - Non-numeric input: Return error "Bill amount must be a valid number"
   - Negative value: Return error "Bill amount must be positive"
   - Zero value: Accept (edge case for testing)

2. **Invalid Tip Percentage**
   - Non-numeric input: Return error "Tip percentage must be a valid number"
   - Out of range (< 0 or > 100): Return error "Tip percentage must be between 0 and 100"

3. **Invalid Split Count**
   - Non-integer input: Return error "Split count must be a whole number"
   - Zero or negative: Return error "Split count must be at least 1"

### API Error Responses

All API errors should follow this format:
```json
{
    "success": false,
    "error": "<descriptive error message>"
}
```

HTTP status codes:
- 400 Bad Request: Invalid input data
- 405 Method Not Allowed: Non-POST requests to calculation endpoint
- 500 Internal Server Error: Unexpected server errors

### Frontend Error Display

- Display validation errors inline near the relevant input field
- Use red text or border to indicate error state
- Clear errors when user corrects the input
- Prevent form submission when validation errors exist

## Testing Strategy

### Unit Testing

Unit tests will verify specific examples and edge cases:

**Backend Tests** (using pytest):
- Test calculation functions with known input/output pairs
- Test validation functions with specific valid and invalid inputs
- Test API endpoint responses for specific requests
- Test error handling for specific error conditions
- Test JSON serialization/deserialization

**Frontend Tests** (using Jest or similar):
- Test UI initialization with default values
- Test button click handlers
- Test form reset functionality
- Test chart initialization with specific data
- Test API call formatting

### Property-Based Testing

Property-based tests will verify universal properties across many randomly generated inputs:

**Testing Library**: Use `hypothesis` for Python backend tests

**Configuration**: Each property test should run a minimum of 100 iterations

**Test Tagging**: Each property-based test must include a comment with this format:
```python
# Feature: tip-bill-calculator, Property X: <property description>
```

**Properties to Test**:
1. Tip calculation formula (Property 2)
2. Total amount formula (Property 4)
3. Per person calculation formula (Property 7)
4. Input validation properties (Properties 1, 5, 6)
5. Rounding properties (Properties 3, 8)
6. API correctness (Properties 16, 17, 18)
7. Numerical stability (Property 12)

**Example Property Test Structure**:
```python
from hypothesis import given, strategies as st

# Feature: tip-bill-calculator, Property 2: Tip calculation formula
@given(
    bill_amount=st.floats(min_value=0.01, max_value=10000),
    tip_percentage=st.floats(min_value=0, max_value=100)
)
def test_tip_calculation_formula(bill_amount, tip_percentage):
    result = calculate_tip(bill_amount, tip_percentage)
    expected = bill_amount * (tip_percentage / 100)
    assert abs(result - expected) < 0.01  # Allow for rounding
```

### Integration Testing

Integration tests will verify the complete flow:
- Frontend → API → Calculation → Response → UI Update
- Test with realistic user scenarios
- Verify chart rendering with calculated data
- Test error propagation from backend to frontend

### Manual Testing Checklist

- Verify glassmorphism effects render correctly across browsers
- Test responsive layout on various screen sizes
- Verify chart animations and interactions
- Test keyboard navigation and accessibility
- Verify mobile numeric keyboard appears on mobile devices

## Deployment Considerations

### Development Environment Setup

1. Create Python virtual environment:
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Run development server:
   ```bash
   python app.py
   ```

### Required Dependencies (requirements.txt)

```
Flask==3.0.0
Flask-CORS==4.0.0
pytest==7.4.3
hypothesis==6.92.0
```

### Environment Variables

- `FLASK_ENV`: Set to 'development' for debug mode
- `FLASK_PORT`: Port number (default: 8000)

### Production Considerations

- Use a production WSGI server (gunicorn or waitress) instead of Flask development server
- Enable CORS only for trusted frontend domains
- Add request rate limiting to prevent abuse
- Implement logging for debugging and monitoring
- Consider adding request/response compression
- Add security headers (CSP, X-Frame-Options, etc.)

### Browser Compatibility

- Modern browsers with CSS backdrop-filter support (Chrome 76+, Safari 9+, Firefox 103+)
- Fallback styling for browsers without glassmorphism support
- Polyfills for older JavaScript features if needed

## Performance Considerations

- All calculations should complete in < 10ms
- API response time should be < 50ms for calculation requests
- Chart rendering should complete in < 100ms
- Use debouncing for real-time input updates (300ms delay)
- Minimize DOM manipulations during updates
- Cache chart instances to avoid recreation

## Security Considerations

- Validate all inputs on both frontend and backend
- Sanitize user inputs to prevent XSS attacks
- Use CORS to restrict API access to trusted origins
- Implement rate limiting to prevent DoS attacks
- No sensitive data storage (stateless application)
- Use HTTPS in production
- Set appropriate security headers
