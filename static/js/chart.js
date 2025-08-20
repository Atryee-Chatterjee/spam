document.addEventListener("DOMContentLoaded", function () {
    if (typeof spamRisk !== "undefined") {
        const ctx = document.getElementById('spamChart').getContext('2d');
        new Chart(ctx, {
            type: 'doughnut',
            data: {
                labels: ['Spam Risk (%)', 'Safe (%)'],
                datasets: [{
                    data: [spamRisk, 100 - spamRisk],
                    backgroundColor: ['#ff073a', '#00ff87'], // Bright Neon Colors
                    borderColor: '#ffffff',
                    borderWidth: 2,
                    hoverOffset: 12
                }]
            },
            options: {
                plugins: {
                    legend: {
                        position: 'bottom',
                        labels: {
                            color: '#fff',
                            font: { size: 14, weight: 'bold' }
                        }
                    },
                    title: {
                        display: true,
                        text: `Spam Risk: ${spamRisk}%`,
                        color: '#fff',
                        font: { size: 18, weight: 'bold' }
                    }
                },
                responsive: true,
                maintainAspectRatio: false
            }
        });
    }
});
