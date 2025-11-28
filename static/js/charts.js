// Chart instances
let pieChart = null;
let barChart = null;

// Chart colors
const colors = {
    bill: 'rgba(74, 144, 226, 0.8)',
    tip: 'rgba(80, 200, 120, 0.8)',
    person: 'rgba(155, 89, 182, 0.8)'
};

// Initialize pie chart
function createPieChart(billAmount, tipAmount) {
    const ctx = document.getElementById('pieChart').getContext('2d');
    
    // Destroy existing chart
    if (pieChart) {
        pieChart.destroy();
    }
    
    pieChart = new Chart(ctx, {
        type: 'pie',
        data: {
            labels: ['Bill Amount', 'Tip Amount'],
            datasets: [{
                data: [billAmount, tipAmount],
                backgroundColor: [colors.bill, colors.tip],
                borderColor: 'rgba(255, 255, 255, 0.5)',
                borderWidth: 2
            }]
        },
        options: {
            responsive: true,
            maintainAspectRatio: true,
            plugins: {
                legend: {
                    position: 'bottom',
                    labels: {
                        color: 'white',
                        font: {
                            size: 14
                        },
                        padding: 15
                    }
                },
                tooltip: {
                    callbacks: {
                        label: function(context) {
                            const label = context.label || '';
                            const value = context.parsed || 0;
                            return `${label}: $${value.toFixed(2)}`;
                        }
                    }
                }
            }
        }
    });
}

// Initialize bar chart
function createBarChart(splitCount, perPersonAmount) {
    const ctx = document.getElementById('barChart').getContext('2d');
    
    // Destroy existing chart
    if (barChart) {
        barChart.destroy();
    }
    
    // Generate labels for each person
    const labels = [];
    const data = [];
    for (let i = 1; i <= splitCount; i++) {
        labels.push(`Person ${i}`);
        data.push(perPersonAmount);
    }
    
    barChart = new Chart(ctx, {
        type: 'bar',
        data: {
            labels: labels,
            datasets: [{
                label: 'Amount per Person',
                data: data,
                backgroundColor: colors.person,
                borderColor: 'rgba(255, 255, 255, 0.5)',
                borderWidth: 2
            }]
        },
        options: {
            responsive: true,
            maintainAspectRatio: true,
            scales: {
                y: {
                    beginAtZero: true,
                    ticks: {
                        color: 'white',
                        callback: function(value) {
                            return '$' + value.toFixed(2);
                        }
                    },
                    grid: {
                        color: 'rgba(255, 255, 255, 0.1)'
                    }
                },
                x: {
                    ticks: {
                        color: 'white'
                    },
                    grid: {
                        color: 'rgba(255, 255, 255, 0.1)'
                    }
                }
            },
            plugins: {
                legend: {
                    display: false
                },
                tooltip: {
                    callbacks: {
                        label: function(context) {
                            const value = context.parsed.y || 0;
                            return `Amount: $${value.toFixed(2)}`;
                        }
                    }
                }
            }
        }
    });
}

// Update charts with new data
window.updateCharts = function(data) {
    createPieChart(data.bill_amount, data.tip_amount);
    createBarChart(data.split_count, data.per_person_amount);
};

// Clear charts
window.clearCharts = function() {
    if (pieChart) {
        pieChart.destroy();
        pieChart = null;
    }
    if (barChart) {
        barChart.destroy();
        barChart = null;
    }
};

// Initialize empty charts on page load
document.addEventListener('DOMContentLoaded', () => {
    createPieChart(0, 0);
    createBarChart(1, 0);
});
