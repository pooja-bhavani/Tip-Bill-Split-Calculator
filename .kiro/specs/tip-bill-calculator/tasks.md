# Implementation Plan

- [x] 1. Set up project structure and Python virtual environment
  - Create project directory structure (app/, static/, templates/, tests/)
  - Initialize Python virtual environment
  - Create requirements.txt with Flask, Flask-CORS, pytest, hypothesis
  - Create .gitignore for Python projects
  - _Requirements: 10.1, 10.4_

- [x] 2. Implement core calculation service
  - Create services/calculator.py with CalculatorService class
  - Implement calculate_tip() method with formula: bill_amount × (tip_percentage / 100)
  - Implement calculate_total() method with formula: bill_amount + tip_amount
  - Implement calculate_per_person() method with formula: total_amount / split_count
  - Implement rounding to 2 decimal places for all monetary values
  - _Requirements: 1.3, 1.4, 1.5, 3.3, 3.4_

- [ ]* 2.1 Write property test for tip calculation formula
  - **Property 2: Tip calculation formula**
  - **Validates: Requirements 1.3**

- [ ]* 2.2 Write property test for total amount formula
  - **Property 4: Total amount formula**
  - **Validates: Requirements 1.5**

- [ ]* 2.3 Write property test for per person calculation
  - **Property 7: Per person calculation formula**
  - **Validates: Requirements 3.3**

- [ ]* 2.4 Write property test for tip amount rounding
  - **Property 3: Tip amount rounding**
  - **Validates: Requirements 1.4**

- [ ]* 2.5 Write property test for per person rounding
  - **Property 8: Per person amount rounding**
  - **Validates: Requirements 3.4**

- [x] 3. Implement input validation service
  - Create services/validator.py with validation functions
  - Implement validate_bill_amount() to reject non-numeric and negative values
  - Implement validate_tip_percentage() to ensure 0-100 range
  - Implement validate_split_count() to ensure positive integers only
  - Return descriptive error messages for each validation failure
  - _Requirements: 1.2, 2.3, 2.4, 3.1, 3.2_

- [ ]* 3.1 Write property test for bill amount validation
  - **Property 1: Invalid bill amounts are rejected**
  - **Validates: Requirements 1.2**

- [ ]* 3.2 Write property test for tip percentage validation
  - **Property 5: Custom tip percentage validation**
  - **Validates: Requirements 2.3**

- [ ]* 3.3 Write property test for split count validation
  - **Property 6: Split count validation**
  - **Validates: Requirements 3.1**

- [x] 4. Create Flask application and API endpoint
  - Create app.py with Flask app initialization
  - Configure Flask to run on port 8000
  - Enable Flask-CORS for frontend access
  - Create routes/api.py with POST endpoint at /api-us-west-2/prod/ai/data
  - Implement request parsing for bill_amount, tip_percentage, split_count
  - Integrate CalculatorService and validation
  - Return JSON responses with calculated values or error messages
  - _Requirements: 8.1, 8.2, 8.3, 8.4, 8.5_

- [ ]* 4.1 Write property test for API calculation correctness
  - **Property 16: API calculation correctness**
  - **Validates: Requirements 8.3**

- [ ]* 4.2 Write property test for API error handling
  - **Property 17: API error handling**
  - **Validates: Requirements 8.4**

- [ ]* 4.3 Write property test for API JSON response format
  - **Property 18: API JSON response format**
  - **Validates: Requirements 8.5**

- [x] 5. Checkpoint - Ensure all tests pass
  - Ensure all tests pass, ask the user if questions arise.

- [x] 6. Create HTML structure with glassmorphism UI
  - Create templates/index.html with semantic HTML structure
  - Add input fields for bill amount, tip percentage, and split count
  - Add preset tip percentage buttons (10%, 15%, 18%, 20%, 25%)
  - Add custom tip percentage input field
  - Add reset button
  - Add display areas for calculated values (tip, total, per person)
  - Add containers for pie chart and bar chart
  - Set input type="number" for numeric fields to trigger mobile keyboards
  - _Requirements: 1.1, 2.1, 5.1, 5.2, 5.3, 6.3_

