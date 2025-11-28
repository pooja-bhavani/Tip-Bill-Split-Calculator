// Calculator state
let state = {
    billAmount: 0,
    tipPercentage: 18,
    splitCount: 1,
    debounceTimer: null
};

// DOM elements
const billAmountInput = document.getElementById('billAmount');
const customTipInput = document.getElementById('customTip');
const splitCountInput = document.getElementById('splitCount');
const tipButtons = document.querySelectorAll('.tip-btn');
const resetBtn = document.getElementById('resetBtn');

// Result elements
const tipAmountEl = document.getElementById('tipAmount');
const totalAmountEl = document.getElementById('totalAmount');
const perPersonAmountEl = document.getElementById('perPersonAmount');

// Error elements
const billAmountError = document.getElementById('billAmountError');
const tipPercentageError = document.getElementById('tipPercentageError');
const splitCountError = document.getElementById('splitCountError');

// Format currency
function formatCurrency(amount) {
    return `$${amount.toFixed(2)}`;
}

// Clear all errors
function clearErrors() {
    billAmountError.textContent = '';
    tipPercentageError.textContent = '';
    splitCountError.textContent = '';
}

// Display error
function displayError(element, message) {
    element.textContent = message;
}

// Debounced calculation
function debouncedCalculate() {
    clearTimeout(state.debounceTimer);
    state.debounceTimer = setTimeout(() => {
        calculate();
    }, 300);
}

// Main calculation function
async function calculate() {
    clearErrors();

    // Get current values
    const billAmount = parseFloat(billAmountInput.value) || 0;
    const tipPercentage = state.tipPercentage;
    const splitCount = parseInt(splitCountInput.value) || 1;

    // Basic validation
    if (billAmount < 0) {
        displayError(billAmountError, 'Bill amount must be positive');
        return;
    }

    if (splitCount < 1) {
        displayError(splitCountError, 'Split count must be at least 1');
        return;
    }

    // Update state
    state.billAmount = billAmount;
    state.splitCount = splitCount;

    // Call API
    try {
        const response = await fetch('/api-us-west-2/prod/ai/data', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({
                bill_amount: billAmount,
                tip_percentage: tipPercentage,
                split_count: splitCount
            })
        });

        const data = await response.json();

        if (data.success) {
            // Update results
            tipAmountEl.textContent = formatCurrency(data.data.tip_amount);
            totalAmountEl.textContent = formatCurrency(data.data.total_amount);
            perPersonAmountEl.textContent = formatCurrency(data.data.per_person_amount);

            // Update charts
            if (window.updateCharts) {
                window.updateCharts(data.data);
            }
        } else {
            // Display API error
            displayError(billAmountError, data.error);
        }
    } catch (error) {
        console.error('Calculation error:', error);
        displayError(billAmountError, 'Failed to calculate. Please try again.');
    }
}

// Handle tip button clicks
tipButtons.forEach(button => {
    button.addEventListener('click', () => {
        // Remove active class from all buttons
        tipButtons.forEach(btn => btn.classList.remove('active'));
        
        // Add active class to clicked button
        button.classList.add('active');
        
        // Clear custom tip input
        customTipInput.value = '';
        
        // Update state and calculate
        state.tipPercentage = parseFloat(button.dataset.tip);
        calculate();
    });
});

// Handle custom tip input
customTipInput.addEventListener('input', () => {
    const customTip = parseFloat(customTipInput.value);
    
    if (customTip !== null && !isNaN(customTip)) {
        // Remove active class from preset buttons
        tipButtons.forEach(btn => btn.classList.remove('active'));
        
        // Validate range
        if (customTip < 0 || customTip > 100) {
            displayError(tipPercentageError, 'Tip percentage must be between 0 and 100');
            return;
        }
        
        // Update state and calculate
        state.tipPercentage = customTip;
        debouncedCalculate();
    }
});

// Handle bill amount input
billAmountInput.addEventListener('input', () => {
    debouncedCalculate();
});

// Handle split count input
splitCountInput.addEventListener('input', () => {
    debouncedCalculate();
});

// Handle reset button
resetBtn.addEventListener('click', () => {
    // Clear inputs
    billAmountInput.value = '';
    customTipInput.value = '';
    splitCountInput.value = '1';
    
    // Reset to default tip (18%)
    tipButtons.forEach(btn => btn.classList.remove('active'));
    const defaultBtn = document.querySelector('[data-tip="18"]');
    if (defaultBtn) {
        defaultBtn.classList.add('active');
    }
    
    // Reset state
    state.billAmount = 0;
    state.tipPercentage = 18;
    state.splitCount = 1;
    
    // Clear results
    tipAmountEl.textContent = '$0.00';
    totalAmountEl.textContent = '$0.00';
    perPersonAmountEl.textContent = '$0.00';
    
    // Clear errors
    clearErrors();
    
    // Clear charts
    if (window.clearCharts) {
        window.clearCharts();
    }
    
    // Focus bill amount input
    billAmountInput.focus();
});

// Initialize on page load
document.addEventListener('DOMContentLoaded', () => {
    // Set default active button
    const defaultBtn = document.querySelector('[data-tip="18"]');
    if (defaultBtn) {
        defaultBtn.classList.add('active');
    }
    
    // Focus bill amount input
    billAmountInput.focus();
});
