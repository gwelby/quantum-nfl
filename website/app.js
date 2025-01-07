// Quantum NFL Application Core
document.addEventListener('DOMContentLoaded', () => {
    initializeApp();
    setupEventListeners();
    loadPredictions();
});

// Initialize application
function initializeApp() {
    // Setup mobile menu
    const menuButton = document.getElementById('menuButton');
    const navMenu = document.querySelector('.nav-menu');
    
    menuButton.addEventListener('click', () => {
        navMenu.classList.toggle('hidden');
    });

    // Close menu on click outside
    document.addEventListener('click', (e) => {
        if (!menuButton.contains(e.target) && !navMenu.contains(e.target)) {
            navMenu.classList.add('hidden');
        }
    });

    // Initialize quantum effects
    initQuantumEffects();
}

// Setup event listeners
function setupEventListeners() {
    // Smooth scroll for navigation links
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

    // Quantum card hover effects
    document.querySelectorAll('.quantum-card').forEach(card => {
        card.addEventListener('mousemove', handleQuantumHover);
        card.addEventListener('mouseleave', resetQuantumEffect);
    });
}

// Load predictions
async function loadPredictions() {
    const predictionsGrid = document.getElementById('predictions-grid');
    if (!predictionsGrid) return;

    // Sample predictions data (replace with actual API call)
    const predictions = [
        {
            teams: ['Kansas City Chiefs', 'Buffalo Bills'],
            probability: 0.78,
            quantumState: 'Superposition',
            prediction: 'High-scoring offensive battle'
        },
        {
            teams: ['San Francisco 49ers', 'Philadelphia Eagles'],
            probability: 0.65,
            quantumState: 'Entangled',
            prediction: 'Defensive showcase'
        },
        {
            teams: ['Dallas Cowboys', 'Green Bay Packers'],
            probability: 0.72,
            quantumState: 'Coherent',
            prediction: 'Close game with multiple lead changes'
        }
    ];

    predictions.forEach(pred => {
        const predictionCard = createPredictionCard(pred);
        predictionsGrid.appendChild(predictionCard);
    });
}

// Create prediction card
function createPredictionCard(prediction) {
    const card = document.createElement('div');
    card.className = 'quantum-card p-6';
    
    card.innerHTML = `
        <div class="mb-4">
            <h3 class="text-xl font-bold mb-2">${prediction.teams.join(' vs ')}</h3>
            <div class="text-sm text-gray-400">Quantum State: ${prediction.quantumState}</div>
        </div>
        <div class="mb-4">
            <div class="h-2 bg-gray-700 rounded-full">
                <div class="h-2 bg-purple-600 rounded-full" style="width: ${prediction.probability * 100}%"></div>
            </div>
            <div class="text-sm mt-1">Probability: ${(prediction.probability * 100).toFixed(1)}%</div>
        </div>
        <p class="text-gray-300">${prediction.prediction}</p>
    `;

    return card;
}

// Handle quantum hover effect
function handleQuantumHover(e) {
    const card = e.currentTarget;
    const rect = card.getBoundingClientRect();
    const x = e.clientX - rect.left;
    const y = e.clientY - rect.top;

    const centerX = rect.width / 2;
    const centerY = rect.height / 2;

    const angleX = (x - centerX) / centerX * 10;
    const angleY = (y - centerY) / centerY * 10;

    card.style.transform = `perspective(1000px) rotateX(${-angleY}deg) rotateY(${angleX}deg) scale3d(1.02, 1.02, 1.02)`;
}

// Reset quantum effect
function resetQuantumEffect(e) {
    const card = e.currentTarget;
    card.style.transform = 'perspective(1000px) rotateX(0) rotateY(0) scale3d(1, 1, 1)';
}

// Initialize quantum effects
function initQuantumEffects() {
    // Add quantum particle effect to hero section
    const hero = document.getElementById('hero');
    if (hero) {
        createQuantumParticles(hero);
    }
}

// Create quantum particles
function createQuantumParticles(container) {
    const canvas = document.createElement('canvas');
    canvas.className = 'absolute top-0 left-0 w-full h-full -z-10';
    container.style.position = 'relative';
    container.appendChild(canvas);

    const ctx = canvas.getContext('2d');
    let particles = [];

    function resizeCanvas() {
        canvas.width = container.offsetWidth;
        canvas.height = container.offsetHeight;
    }

    resizeCanvas();
    window.addEventListener('resize', resizeCanvas);

    // Create particles
    for (let i = 0; i < 50; i++) {
        particles.push({
            x: Math.random() * canvas.width,
            y: Math.random() * canvas.height,
            size: Math.random() * 3 + 1,
            speedX: Math.random() * 2 - 1,
            speedY: Math.random() * 2 - 1,
            life: Math.random() * 0.5 + 0.5
        });
    }

    // Animate particles
    function animate() {
        ctx.clearRect(0, 0, canvas.width, canvas.height);

        particles.forEach((particle, index) => {
            particle.x += particle.speedX;
            particle.y += particle.speedY;
            particle.life -= 0.001;

            // Reset particle if it's dead or out of bounds
            if (particle.life <= 0 || 
                particle.x < 0 || particle.x > canvas.width || 
                particle.y < 0 || particle.y > canvas.height) {
                particles[index] = {
                    x: Math.random() * canvas.width,
                    y: Math.random() * canvas.height,
                    size: Math.random() * 3 + 1,
                    speedX: Math.random() * 2 - 1,
                    speedY: Math.random() * 2 - 1,
                    life: 1
                };
            }

            // Draw particle
            ctx.beginPath();
            ctx.arc(particle.x, particle.y, particle.size, 0, Math.PI * 2);
            ctx.fillStyle = `rgba(139, 92, 246, ${particle.life})`;
            ctx.fill();
        });

        requestAnimationFrame(animate);
    }

    animate();
}

// Service Worker Registration
if ('serviceWorker' in navigator) {
    window.addEventListener('load', () => {
        navigator.serviceWorker.register('/service-worker.js')
            .then(registration => {
                console.log('ServiceWorker registration successful');
            })
            .catch(err => {
                console.log('ServiceWorker registration failed: ', err);
            });
    });
}
