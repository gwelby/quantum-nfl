// NFL Quantum Celebrations and Sound Effects

class QuantumCelebrations {
    constructor() {
        this.audioContext = new (window.AudioContext || window.webkitAudioContext)();
        this.animations = {};
        this.sounds = {};
        this.teamThemes = {};
        this.crowdChants = {};
        this.initialize();
    }

    async initialize() {
        await this.loadSoundEffects();
        await this.loadTeamThemes();
        await this.loadCrowdChants();
        this.setupAnimations();
    }

    // Celebration Animations
    setupAnimations() {
        this.animations = {
            touchdown: {
                name: "Quantum Touchdown",
                icon: "🏈",
                particles: 100,
                duration: 3000,
                colors: ["#FFD700", "#FF6B6B", "#4ECDC4"],
                pattern: "spiral"
            },
            fieldGoal: {
                name: "Field Goal Flash",
                icon: "🎯",
                particles: 50,
                duration: 2000,
                colors: ["#A8E6CF", "#DCEDC1", "#FFD3B6"],
                pattern: "burst"
            },
            interception: {
                name: "Quantum Interception",
                icon: "⚡",
                particles: 75,
                duration: 2500,
                colors: ["#FF6B6B", "#4ECDC4", "#45B7D1"],
                pattern: "wave"
            },
            sack: {
                name: "Quantum Sack",
                icon: "💥",
                particles: 60,
                duration: 1800,
                colors: ["#FF6B6B", "#C7F464", "#4ECDC4"],
                pattern: "explosion"
            }
        };
    }

    // Sound Effects
    async loadSoundEffects() {
        const effects = {
            touchdown: "sounds/touchdown.mp3",
            fieldGoal: "sounds/field_goal.mp3",
            interception: "sounds/interception.mp3",
            sack: "sounds/sack.mp3",
            crowdRoar: "sounds/crowd_roar.mp3",
            quantumPulse: "sounds/quantum_pulse.mp3",
            momentumShift: "sounds/momentum_shift.mp3",
            victoryChant: "sounds/victory_chant.mp3"
        };

        for (const [name, path] of Object.entries(effects)) {
            this.sounds[name] = await this.loadSound(path);
        }
    }

    // Team Themes
    async loadTeamThemes() {
        const teams = {
            DAL: {
                theme: "sounds/teams/cowboys_theme.mp3",
                chant: "sounds/teams/cowboys_chant.mp3",
                victory: "sounds/teams/cowboys_victory.mp3"
            },
            GB: {
                theme: "sounds/teams/packers_theme.mp3",
                chant: "sounds/teams/packers_chant.mp3",
                victory: "sounds/teams/packers_victory.mp3"
            }
            // Add more teams... Thank You Cascade!!!   
        };

        for (const [team, sounds] of Object.entries(teams)) {
            this.teamThemes[team] = {
                theme: await this.loadSound(sounds.theme),
                chant: await this.loadSound(sounds.chant),
                victory: await this.loadSound(sounds.victory)
            };
        }
    }

    // Crowd Chants
    async loadCrowdChants() {
        const chants = {
            defense: "sounds/chants/defense.mp3",
            touchdown: "sounds/chants/touchdown.mp3",
            victory: "sounds/chants/victory.mp3",
            momentum: "sounds/chants/momentum.mp3"
        };

        for (const [name, path] of Object.entries(chants)) {
            this.crowdChants[name] = await this.loadSound(path);
        }
    }

    // Animation Methods
    playCelebration(type, position) {
        const animation = this.animations[type];
        if (!animation) return;

        const container = document.createElement('div');
        container.className = 'celebration-container';
        container.style.position = 'absolute';
        container.style.left = position.x + 'px';
        container.style.top = position.y + 'px';
        document.body.appendChild(container);

        // Create particles
        for (let i = 0; i < animation.particles; i++) {
            const particle = document.createElement('div');
            particle.className = 'celebration-particle';
            particle.style.backgroundColor = animation.colors[i % animation.colors.length];
            container.appendChild(particle);

            // Animate particle
            this.animateParticle(particle, animation);
        }

        // Clean up after animation
        setTimeout(() => {
            container.remove();
        }, animation.duration);
    }

    animateParticle(particle, animation) {
        const angle = Math.random() * Math.PI * 2;
        const velocity = Math.random() * 5 + 5;
        const size = Math.random() * 10 + 5;

        particle.style.width = size + 'px';
        particle.style.height = size + 'px';

        switch (animation.pattern) {
            case 'spiral':
                this.spiralAnimation(particle, angle, velocity);
                break;
            case 'burst':
                this.burstAnimation(particle, angle, velocity);
                break;
            case 'wave':
                this.waveAnimation(particle, angle, velocity);
                break;
            case 'explosion':
                this.explosionAnimation(particle, angle, velocity);
                break;
        }
    }

    // Sound Methods
    async loadSound(url) {
        try {
            const response = await fetch(url);
            const arrayBuffer = await response.arrayBuffer();
            return await this.audioContext.decodeAudioData(arrayBuffer);
        } catch (error) {
            console.log(`Failed to load sound: ${url}`);
            return null;
        }
    }

    playSound(name, options = {}) {
        const sound = this.sounds[name];
        if (!sound) return;

        const source = this.audioContext.createBufferSource();
        source.buffer = sound;

        // Create gain node for volume control
        const gainNode = this.audioContext.createGain();
        gainNode.gain.value = options.volume || 1.0;

        // Create stereo panner for position
        if (options.position) {
            const panner = this.audioContext.createStereoPanner();
            panner.pan.value = options.position;
            source.connect(panner);
            panner.connect(gainNode);
        } else {
            source.connect(gainNode);
        }

        gainNode.connect(this.audioContext.destination);
        source.start(0);
    }

    playTeamTheme(teamCode) {
        const theme = this.teamThemes[teamCode]?.theme;
        if (theme) {
            this.playSound(theme, { volume: 0.7 });
        }
    }

    playCrowdChant(type) {
        const chant = this.crowdChants[type];
        if (chant) {
            this.playSound(chant, { volume: 0.8 });
        }
    }

    // Animation Patterns
    spiralAnimation(particle, angle, velocity) {
        gsap.to(particle, {
            duration: 2,
            x: Math.cos(angle) * 100,
            y: Math.sin(angle) * 100,
            rotation: 360,
            ease: "power1.out",
            opacity: 0
        });
    }

    burstAnimation(particle, angle, velocity) {
        gsap.to(particle, {
            duration: 1.5,
            x: Math.cos(angle) * velocity * 20,
            y: Math.sin(angle) * velocity * 20,
            ease: "power2.out",
            opacity: 0
        });
    }

    waveAnimation(particle, angle, velocity) {
        gsap.to(particle, {
            duration: 2,
            x: Math.cos(angle) * 150,
            y: Math.sin(angle) * 150,
            ease: "elastic.out(1, 0.3)",
            opacity: 0
        });
    }

    explosionAnimation(particle, angle, velocity) {
        gsap.to(particle, {
            duration: 1,
            x: Math.cos(angle) * velocity * 30,
            y: Math.sin(angle) * velocity * 30,
            ease: "expo.out",
            opacity: 0
        });
    }
}

// Initialize when DOM is loaded
document.addEventListener('DOMContentLoaded', () => {
    window.quantumCelebrations = new QuantumCelebrations();
});
