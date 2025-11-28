# Requirements Document

## Introduction

The Tip & Bill Split Calculator is a web application that enables users to calculate appropriate tip amounts for restaurant bills and split the total cost among multiple people. The system provides an intuitive interface for entering bill amounts, selecting tip percentages, and dividing costs fairly among diners.

## Glossary

- **Calculator**: The Tip & Bill Split Calculator application
- **User**: A person using the Calculator to compute tips and split bills
- **Bill Amount**: The pre-tip total cost of a restaurant meal or service
- **Tip Percentage**: The percentage of the Bill Amount to be added as gratuity
- **Tip Amount**: The calculated gratuity value based on Bill Amount and Tip Percentage
- **Total Amount**: The sum of Bill Amount and Tip Amount
- **Split Count**: The number of people among whom the Total Amount will be divided
- **Per Person Amount**: The Total Amount divided by the Split Count
- **API Endpoint**: A REST endpoint exposed at /api-us-west-2/prod/ai/data for calculation operations
- **Flask Server**: The Python Flask web server running on port 8000
- **Glassmorphism UI**: A modern UI design style featuring frosted glass effects with transparency and blur

## Requirements

### Requirement 1

**User Story:** As a user, I want to enter a bill amount and calculate the tip, so that I can determine how much gratuity to leave.

#### Acceptance Criteria

1. WHEN a user enters a valid Bill Amount THEN the Calculator SHALL accept and display the value
2. WHEN a user enters a non-numeric or negative Bill Amount THEN the Calculator SHALL reject the input and display an error message
3. WHEN a user selects a Tip Percentage THEN the Calculator SHALL compute the Tip Amount as the product of Bill Amount and Tip Percentage
4. WHEN the Tip Amount is calculated THEN the Calculator SHALL display the Tip Amount rounded to two decimal places
5. WHEN the Tip Amount is calculated THEN the Calculator SHALL compute and display the Total Amount as the sum of Bill Amount and Tip Amount

### Requirement 2

**User Story:** As a user, I want to choose from common tip percentages or enter a custom percentage, so that I can tip according to my preference or local customs.

#### Acceptance Criteria

1. WHEN the Calculator loads THEN the Calculator SHALL display preset tip options of 10%, 15%, 18%, 20%, and 25%
2. WHEN a user selects a preset tip option THEN the Calculator SHALL apply that Tip Percentage to the Bill Amount
3. WHEN a user enters a custom Tip Percentage THEN the Calculator SHALL validate it is between 0% and 100%
4. WHEN a user enters a custom Tip Percentage outside the valid range THEN the Calculator SHALL reject the input and display an error message
5. WHEN a user switches between preset and custom tip options THEN the Calculator SHALL recalculate the Tip Amount immediately

### Requirement 3

**User Story:** As a user, I want to split the total bill among multiple people, so that each person knows their fair share.

#### Acceptance Criteria

1. WHEN a user enters a Split Count THEN the Calculator SHALL validate it is a positive integer
2. WHEN a user enters an invalid Split Count THEN the Calculator SHALL reject the input and display an error message
3. WHEN a valid Split Count is entered THEN the Calculator SHALL compute the Per Person Amount by dividing Total Amount by Split Count
4. WHEN the Per Person Amount is calculated THEN the Calculator SHALL display the value rounded to two decimal places
5. WHEN the Split Count is 1 THEN the Calculator SHALL display the Per Person Amount equal to the Total Amount

### Requirement 4

**User Story:** As a user, I want to see all calculations update in real-time, so that I can quickly adjust values and see the results.

#### Acceptance Criteria

1. WHEN a user modifies the Bill Amount THEN the Calculator SHALL recalculate and update Tip Amount, Total Amount, and Per Person Amount immediately
2. WHEN a user modifies the Tip Percentage THEN the Calculator SHALL recalculate and update Tip Amount, Total Amount, and Per Person Amount immediately
3. WHEN a user modifies the Split Count THEN the Calculator SHALL recalculate and update the Per Person Amount immediately
4. WHEN any calculation updates THEN the Calculator SHALL complete the update within 100 milliseconds
5. WHEN multiple values are changed in sequence THEN the Calculator SHALL maintain calculation accuracy without rounding errors accumulating

### Requirement 5

**User Story:** As a user, I want to reset all values to start a new calculation, so that I can quickly calculate for a different bill.

