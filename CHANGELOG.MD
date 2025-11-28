# Changelog

## Version 2.0.0 - Enhanced Features (2024)

### 🎉 Major Additions

#### 💡 Tip Guide
- Added visual tip guide with service quality recommendations
- Four tiers: Good (15-18%), Great (18-20%), Excellent (20-25%), Outstanding (25%+)
- Interactive cards with emoji indicators
- Always visible at top of page for quick reference

#### 💱 Multi-Currency Support
- Added support for 6 major currencies:
  - USD ($) - US Dollar
  - EUR (€) - Euro
  - GBP (£) - British Pound
  - INR (₹) - Indian Rupee
  - CAD ($) - Canadian Dollar
  - AUD ($) - Australian Dollar
- Currency selector with flag emojis
- Automatic symbol updates throughout interface
- Currency preserved in calculation history

#### 📜 Calculation History
- Save up to 10 recent calculations
- Persistent storage using localStorage
- Each entry shows:
  - Timestamp
  - Bill amount and currency
  - Tip percentage and amount
  - Total amount
  - Split count and per-person amount
- Individual delete functionality
- Clear all history option
- Scrollable list with custom styling

#### 📋 Share Functionality
- One-click copy to clipboard
- Formatted text summary including:
  - All calculation details
  - Easy-to-read layout
  - App attribution
- Visual feedback on successful copy
- Perfect for sharing via text, email, or messaging apps

#### 💾 Save to History
- Manual save button for important calculations
- Adds to top of history list
- Confirmation feedback
- Automatic limit management (keeps last 10)

### 🎨 UI/UX Improvements

- Enhanced glassmorphism effects on new sections
- Smooth hover animations on all interactive elements
- Responsive grid layouts for new features
- Custom scrollbar styling for history list
- Improved mobile layout with adaptive grids
- Better visual hierarchy with section organization

### 🔧 Technical Improvements

- Enhanced state management for currency and calculations
- localStorage integration for data persistence
- Clipboard API integration for sharing
- Dynamic DOM rendering for history
- Improved code organization and modularity
- Better error handling and user feedback

### 📱 Mobile Enhancements

- Tip guide adapts to 2-column layout on mobile
- Action buttons stack vertically on small screens
- History details optimize for single column
- Maintained touch-friendly button sizes
- Improved scrolling experience

---

## Version 1.0.0 - Initial Release

### Core Features

- Bill amount calculation
- Tip percentage selection (preset and custom)
- Bill splitting among multiple people
- Real-time calculations with debouncing
- Input validation and error handling
- Glassmorphism UI design
- Responsive layout (desktop and mobile)
- Chart.js visualizations:
  - Pie chart for bill/tip breakdown
  - Bar chart for per-person splits
- Flask backend with REST API
- Comprehensive test suite

### Technical Stack

- Python 3.13 + Flask 3.0.0
- HTML5, CSS3, Vanilla JavaScript
- Chart.js for visualizations
- pytest + hypothesis for testing

---

## Upcoming Features (Roadmap)

### Planned for v2.1
- Dark mode toggle
- Custom tip guide ranges
- Export history as CSV

### Planned for v3.0
- Uneven bill splitting
- Tax calculator
- Group member names
- QR code generation for payment apps

---

## Migration Notes

### From v1.0 to v2.0

**No breaking changes!** All v1.0 features remain fully functional.

**New Dependencies:** None - all new features use native browser APIs

**Data Storage:** New localStorage usage for calculation history (automatic, no setup required)

**Browser Requirements:** 
- Clipboard API requires HTTPS in production (or localhost for development)
- localStorage widely supported across all modern browsers

---

## Bug Fixes

### v2.0.0
- Fixed currency formatting consistency
- Improved mobile responsive layout
- Enhanced error message display
- Better handling of edge cases in calculations

---

## Performance

- History limited to 10 items for optimal performance
- Efficient DOM updates using batch rendering
- No additional external dependencies
- Minimal impact on page load time

---

## Acknowledgments

Thanks to all users who requested these features! Your feedback helps make this app better.

---

**Full Documentation:** See FEATURES.md for detailed feature descriptions
**Setup Guide:** See README.md for installation and usage instructions
**Screenshot Guide:** See SCREENSHOT_GUIDE.md for capturing app screenshots
