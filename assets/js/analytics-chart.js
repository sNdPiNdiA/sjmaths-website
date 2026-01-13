/**
 * Renders a bar chart for time spent per question.
 * @param {string} canvasId - The ID of the canvas element.
 * @param {string} storageKey - The localStorage key for time data.
 */
function renderAnalyticsChart(canvasId, storageKey) {
    const ctx = document.getElementById(canvasId);
    if (!ctx) return;

    const rawData = localStorage.getItem(storageKey);
    if (!rawData) {
        // If no data, hide the canvas container if possible or just return
        return;
    }

    const timeData = JSON.parse(rawData);

    // Sort keys based on question number (e.g., 's1_q1', 'q10')
    const sortedKeys = Object.keys(timeData).sort((a, b) => {
        const getNum = (str) => {
            const match = str.match(/q(\d+)/i);
            return match ? parseInt(match[1]) : 0;
        };
        return getNum(a) - getNum(b);
    });

    const dataValues = sortedKeys.map(k => timeData[k]);
    const labels = sortedKeys.map(k => {
        const match = k.match(/q(\d+)/i);
        return match ? `Q${match[1]}` : k;
    });

    new Chart(ctx, {
        type: 'bar',
        data: {
            labels: labels,
            datasets: [{
                label: 'Time Spent',
                data: dataValues,
                backgroundColor: 'rgba(123, 31, 162, 0.6)',
                borderColor: 'rgba(123, 31, 162, 1)',
                borderWidth: 1,
                borderRadius: 4,
                hoverBackgroundColor: 'rgba(123, 31, 162, 0.8)'
            }]
        },
        options: {
            responsive: true,
            maintainAspectRatio: false,
            scales: {
                y: {
                    beginAtZero: true,
                    title: { display: true, text: 'Seconds' },
                    grid: { color: 'rgba(0, 0, 0, 0.05)' }
                },
                x: {
                    grid: { display: false }
                }
            },
            plugins: {
                legend: { display: false },
                tooltip: {
                    callbacks: {
                        label: (ctx) => {
                            const val = ctx.parsed.y;
                            const m = Math.floor(val / 60);
                            const s = val % 60;
                            return `Time: ${m}m ${s}s`;
                        }
                    }
                }
            }
        }
    });
}