#### Acceptance Criteria

1. WHEN a user clicks the reset button THEN the Calculator SHALL clear the Bill Amount field
2. WHEN a user clicks the reset button THEN the Calculator SHALL reset the Tip Percentage to a default value of 15%
3. WHEN a user clicks the reset button THEN the Calculator SHALL reset the Split Count to 1
4. WHEN a user clicks the reset button THEN the Calculator SHALL clear all calculated values
5. WHEN the reset is complete THEN the Calculator SHALL focus the Bill Amount input field for immediate data entry

### Requirement 6

**User Story:** As a user, I want the interface to be clear and easy to use on both desktop and mobile devices, so that I can calculate bills wherever I am.

#### Acceptance Criteria

1. WHEN the Calculator is displayed on a mobile device THEN the Calculator SHALL render all controls and results in a single-column layout
2. WHEN the Calculator is displayed on a desktop device THEN the Calculator SHALL render controls and results in an optimized multi-column layout
3. WHEN input fields receive focus on mobile devices THEN the Calculator SHALL display the appropriate numeric keyboard
4. WHEN the Calculator is rendered THEN the Calculator SHALL use sufficient font sizes and touch targets for mobile usability
5. WHEN the Calculator displays monetary values THEN the Calculator SHALL format them with appropriate currency symbols and decimal places

### Requirement 7

**User Story:** As a user, I want to see visual representations of the bill breakdown, so that I can quickly understand the cost distribution.

#### Acceptance Criteria

1. WHEN a bill calculation is complete THEN the Calculator SHALL display a pie chart showing the proportion of Bill Amount versus Tip Amount
2. WHEN multiple people are splitting the bill THEN the Calculator SHALL display a bar chart showing the Per Person Amount for each person
3. WHEN the Split Count changes THEN the Calculator SHALL update all charts immediately to reflect the new distribution
4. WHEN charts are displayed THEN the Calculator SHALL use clear labels and color coding to distinguish between different amounts
5. WHEN a user hovers over chart elements THEN the Calculator SHALL display detailed tooltips with exact values

### Requirement 8

**User Story:** As a developer, I want the application to use a Flask backend with RESTful API endpoints, so that calculations are handled server-side and the architecture is maintainable.

#### Acceptance Criteria

1. WHEN the Flask Server starts THEN the Flask Server SHALL listen on port 8000
2. WHEN a calculation request is received THEN the Flask Server SHALL process it via the API Endpoint at /api-us-west-2/prod/ai/data
3. WHEN the API Endpoint receives a POST request with Bill Amount, Tip Percentage, and Split Count THEN the Flask Server SHALL return calculated Tip Amount, Total Amount, and Per Person Amount
4. WHEN the API Endpoint receives invalid input THEN the Flask Server SHALL return an HTTP 400 error with a descriptive error message
5. WHEN the Flask Server processes requests THEN the Flask Server SHALL return responses in JSON format

### Requirement 9

**User Story:** As a user, I want a modern glassmorphism interface, so that the application is visually appealing and enjoyable to use.

#### Acceptance Criteria

1. WHEN the Calculator interface loads THEN the Calculator SHALL apply glassmorphism styling with frosted glass effects
2. WHEN UI elements are rendered THEN the Calculator SHALL use semi-transparent backgrounds with backdrop blur
3. WHEN the Calculator displays cards or panels THEN the Calculator SHALL apply subtle borders and shadows to create depth
4. WHEN the user interacts with buttons or inputs THEN the Calculator SHALL provide smooth transitions and hover effects
5. WHEN the glassmorphism effects are applied THEN the Calculator SHALL maintain readability and contrast for all text elements

### Requirement 10

**User Story:** As a developer, I want the application to run in a Python virtual environment, so that dependencies are isolated and the project is reproducible.

#### Acceptance Criteria

1. WHEN the development environment is set up THEN the Calculator SHALL use a Python virtual environment for all dependencies
2. WHEN dependencies are installed THEN the Flask Server SHALL install packages only within the virtual environment
3. WHEN the Flask Server starts THEN the Flask Server SHALL use the Python interpreter from the virtual environment
4. WHEN the project is deployed THEN the Calculator SHALL include a requirements.txt file listing all dependencies
5. WHEN a new developer sets up the project THEN the Calculator SHALL provide clear instructions for creating and activating the virtual environment
