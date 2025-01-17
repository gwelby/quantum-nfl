// NFL Quantum Clock
export class NFLQuantumClock {
    constructor(canvasId) {
        console.log('Initializing NFL Quantum Clock...', canvasId);
        
        // Get canvas element
        this.canvas = document.getElementById(canvasId);
        if (!this.canvas) {
            console.error('NFL Quantum Clock: Canvas element not found:', canvasId);
            throw new Error(`Canvas element not found: ${canvasId}`);
        }
        
        // Initialize canvas context
        this.ctx = this.canvas.getContext('2d');
        if (!this.ctx) {
            console.error('NFL Quantum Clock: Unable to get canvas context');
            throw new Error('Unable to get canvas context');
        }
        
        // Set up dimensions
        this.size = Math.min(window.innerWidth, window.innerHeight) * 0.8;
        this.canvas.width = this.size;
        this.canvas.height = this.size;
        this.radius = this.size * 0.4;
        this.center = { x: this.size / 2, y: this.size / 2 };

        // Game state
        this.gameTime = 900; // 15:00 minutes
        this.quarter = 1;
        this.momentum = 0;
        this.quantumPhase = 0;
        this.harmonyPhase = 0;
        this.isHurryUp = false;
        this.currentMode = 'regulation';

        // Animation state
        this.isAnimating = true;
        this.lastFrameTime = performance.now();

        // Start animation loop
        console.log('Starting animation loop...');
        this.animate();
        
        // Add resize handler
        window.addEventListener('resize', () => this.handleResize());
        
        console.log('NFL Quantum Clock initialized successfully');
    }

    handleResize() {
        this.size = Math.min(window.innerWidth, window.innerHeight) * 0.8;
        this.canvas.width = this.size;
        this.canvas.height = this.size;
        this.radius = this.size * 0.4;
        this.center = { x: this.size / 2, y: this.size / 2 };
    }

    animate() {
        const time = performance.now() * 0.001;
        
        // Clear canvas
        this.ctx.fillStyle = 'rgba(13, 14, 31, 0.1)';
        this.ctx.fillRect(0, 0, this.canvas.width, this.canvas.height);
        
        // Draw orbital rings
        this.ctx.strokeStyle = '#6D28D9';
        this.ctx.lineWidth = 2;
        
        // Multiple orbiting rings
        for (let i = 0; i < 3; i++) {
            const radius = 80 + Math.sin(time * (1 + i * 0.2)) * 10;
            const rotation = time * (0.5 + i * 0.3);
            
            this.ctx.beginPath();
            this.ctx.arc(
                this.canvas.width / 2 + Math.cos(rotation) * 5,
                this.canvas.height / 2 + Math.sin(rotation) * 5,
                radius,
                0,
                Math.PI * 2
            );
            this.ctx.stroke();
            
            // Add quantum particles
            for (let j = 0; j < 5; j++) {
                const particleAngle = rotation + (Math.PI * 2 * j) / 5;
                const x = this.canvas.width / 2 + Math.cos(particleAngle) * radius;
                const y = this.canvas.height / 2 + Math.sin(particleAngle) * radius;
                
                const glow = this.ctx.createRadialGradient(x, y, 0, x, y, 10);
                glow.addColorStop(0, 'rgba(139, 92, 246, 0.8)');
                glow.addColorStop(1, 'rgba(139, 92, 246, 0)');
                
                this.ctx.fillStyle = glow;
                this.ctx.beginPath();
                this.ctx.arc(x, y, 10, 0, Math.PI * 2);
                this.ctx.fill();
            }
        }
        
        // Draw time
        const now = new Date();
        const timeString = now.toLocaleTimeString();
        
        this.ctx.font = 'bold 24px Arial';
        this.ctx.fillStyle = '#8B5CF6';
        this.ctx.textAlign = 'center';
        this.ctx.textBaseline = 'middle';
        this.ctx.fillText(timeString, this.canvas.width / 2, this.canvas.height / 2);
        
        // Add pulsing glow around time
        const pulseSize = 40 + Math.sin(time * 3) * 10;
        const timeGlow = this.ctx.createRadialGradient(
            this.canvas.width / 2,
            this.canvas.height / 2,
            pulseSize - 20,
            this.canvas.width / 2,
            this.canvas.height / 2,
            pulseSize
        );
        timeGlow.addColorStop(0, 'rgba(139, 92, 246, 0.2)');
        timeGlow.addColorStop(1, 'rgba(139, 92, 246, 0)');
        
        this.ctx.fillStyle = timeGlow;
        this.ctx.beginPath();
        this.ctx.arc(this.canvas.width / 2, this.canvas.height / 2, pulseSize, 0, Math.PI * 2);
        this.ctx.fill();
        
        requestAnimationFrame(() => this.animate());
    }
}
