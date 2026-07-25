// =====================================
// Check Theme
// =====================================

const isDark = document.body.classList.contains("dark");

const textColor = isDark ? "#f5f5f5" : "#374151";
const gridColor = isDark ? "#444" : "#e5e7eb";

// =====================================
// Expense Breakdown Chart
// =====================================

const expenseCanvas = document.getElementById("expenseChart");

if (expenseCanvas) {

    new Chart(expenseCanvas, {

        type: "doughnut",

        data: {

            labels: categoryLabels,

            datasets: [{

                data: categoryAmounts,

                backgroundColor: [

                    "#2563eb",
                    "#16a34a",
                    "#f59e0b",
                    "#ef4444",
                    "#8b5cf6",
                    "#06b6d4",
                    "#ec4899",
                    "#84cc16"

                ]

            }]

        },

        options: {

            responsive: true,

            plugins: {

                legend: {

                    position: "bottom",

                    labels: {

                        color: textColor

                    }

                }

            }

        }

    });

}

// =====================================
// Monthly Trend Chart
// =====================================

const trendCanvas = document.getElementById("trendChart");

if (trendCanvas) {

    new Chart(trendCanvas, {

        type: "line",

        data: {

            labels: trendLabels,

            datasets: [

                {

                    label: "Income",

                    data: trendIncome,

                    borderColor: "#22c55e",

                    backgroundColor: "rgba(34,197,94,0.15)",

                    fill: false,

                    tension: 0.4

                },

                {

                    label: "Expenses",

                    data: trendExpense,

                    borderColor: "#ef4444",

                    backgroundColor: "rgba(239,68,68,0.15)",

                    fill: false,

                    tension: 0.4

                }

            ]

        },

        options: {

            responsive: true,

            plugins: {

                legend: {

                    position: "bottom",

                    labels: {

                        color: textColor

                    }

                }

            },

            scales: {

                x: {

                    ticks: {

                        color: textColor

                    },

                    grid: {

                        color: gridColor

                    }

                },

                y: {

                    beginAtZero: true,

                    ticks: {

                        color: textColor

                    },

                    grid: {

                        color: gridColor

                    }

                }

            }

        }

    });

}