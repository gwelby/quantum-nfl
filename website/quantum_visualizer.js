// Quantum NFL Visualizer
class QuantumVisualizer {
    constructor(canvasId) {
        this.canvas = document.getElementById(canvasId);
        this.ctx = this.canvas.getContext('2d');
        this.particles = [];
        this.entanglementLines = [];
        this.setupCanvas();
        this.initializeParticles();
        this.animate();
    }

    setupCanvas() {
        this.canvas.width = window.innerWidth;
        this.canvas.height = window.innerHeight;
        
        window.addEventListener('resize', () => {
            this.canvas.width = window.innerWidth;
            this.canvas.height = window.innerHeight;
        });
    }

    initializeParticles() {
        const numParticles = 32;
        for (let i = 0; i < numParticles; i++) {
            this.particles.push({
                x: Math.random() * this.canvas.width,
                y: Math.random() * this.canvas.height,
                radius: Math.random() * 3 + 1,
                speed: Math.random() * 2 + 1,
                direction: Math.random() * Math.PI * 2,
                quantumState: Math.random(),
                entangled: false,
                color: this.getQuantumColor(Math.random())
            });
        }
    }

    animate() {
        this.ctx.fillStyle = 'rgba(0, 0, 0, 0.05)';
        this.ctx.fillRect(0, 0, this.canvas.width, this.canvas.height);

        this.updateParticles();
        this.drawEntanglementLines();
        this.drawParticles();
        this.drawQuantumWaves();

        requestAnimationFrame(() => this.animate());
    }

    updateParticles() {
        this.particles.forEach(particle => {
            // Update position with quantum wave function
            particle.x += Math.cos(particle.direction) * particle.speed;
            particle.y += Math.sin(particle.direction) * particle.speed;

            // Quantum tunneling effect at boundaries
            if (particle.x < 0) particle.x = this.canvas.width;
            if (particle.x > this.canvas.width) particle.x = 0;
            if (particle.y < 0) particle.y = this.canvas.height;
            if (particle.y > this.canvas.height) particle.y = 0;

            // Update quantum state
            particle.quantumState = this.updateQuantumState(particle.quantumState);
            particle.color = this.getQuantumColor(particle.quantumState);

            // Random direction changes based on quantum probability
            if (Math.random() < 0.02) {
                particle.direction += (Math.random() - 0.5) * Math.PI / 2;
            }
        });

        // Update entanglement lines
        this.updateEntanglementLines();
    }

    drawParticles() {
        this.particles.forEach(particle => {
            this.ctx.beginPath();
            this.ctx.arc(particle.x, particle.y, particle.radius, 0, Math.PI * 2);
            this.ctx.fillStyle = particle.color;
            this.ctx.fill();

            // Add quantum glow effect
            const gradient = this.ctx.createRadialGradient(
                particle.x, particle.y, 0,
                particle.x, particle.y, particle.radius * 3
            );
            gradient.addColorStop(0, particle.color);
            gradient.addColorStop(1, 'rgba(0, 0, 0, 0)');
            
            this.ctx.beginPath();
            this.ctx.arc(particle.x, particle.y, particle.radius * 3, 0, Math.PI * 2);
            this.ctx.fillStyle = gradient;
            this.ctx.fill();
        });
    }

    drawEntanglementLines() {
        this.ctx.strokeStyle = 'rgba(138, 43, 226, 0.2)';
        this.ctx.lineWidth = 1;

        this.entanglementLines.forEach(line => {
            const gradient = this.ctx.createLinearGradient(
                line.start.x, line.start.y,
                line.end.x, line.end.y
            );
            gradient.addColorStop(0, this.getQuantumColor(line.start.quantumState));
            gradient.addColorStop(1, this.getQuantumColor(line.end.quantumState));

            this.ctx.beginPath();
            this.ctx.moveTo(line.start.x, line.start.y);
            this.ctx.lineTo(line.end.x, line.end.y);
            this.ctx.strokeStyle = gradient;
            this.ctx.stroke();
        });
    }

    drawQuantumWaves() {
        this.ctx.strokeStyle = 'rgba(138, 43, 226, 0.1)';
        this.ctx.lineWidth = 2;

        this.particles.forEach(particle => {
            // Draw quantum probability wave
            this.ctx.beginPath();
            for (let i = 0; i < Math.PI * 2; i += 0.1) {
                const radius = particle.radius * 5;
                const x = particle.x + Math.cos(i) * radius * 
                         (1 + 0.3 * Math.sin(particle.quantumState * 10));
                const y = particle.y + Math.sin(i) * radius * 
                         (1 + 0.3 * Math.cos(particle.quantumState * 10));

                if (i === 0) {
                    this.ctx.moveTo(x, y);
                } else {
                    this.ctx.lineTo(x, y);
                }
            }
            this.ctx.closePath();
            this.ctx.stroke();
        });
    }

    updateEntanglementLines() {
        this.entanglementLines = [];
        
        this.particles.forEach((p1, i) => {
            this.particles.slice(i + 1).forEach(p2 => {
                const distance = Math.hypot(p2.x - p1.x, p2.y - p1.y);
                if (distance < 100) {
                    this.entanglementLines.push({
                        start: p1,
                        end: p2,
                        strength: 1 - distance / 100
                    });
                }
            });
        });
    }

    updateQuantumState(state) {
        // Quantum wave function evolution
        return (state + 0.01) % 1;
    }

    getQuantumColor(state) {
        // Color spectrum based on quantum state
        const hue = state * 360;
        return `hsla(${hue}, 70%, 50%, 0.8)`;
    }

    // Public methods for external interaction
    addQuantumParticle(x, y) {
        this.particles.push({
            x: x || Math.random() * this.canvas.width,
            y: y || Math.random() * this.canvas.height,
            radius: Math.random() * 3 + 1,
            speed: Math.random() * 2 + 1,
            direction: Math.random() * Math.PI * 2,
            quantumState: Math.random(),
            entangled: false,
            color: this.getQuantumColor(Math.random())
        });
    }

    createEntanglement(index1, index2) {
        if (index1 < this.particles.length && index2 < this.particles.length) {
            this.particles[index1].entangled = true;
            this.particles[index2].entangled = true;
            this.particles[index2].quantumState = this.particles[index1].quantumState;
        }
    }

    collapseWaveFunction(index) {
        if (index < this.particles.length) {
            this.particles[index].quantumState = Math.random();
            this.particles[index].color = this.getQuantumColor(this.particles[index].quantumState);
        }
    }
}

// Export for use in main application
export default QuantumVisualizer;
