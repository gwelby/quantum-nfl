// Quantum NFL Application

// Constants
const QUANTUM_STATES = {
    SUPERPOSITION: 'superposition',
    ENTANGLED: 'entangled',
    COLLAPSED: 'collapsed'
};

// DOM Elements
const menuButton = document.getElementById('menuButton');
const navMenu = document.querySelector('.nav-menu');
const predictionsGrid = document.getElementById('predictions-grid');

// Theme handling
const prefersDark = window.matchMedia('(prefers-color-scheme: dark)');
const updateTheme = (e) => {
    document.body.classList.toggle('dark', e.matches);
};
prefersDark.addListener(updateTheme);
updateTheme(prefersDark);

// Mobile menu toggle
menuButton?.addEventListener('click', () => {
    navMenu?.classList.toggle('active');
});

// Quantum effects
const applyQuantumEffect = (element) => {
    element.classList.add('quantum-animate');
    setTimeout(() => {
        element.classList.remove('quantum-animate');
    }, 2000);
};

// Intersection Observer for animations
const observeElements = () => {
    const observer = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.classList.add('quantum-animate');
                observer.unobserve(entry.target);
            }
        });
    }, {
        threshold: 0.1
    });

    document.querySelectorAll('.quantum-card').forEach(card => {
        observer.observe(card);
    });
};

// Live predictions
const fetchPredictions = async () => {
    try {
        // Simulate quantum computation delay
        await new Promise(resolve => setTimeout(resolve, 2000));
        
        const predictions = [
            {
                teams: ['GB', 'CHI'],
                probability: 85,
                quantum_state: QUANTUM_STATES.SUPERPOSITION
            },
            {
                teams: ['SF', 'SEA'],
                probability: 65,
                quantum_state: QUANTUM_STATES.ENTANGLED
            },
            {
                teams: ['KC', 'LV'],
                probability: 75,
                quantum_state: QUANTUM_STATES.COLLAPSED
            }
        ];

        updatePredictions(predictions);
    } catch (error) {
        console.error('Error fetching predictions:', error);
        predictionsGrid.innerHTML = `
            <div class="quantum-card p-6 text-center">
                <p class="text-red-500">Error loading predictions. Please try again later.</p>
            </div>
        `;
    }
};

// Update predictions UI
const updatePredictions = (predictions) => {
    if (!predictionsGrid) return;

    predictionsGrid.innerHTML = predictions.map(pred => `
        <div class="quantum-card p-6 ${pred.quantum_state}">
            <div class="flex justify-between items-center mb-4">
                <span class="text-2xl font-bold">${pred.teams[0]}</span>
                <span class="text-gray-600 dark:text-gray-400">vs</span>
                <span class="text-2xl font-bold">${pred.teams[1]}</span>
            </div>
            <div class="text-center">
                <div class="text-3xl font-bold mb-2">${pred.probability}%</div>
                <p class="text-gray-600 dark:text-gray-300">Win Probability</p>
                <div class="mt-2 text-sm text-purple-600 dark:text-purple-400">
                    Quantum State: ${pred.quantum_state}
                </div>
            </div>
        </div>
    `).join('');
};

// Smooth scroll for navigation
document.querySelectorAll('a[href^="#"]').forEach(anchor => {
    anchor.addEventListener('click', function (e) {
        e.preventDefault();
        const target = document.querySelector(this.getAttribute('href'));
        if (target) {
            target.scrollIntoView({
                behavior: 'smooth',
                block: 'start'
            });
            // Close mobile menu if open
            navMenu?.classList.remove('active');
        }
    });
});

// Initialize
document.addEventListener('DOMContentLoaded', () => {
    observeElements();
    fetchPredictions();
});

// Export for testing
if (typeof module !== 'undefined' && module.exports) {
    module.exports = {
        QUANTUM_STATES,
        applyQuantumEffect,
        updatePredictions
    };
}
