// NFL Quantum Teams Website JavaScript

// Mobile menu toggle
document.addEventListener('DOMContentLoaded', () => {
    const menuButton = document.getElementById('menuButton');
    const navMenu = document.querySelector('.nav-menu');

    if (menuButton) {
        menuButton.addEventListener('click', () => {
            navMenu.classList.toggle('active');
        });
    }
});

// Dark mode toggle
function toggleDarkMode() {
    document.body.classList.toggle('dark');
    localStorage.setItem('darkMode', document.body.classList.contains('dark'));
}

// Check for saved dark mode preference
if (localStorage.getItem('darkMode') === 'true') {
    document.body.classList.add('dark');
}

// Live predictions update
class PredictionUpdater {
    constructor() {
        this.predictions = {};
        this.updateInterval = 60000; // Update every minute
    }

    async fetchPredictions() {
        try {
            // In real implementation, this would fetch from your API
            const response = await fetch('/api/predictions');
            const data = await response.json();
            this.updatePredictionCards(data);
        } catch (error) {
            console.error('Error fetching predictions:', error);
        }
    }

    updatePredictionCards(predictions) {
        const container = document.getElementById('predictions');
        if (!container) return;

        predictions.forEach(prediction => {
            const card = this.createPredictionCard(prediction);
            container.appendChild(card);
        });
    }

    createPredictionCard(prediction) {
        const card = document.createElement('div');
        card.className = 'prediction-card bg-white dark:bg-gray-800 p-6 rounded-lg shadow-lg';
        card.innerHTML = `
            <div class="flex justify-between items-center mb-4">
                <span class="text-green-600 font-bold">${prediction.homeTeam}</span>
                <span class="text-gray-600 dark:text-gray-400">vs</span>
                <span class="text-blue-600 font-bold">${prediction.awayTeam}</span>
            </div>
            <div class="text-center">
                <div class="text-2xl font-bold mb-2">${prediction.winProbability}%</div>
                <p class="text-gray-600 dark:text-gray-400">Win Probability</p>
            </div>
        `;
        return card;
    }

    start() {
        this.fetchPredictions();
        setInterval(() => this.fetchPredictions(), this.updateInterval);
    }
}

// Initialize prediction updater
const predictionUpdater = new PredictionUpdater();
predictionUpdater.start();

// Smooth scrolling for navigation links
document.querySelectorAll('a[href^="#"]').forEach(anchor => {
    anchor.addEventListener('click', function (e) {
        e.preventDefault();
        const target = document.querySelector(this.getAttribute('href'));
        if (target) {
            target.scrollIntoView({
                behavior: 'smooth',
                block: 'start'
            });
        }
    });
});

// Intersection Observer for animations
const observerOptions = {
    threshold: 0.1,
    rootMargin: '0px'
};

const observer = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
        if (entry.isIntersecting) {
            entry.target.classList.add('animate-fade-in');
            observer.unobserve(entry.target);
        }
    });
}, observerOptions);

// Observe all sections for animation
document.querySelectorAll('section').forEach(section => {
    observer.observe(section);
});

// Handle form submissions
document.querySelectorAll('form').forEach(form => {
    form.addEventListener('submit', async (e) => {
        e.preventDefault();
        const formData = new FormData(form);
        try {
            const response = await fetch(form.action, {
                method: 'POST',
                body: formData
            });
            const data = await response.json();
            // Handle response
            console.log('Form submitted:', data);
        } catch (error) {
            console.error('Error submitting form:', error);
        }
    });
});