- [x] 7. Implement glassmorphism CSS styling
  - Create static/css/styles.css with glassmorphism effects
  - Apply backdrop-filter: blur() for frosted glass effect
  - Use semi-transparent backgrounds with rgba() colors
  - Add subtle borders and box-shadows for depth
  - Implement smooth transitions for hover and focus states
  - Create responsive layout (single-column mobile, multi-column desktop)
  - Style buttons, inputs, and result displays with glass effect
  - Ensure sufficient contrast for text readability
  - _Requirements: 9.1, 9.2, 9.3, 9.4, 6.1, 6.2_

- [x] 8. Implement frontend calculator logic
  - Create static/js/calculator.js module
  - Implement input event listeners for bill amount, tip percentage, split count
  - Implement click handlers for preset tip buttons
  - Implement API call function to POST to /api-us-west-2/prod/ai/data
  - Parse JSON responses and update UI with calculated values
  - Display error messages for validation failures
  - Implement debouncing (300ms) for real-time input updates
  - Format monetary values with currency symbol and 2 decimal places
  - _Requirements: 4.1, 4.2, 4.3, 6.5_

- [ ]* 8.1 Write property test for recalculation on bill amount change
  - **Property 9: Bill amount change triggers recalculation**
  - **Validates: Requirements 4.1**

- [ ]* 8.2 Write property test for recalculation on tip percentage change
  - **Property 10: Tip percentage change triggers recalculation**
  - **Validates: Requirements 4.2**

- [ ]* 8.3 Write property test for recalculation on split count change
  - **Property 11: Split count change triggers recalculation**
  - **Validates: Requirements 4.3**

- [ ]* 8.4 Write property test for numerical stability
  - **Property 12: Numerical stability across operations**
  - **Validates: Requirements 4.5**

- [ ]* 8.5 Write property test for currency formatting
  - **Property 13: Currency formatting**
  - **Validates: Requirements 6.5**

- [x] 9. Implement reset functionality
  - Add click handler for reset button
  - Clear bill amount input field
  - Reset tip percentage to 15% default
  - Reset split count to 1
  - Clear all calculated value displays
  - Clear charts
  - Set focus to bill amount input field
  - _Requirements: 5.1, 5.2, 5.3, 5.4, 5.5_

- [x] 10. Integrate Chart.js for data visualization
  - Add Chart.js library via CDN in index.html
  - Create static/js/charts.js module
  - Implement createPieChart() function for bill/tip breakdown
  - Implement createBarChart() function for per-person amounts
  - Configure chart colors, labels, and styling
  - Add tooltip configuration for hover interactions
  - _Requirements: 7.1, 7.5_

- [x] 11. Implement chart update logic
  - Create updatePieChart() function to refresh pie chart data
  - Create updateBarChart() function to refresh bar chart with split count entries
  - Call chart update functions after each calculation
  - Destroy and recreate charts on data changes to ensure accuracy
  - _Requirements: 7.2, 7.3_

- [ ]* 11.1 Write property test for bar chart data generation
  - **Property 14: Bar chart data generation**
  - **Validates: Requirements 7.2**

- [ ]* 11.2 Write property test for chart updates on split count change
  - **Property 15: Chart updates on split count change**
  - **Validates: Requirements 7.3**

- [x] 12. Add error handling and user feedback
  - Implement frontend validation before API calls
  - Display inline error messages near invalid inputs
  - Add error styling (red borders/text) for invalid fields
  - Clear errors when user corrects input
  - Handle API errors gracefully with user-friendly messages
  - Add loading states during API calls
  - _Requirements: 1.2, 2.4, 3.2_

- [x] 13. Final checkpoint - Ensure all tests pass
  - Ensure all tests pass, ask the user if questions arise.

- [x] 14. Create project documentation
  - Create README.md with project overview
  - Document virtual environment setup instructions
  - Document how to install dependencies
  - Document how to run the development server
  - Add API endpoint documentation
  - Add screenshots or GIFs of the UI
  - _Requirements: 10.5_
