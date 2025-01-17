// Quantum Teams Visualization
import * as THREE from 'https://cdn.skypack.dev/three@0.132.2';
import { OrbitControls } from 'https://cdn.skypack.dev/three@0.132.2/examples/jsm/controls/OrbitControls.js';

export class QuantumTeamsViz {
    constructor(containerId = 'quantum-teams') {
        console.log('Initializing Quantum Teams visualization...', containerId);
        
        // Get container
        this.container = document.getElementById(containerId);
        if (!this.container) {
            console.error('QuantumTeamsViz: Container not found:', containerId);
            return; // Fail gracefully
        }

        // Setup Three.js scene
        this.scene = new THREE.Scene();
        this.camera = new THREE.PerspectiveCamera(75, this.container.clientWidth / this.container.clientHeight, 0.1, 1000);
        this.renderer = new THREE.WebGLRenderer({ 
            antialias: true, 
            alpha: true 
        });
        
        // Configure renderer
        this.renderer.setSize(this.container.clientWidth, this.container.clientHeight);
        this.renderer.setPixelRatio(window.devicePixelRatio);
        this.container.appendChild(this.renderer.domElement);
        
        // Add controls
        this.controls = new OrbitControls(this.camera, this.renderer.domElement);
        this.controls.enableDamping = true;
        this.controls.dampingFactor = 0.05;
        
        // Position camera
        this.camera.position.z = 15;
        
        // Initialize state
        this.teams = [];
        this.quantumConnections = [];
        this.consciousness = 0;
        
        // Setup teams
        this.initTeams();
        
        // Start animation
        this.animate();
        
        // Handle window resize
        window.addEventListener('resize', () => this.onWindowResize());
        
        console.log('Quantum Teams visualization initialized');
    }

    initTeams() {
        const NFL_DIVISIONS = {
            'AFC': {
                'North': ['BAL', 'CIN', 'CLE', 'PIT'],
                'South': ['HOU', 'IND', 'JAX', 'TEN'],
                'East': ['BUF', 'MIA', 'NE', 'NYJ'],
                'West': ['DEN', 'KC', 'LV', 'LAC']
            },
            'NFC': {
                'North': ['CHI', 'DET', 'GB', 'MIN'],
                'South': ['ATL', 'CAR', 'NO', 'TB'],
                'East': ['DAL', 'NYG', 'PHI', 'WAS'],
                'West': ['ARI', 'LAR', 'SF', 'SEA']
            }
        };

        // Create quantum spheres for each team
        Object.entries(NFL_DIVISIONS).forEach(([conference, divisions], confIndex) => {
            Object.entries(divisions).forEach(([division, teams], divIndex) => {
                teams.forEach((team, teamIndex) => {
                    this.createTeamQuantumSphere(team, confIndex, divIndex, teamIndex);
                });
            });
        });
    }

    createTeamQuantumSphere(team, confIndex, divIndex, teamIndex) {
        const geometry = new THREE.SphereGeometry(0.5, 32, 32);
        
        const vertexShader = 'varying vec2 vUv; varying vec3 vNormal; void main() { vUv = uv; vNormal = normalize(normalMatrix * normal); gl_Position = projectionMatrix * modelViewMatrix * vec4(position, 1.0); }';
        const fragmentShader = 'uniform float time; uniform float consciousness; uniform vec3 teamColor; varying vec2 vUv; varying vec3 vNormal; void main() { float wave = sin(vUv.x * 10.0 + time) * 0.5 + 0.5; float conscious = smoothstep(0.0, 1.0, consciousness); vec3 glowColor = mix(teamColor, vec3(1.0), conscious * wave); float fresnel = pow(1.0 - dot(vNormal, vec3(0.0, 0.0, 1.0)), 3.0); gl_FragColor = vec4(glowColor * (fresnel + 0.5), 1.0); }';

        const material = new THREE.ShaderMaterial({
            uniforms: {
                time: { value: 0 },
                consciousness: { value: 0 },
                teamColor: { value: new THREE.Color(this.getTeamColor(team)) }
            },
            vertexShader,
            fragmentShader
        });

        const sphere = new THREE.Mesh(geometry, material);
        const angle = (teamIndex / 4) * Math.PI * 2;
        const radius = 5 + confIndex * 3;
        sphere.position.set(
            Math.cos(angle) * radius,
            divIndex * 2 - 3,
            Math.sin(angle) * radius
        );

        sphere.userData = { team };
        this.teams.push(sphere);
        this.scene.add(sphere);
    }

    getTeamColor(team) {
        const TEAM_COLORS = {
            'ARI': '#97233F', 'ATL': '#A71930', 'BAL': '#241773', 'BUF': '#00338D',
            'CAR': '#0085CA', 'CHI': '#C83803', 'CIN': '#FB4F14', 'CLE': '#FF3C00',
            'DAL': '#003594', 'DEN': '#FB4F14', 'DET': '#0076B6', 'GB': '#203731',
            'HOU': '#03202F', 'IND': '#002C5F', 'JAX': '#006778', 'KC': '#E31837',
            'LAC': '#0080C6', 'LAR': '#003594', 'LV': '#000000', 'MIA': '#008E97',
            'MIN': '#4F2683', 'NE': '#002244', 'NO': '#D3BC8D', 'NYG': '#0B2265',
            'NYJ': '#125740', 'PHI': '#004C54', 'PIT': '#FFB612', 'SF': '#AA0000',
            'SEA': '#002244', 'TB': '#D50A0A', 'TEN': '#0C2340', 'WAS': '#773141'
        };
        return TEAM_COLORS[team] || '#FFFFFF';
    }

    onWindowResize() {
        if (!this.container) return;
        
        const width = this.container.clientWidth;
        const height = this.container.clientHeight;
        
        this.camera.aspect = width / height;
        this.camera.updateProjectionMatrix();
        this.renderer.setSize(width, height);
    }

    animate() {
        if (!this.container) return;
        
        requestAnimationFrame(() => this.animate());

        // Update quantum effects
        const time = performance.now() * 0.001;
        this.teams.forEach((team, index) => {
            // Update uniforms
            team.material.uniforms.time.value = time;
            team.material.uniforms.consciousness.value = (Math.sin(time + index) + 1) * 0.5;

            // Orbital rotation
            const orbitSpeed = 0.2 + (index % 4) * 0.05;
            const verticalBob = Math.sin(time * 2 + index) * 0.2;
            const radius = team.position.length();
            
            team.position.x = Math.cos(time * orbitSpeed) * radius;
            team.position.z = Math.sin(time * orbitSpeed) * radius;
            team.position.y += verticalBob - team.position.y * 0.1;

            // Self rotation
            team.rotation.y = time * 0.5;
            team.rotation.x = Math.sin(time * 0.5) * 0.2;
        });

        // Pulse the consciousness field
        this.consciousness = (Math.sin(time) + 1) * 0.5;

        // Update controls
        this.controls.update();

        // Render scene
        this.renderer.render(this.scene, this.camera);
    }
}

// Initialize when DOM is loaded
document.addEventListener('DOMContentLoaded', () => {
    const quantumTeams = new QuantumTeamsViz();
});
