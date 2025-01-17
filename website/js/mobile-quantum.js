// Mobile-Optimized Quantum Football Experience

export class MobileQuantumManager {
    constructor() {
        this.sensors = {
            accelerometer: null,
            gyroscope: null,
            orientation: null
        };
        this.quantumState = {
            timeDilation: 1.0,
            fieldStrength: 0,
            momentum: 0
        };
        this.batteryStatus = {
            level: 1.0,
            charging: false
        };
        this.performanceMode = 'high';
        this.initializeSensors();
        this.checkBattery();
    }

    async initializeSensors() {
        // Initialize device sensors with error handling
        try {
            if ('Accelerometer' in window) {
                this.sensors.accelerometer = new Accelerometer({ frequency: 30 });
                this.sensors.accelerometer.addEventListener('reading', () => {
                    this.updateQuantumState('acceleration');
                });
                this.sensors.accelerometer.start();
            }

            if ('Gyroscope' in window) {
                this.sensors.gyroscope = new Gyroscope({ frequency: 30 });
                this.sensors.gyroscope.addEventListener('reading', () => {
                    this.updateQuantumState('rotation');
                });
                this.sensors.gyroscope.start();
            }

            // Device orientation for quantum field visualization
            window.addEventListener('deviceorientation', (event) => {
                this.sensors.orientation = {
                    alpha: event.alpha,
                    beta: event.beta,
                    gamma: event.gamma
                };
                this.updateQuantumState('orientation');
            });
        } catch (error) {
            console.log('Sensor initialization failed:', error);
            this.fallbackToBasicMode();
        }
    }

    async checkBattery() {
        if ('getBattery' in navigator) {
            const battery = await navigator.getBattery();
            this.batteryStatus.level = battery.level;
            this.batteryStatus.charging = battery.charging;
            this.adjustPerformance();

            // Monitor battery changes
            battery.addEventListener('levelchange', () => {
                this.batteryStatus.level = battery.level;
                this.adjustPerformance();
            });
        }
    }

    adjustPerformance() {
        // Optimize performance based on battery
        if (this.batteryStatus.charging || this.batteryStatus.level > 0.2) {
            this.performanceMode = 'high';
            this.updateFrameRate(60);
        } else {
            this.performanceMode = 'low';
            this.updateFrameRate(30);
        }
    }

    updateFrameRate(fps) {
        this.frameInterval = 1000 / fps;
        // Update animation loops
        if (this.animationFrame) {
            cancelAnimationFrame(this.animationFrame);
        }
        this.startAnimation();
    }

    updateQuantumState(sensorType) {
        switch (sensorType) {
            case 'acceleration':
                this.updateTimeDilation();
                break;
            case 'rotation':
                this.updateFieldStrength();
                break;
            case 'orientation':
                this.updateMomentum();
                break;
        }
        this.render();
    }

    updateTimeDilation() {
        if (!this.sensors.accelerometer) return;
        
        // Calculate time dilation based on device movement
        const acceleration = Math.sqrt(
            Math.pow(this.sensors.accelerometer.x, 2) +
            Math.pow(this.sensors.accelerometer.y, 2) +
            Math.pow(this.sensors.accelerometer.z, 2)
        );

        // Apply quantum mechanics-inspired formula
        this.quantumState.timeDilation = 1 / Math.sqrt(1 - Math.min(acceleration / 100, 0.99));
    }

    updateFieldStrength() {
        if (!this.sensors.gyroscope) return;

        // Calculate quantum field strength from rotation
        const rotation = Math.sqrt(
            Math.pow(this.sensors.gyroscope.x, 2) +
            Math.pow(this.sensors.gyroscope.y, 2) +
            Math.pow(this.sensors.gyroscope.z, 2)
        );

        this.quantumState.fieldStrength = Math.min(rotation / 360, 1);
    }

    updateMomentum() {
        if (!this.sensors.orientation) return;

        // Calculate quantum momentum from device orientation
        const orientation = Math.abs(
            (this.sensors.orientation.beta || 0) / 180 +
            (this.sensors.orientation.gamma || 0) / 90
        );

        this.quantumState.momentum = Math.min(orientation, 1);
    }

    render() {
        // Throttle rendering based on performance mode
        if (!this.lastRender || Date.now() - this.lastRender >= this.frameInterval) {
            this.lastRender = Date.now();
            
            // Update quantum visualizations
            this.updateQuantumClock();
            this.updateQuantumField();
            this.updateParticleEffects();
        }
    }

    updateQuantumClock() {
        const clock = document.getElementById('quantumClock');
        if (!clock) return;

        const dilatedTime = this.getGameTime() * this.quantumState.timeDilation;
        clock.innerHTML = this.formatTime(dilatedTime);
    }

    updateQuantumField() {
        const field = document.getElementById('quantumField');
        if (!field) return;

        // Apply quantum field effects based on device motion
        const intensity = this.quantumState.fieldStrength * 100;
        field.style.filter = `hue-rotate(${intensity}deg) brightness(${1 + intensity/100})`;
    }

    updateParticleEffects() {
        // Optimize particle effects for mobile
        const particleCount = this.performanceMode === 'high' ? 100 : 50;
        this.renderParticles(particleCount);
    }

    renderParticles(count) {
        const container = document.getElementById('particleContainer');
        if (!container) return;

        // Clear existing particles
        container.innerHTML = '';

        // Add optimized particles
        for (let i = 0; i < count; i++) {
            const particle = document.createElement('div');
            particle.className = 'quantum-particle';
            particle.style.transform = this.calculateParticlePosition(i);
            container.appendChild(particle);
        }
    }

    calculateParticlePosition(index) {
        const angle = (index / count) * Math.PI * 2;
        const radius = 50 * this.quantumState.fieldStrength;
        const x = Math.cos(angle) * radius;
        const y = Math.sin(angle) * radius;
        return `translate(${x}px, ${y}px)`;
    }

    getGameTime() {
        // Get current game time in seconds
        return 900; // 15:00 minutes
    }

    formatTime(seconds) {
        const minutes = Math.floor(seconds / 60);
        const remainingSeconds = Math.floor(seconds % 60);
        return `${minutes}:${remainingSeconds.toString().padStart(2, '0')}`;
    }

    fallbackToBasicMode() {
        // Simplified version for devices without sensors
        this.performanceMode = 'basic';
        this.frameInterval = 1000 / 30;
        
        // Use simple time-based effects
        setInterval(() => {
            this.quantumState.timeDilation = 1 + Math.sin(Date.now() / 1000) * 0.1;
            this.render();
        }, this.frameInterval);
    }

    startAnimation() {
        const animate = () => {
            this.render();
            this.animationFrame = requestAnimationFrame(animate);
        };
        animate();
    }
}

// Initialize when DOM is loaded
document.addEventListener('DOMContentLoaded', () => {
    const mobileQuantum = new MobileQuantumManager();
});
