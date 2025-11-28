# 💰 Tip & Bill Split Calculator

A modern web application for calculating tips and splitting bills among multiple people. Built with Python Flask backend and a beautiful glassmorphism UI.

![Python](https://img.shields.io/badge/Python-3.13-blue)
![Flask](https://img.shields.io/badge/Flask-3.0.0-green)
![License](https://img.shields.io/badge/License-MIT-yellow)

## Features

- 🧮 **Smart Calculations**: Accurate tip and bill splitting calculations
- 🎨 **Glassmorphism UI**: Modern frosted glass design with smooth animations
- 📊 **Visual Charts**: Pie chart for bill breakdown and bar chart for per-person splits
- 📱 **Responsive Design**: Works seamlessly on desktop and mobile devices
- ⚡ **Real-time Updates**: Instant calculations with 300ms debouncing
- ✅ **Input Validation**: Comprehensive error handling and user feedback
- 🎯 **Preset Tips**: Quick selection of common tip percentages (10%, 15%, 18%, 20%, 25%)
- 🔧 **Custom Tips**: Enter any custom tip percentage between 0-100%

## Tech Stack

**Backend:**
- Python 3.13
- Flask 3.0.0
- Flask-CORS 4.0.0

**Frontend:**
- HTML5
- CSS3 (Glassmorphism effects)
- Vanilla JavaScript
- Chart.js 4.4.0

**Testing:**
- pytest 7.4.3
- hypothesis 6.92.0

## Installation

### Prerequisites

- Python 3.13 or higher
- pip (Python package manager)

### Setup Instructions

1. **Clone the repository** (or navigate to the project directory)

2. **Create a virtual environment:**
   ```bash
   python3 -m venv venv
   ```

3. **Activate the virtual environment:**
   
   On macOS/Linux:
   ```bash
   source venv/bin/activate
   ```
   
   On Windows:
   ```bash
   venv\Scripts\activate
   ```

4. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

## Running the Application

1. **Start the Flask development server:**
   ```bash
   python app.py
   ```

2. **Open your browser and navigate to:**
   ```
   http://localhost:8000
   ```

The application will be running on port 8000.

## API Documentation

### Calculate Bill Endpoint

**Endpoint:** `POST /api-us-west-2/prod/ai/data`

**Request Body:**
```json
{
  "bill_amount": 100.00,
  "tip_percentage": 15,
  "split_count": 4
}
```

**Success Response (200 OK):**
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

**Error Response (400 Bad Request):**
```json
{
  "success": false,
  "error": "Bill amount must be positive"
}
```

## Running Tests

Run all tests:
```bash
pytest tests/ -v
```

Run specific test file:
```bash
pytest tests/test_calculator.py -v
```

Run with coverage:
```bash
pytest tests/ --cov=app --cov-report=html
```

## Project Structure

```
.
├── app/
│   ├── __init__.py
│   ├── routes/
│   │   ├── __init__.py
│   │   └── api.py              # API endpoints
│   └── services/
│       ├── __init__.py
│       ├── calculator.py       # Calculation logic
│       └── validator.py        # Input validation
├── static/
│   ├── css/
│   │   └── styles.css          # Glassmorphism styling
│   └── js/
│       ├── calculator.js       # Frontend logic
│       └── charts.js           # Chart.js integration
├── templates/
│   └── index.html              # Main HTML page
├── tests/
│   ├── __init__.py
│   ├── test_api.py             # API tests
│   ├── test_calculator.py      # Calculator tests
│   └── test_validator.py       # Validator tests
├── app.py                      # Flask application entry point
├── requirements.txt            # Python dependencies
└── README.md                   # This file
```

## Usage

1. **Enter Bill Amount**: Type the total bill amount before tip
2. **Select Tip Percentage**: Click a preset button (10%, 15%, 18%, 20%, 25%) or enter a custom percentage
3. **Set Number of People**: Enter how many people are splitting the bill
4. **View Results**: See the tip amount, total amount, and per-person amount
5. **Check Charts**: View visual breakdown with pie chart and bar chart
6. **Reset**: Click the reset button to start a new calculation

## Features in Detail

### Glassmorphism UI
- Frosted glass effect using `backdrop-filter: blur()`
- Semi-transparent backgrounds with subtle borders
- Smooth transitions and hover effects
- Beautiful gradient background

### Real-time Calculations
- Automatic recalculation on input changes
- 300ms debouncing to prevent excessive API calls
- Instant visual feedback

### Input Validation
- Bill amount must be positive
- Tip percentage must be between 0-100%
- Split count must be at least 1
- Clear error messages for invalid inputs

### Responsive Design
- Multi-column layout on desktop
- Single-column layout on mobile
- Touch-friendly buttons (48px minimum)
- Numeric keyboard on mobile devices

## Browser Compatibility

- Chrome 76+ (recommended)
- Safari 9+
- Firefox 103+
- Edge 79+

Note: Glassmorphism effects require browsers with `backdrop-filter` support.

## Development

### Adding New Features

1. Update the requirements in `.kiro/specs/tip-bill-calculator/requirements.md`
2. Update the design in `.kiro/specs/tip-bill-calculator/design.md`
3. Add tasks to `.kiro/specs/tip-bill-calculator/tasks.md`
4. Implement the feature
5. Write tests
6. Update documentation

### Code Style

- Python: Follow PEP 8 guidelines
- JavaScript: Use ES6+ features
- CSS: Use BEM naming convention where applicable

## License

MIT License - feel free to use this project for personal or commercial purposes.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## Support

If you encounter any issues or have questions, please open an issue on the repository.

---

Made with ❤️ using Flask and Chart.js
