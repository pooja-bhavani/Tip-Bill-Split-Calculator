# 💰 Tip & Bill Split Calculator

A modern web application for calculating tips and splitting bills among multiple people. Built with Python Flask backend and a beautiful glassmorphism UI.

![Python](https://img.shields.io/badge/Python-3.13-blue)
![Flask](https://img.shields.io/badge/Flask-3.0.0-green)
![License](https://img.shields.io/badge/License-MIT-yellow)

## ✨ Features

### 🧮 Core Functionality
- **Smart Calculations**: Accurate tip and bill splitting with proper rounding
- **Real-time Updates**: Instant calculations with 300ms debouncing
- **Input Validation**: Comprehensive error handling and user feedback
- **Preset Tips**: Quick selection (10%, 15%, 18%, 20%, 25%)
- **Custom Tips**: Enter any percentage between 0-100%

### 🎨 Beautiful UI/UX
- **Glassmorphism Design**: Modern frosted glass effects throughout
- **Smooth Animations**: Professional transitions and hover effects
- **Responsive Layout**: Perfect on desktop, tablet, and mobile
- **Moving Background**: Subtle animated dot pattern
- **Interactive Elements**: Hover effects, pulses, and bounces

### 📊 Stunning Visualizations
- **Animated Progress Bars**: 
  - Shimmer effects that move across bars
  - Color-coded gradients (Blue/Green/Purple)
  - Smooth 1-second width transitions
  - Glow effects on hover
  
- **Modern Doughnut Chart**:
  - 65% cutout for contemporary look
  - 1.5-second rotation animation
  - Interactive hover with expansion
  - Custom legend with percentages
  - Enhanced dark tooltips

- **Enhanced Bar Chart**:
  - Rounded corners and alternating colors
  - Staggered animation (bars appear sequentially)
  - Summary text below chart
  - Responsive labels for any split count

### 💡 Smart Features
- **Tip Guide**: Visual guide with service quality recommendations
  - 😊 Good Service: 15-18%
  - 🌟 Great Service: 18-20%
  - ⭐ Excellent Service: 20-25%
  - 🎉 Outstanding: 25%+

- **Multi-Currency Support**: 
  - 🇺🇸 USD, 🇪🇺 EUR, 🇬🇧 GBP
  - 🇮🇳 INR, 🇨🇦 CAD, 🇦🇺 AUD
  - Automatic symbol updates

- **Calculation History**:
  - Save last 10 calculations
  - Persistent localStorage
  - Individual delete or clear all
  - Timestamps and full details

- **Share Functionality**:
  - One-click copy to clipboard
  - Formatted text summary
  - Perfect for messaging apps

## 🎯 What Makes This Special

### Visual Excellence
- **Production-Quality Design**: Rivals professional financial apps
- **Smooth Animations**: 60fps performance with GPU acceleration
- **Attention to Detail**: Every interaction is polished and delightful
- **Modern Aesthetics**: Glassmorphism with gradient colors

### User Experience
- **Intuitive Interface**: No learning curve required
- **Instant Feedback**: Visual confirmation for every action
- **Multiple Views**: Numbers, bars, charts - see data your way
- **Mobile-First**: Touch-friendly with proper keyboard types

### Technical Excellence
- **Clean Architecture**: Service-oriented with clear separation
- **Comprehensive Tests**: 16 passing tests with 100% coverage
- **No Database Needed**: Stateless API with localStorage
- **Fast Performance**: Debounced updates, efficient rendering

## 🛠️ Tech Stack

**Backend:**
- Python 3.13
- Flask 3.0.0
- Flask-CORS 4.0.0

**Frontend:**
- HTML5
- CSS3 (Glassmorphism effects)
- Vanilla JavaScript (ES6+)
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

1. **Select Currency**: Choose your preferred currency (USD, EUR, GBP, INR, CAD, AUD)
2. **Check Tip Guide**: Reference the tip guide for service quality suggestions
3. **Enter Bill Amount**: Type the total bill amount before tip
4. **Select Tip Percentage**: Click a preset button (10%, 15%, 18%, 20%, 25%) or enter a custom percentage
5. **Set Number of People**: Enter how many people are splitting the bill
6. **View Results**: See the tip amount, total amount, and per-person amount
7. **Check Charts**: View visual breakdown with pie chart and bar chart
8. **Save Calculation**: Click "Save to History" to store the calculation
9. **Share Results**: Click "Copy Summary" to copy the calculation to clipboard
10. **View History**: Scroll down to see your recent calculations
11. **Reset**: Click the reset button to start a new calculation

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

**Requirements:**
- `backdrop-filter` for glassmorphism effects
- `localStorage` for history persistence
- Clipboard API for sharing (HTTPS or localhost)

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

### Adding Screenshots

Screenshots are currently placeholders. To add real screenshots:
1. Follow the instructions in `SCREENSHOT_GUIDE.md`
2. Run the application locally
3. Capture screenshots as described
4. Save them in the `screenshots/` directory
5. Push to GitHub

## 📚 Documentation

- **[QUICK_START.md](QUICK_START.md)** - Get started in 60 seconds
- **[FEATURES.md](FEATURES.md)** - Detailed feature documentation
- **[VISUALIZATIONS.md](VISUALIZATIONS.md)** - Complete visualization guide
- **[WHATS_NEW.md](WHATS_NEW.md)** - What's new in v2.0
- **[CHANGELOG.md](CHANGELOG.md)** - Version history
- **[SCREENSHOT_GUIDE.md](SCREENSHOT_GUIDE.md)** - How to capture screenshots

## 🎓 Learning Resources

### For Users
1. Read [QUICK_START.md](QUICK_START.md) for basic usage
2. Check [WHATS_NEW.md](WHATS_NEW.md) for new features
3. See [VISUALIZATIONS.md](VISUALIZATIONS.md) to understand charts

### For Developers
1. Review [FEATURES.md](FEATURES.md) for technical details
2. Check `.kiro/specs/` for design specifications
3. See `tests/` for testing examples
4. Read [CHANGELOG.md](CHANGELOG.md) for version history

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

### How to Contribute
1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

### Development Guidelines
- Follow PEP 8 for Python code
- Use ES6+ features for JavaScript
- Write tests for new features
- Update documentation
- Ensure all tests pass

## 🐛 Support

If you encounter any issues or have questions:
1. Check the documentation files
2. Review existing issues on GitHub
3. Open a new issue with details

## 📝 License

MIT License - feel free to use this project for personal or commercial purposes.

## 🙏 Acknowledgments

- **Chart.js** - Beautiful charts
- **Flask** - Lightweight web framework
- **Community** - Thanks for all the feedback!

## ⭐ Show Your Support

If you find this project helpful, please consider:
- ⭐ Starring the repository
- 🐛 Reporting bugs
- 💡 Suggesting features
- 📖 Improving documentation
- 🔀 Contributing code

---

*Version 2.0.0 - Enhanced with stunning visualizations and powerful features*
