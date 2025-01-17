// Quantum NFL Matchup Component
class QuantumMatchup {
    constructor(container) {
        this.container = container;
        this.teams = {
            'Kansas City Chiefs': {
                logo: '/assets/teams/chiefs.png',
                colors: ['#E31837', '#FFB81C'],
                quantumSignature: {
                    offense: 0.92,
                    defense: 0.88,
                    special: 0.85,
                    momentum: 0.90
                },
                players: {
                    'Patrick Mahomes': {
                        position: 'QB',
                        quantumRating: 0.95,
                        superposition: 0.93,
                        entanglement: 0.91
                    },
                    'Travis Kelce': {
                        position: 'TE',
                        quantumRating: 0.89,
                        superposition: 0.87,
                        entanglement: 0.92
                    }
                }
            },
            'Buffalo Bills': {
                logo: '/assets/teams/bills.png',
                colors: ['#00338D', '#C60C30'],
                quantumSignature: {
                    offense: 0.89,
                    defense: 0.87,
                    special: 0.86,
                    momentum: 0.88
                },
                players: {
                    'Josh Allen': {
                        position: 'QB',
                        quantumRating: 0.92,
                        superposition: 0.90,
                        entanglement: 0.88
                    },
                    'Stefon Diggs': {
                        position: 'WR',
                        quantumRating: 0.88,
                        superposition: 0.89,
                        entanglement: 0.87
                    }
                }
            }
            // Add more teams...
        };
        
        this.initializeUI();
        this.setupEventListeners();
    }

    initializeUI() {
        this.container.innerHTML = `
            <div class="quantum-matchup">
                <div class="team-selection">
                    <div class="team-a">
                        <h3>Team A</h3>
                        ${this.createTeamSelector('team-a-select')}
                        <div class="quantum-signature" id="team-a-signature"></div>
                    </div>
                    <div class="vs-container">
                        <div class="quantum-interference"></div>
                        <h2>VS</h2>
                        <div class="prediction-container"></div>
                    </div>
                    <div class="team-b">
                        <h3>Team B</h3>
                        ${this.createTeamSelector('team-b-select')}
                        <div class="quantum-signature" id="team-b-signature"></div>
                    </div>
                </div>
                <div class="quantum-analysis">
                    <canvas id="quantum-visualization"></canvas>
                    <div class="analysis-details"></div>
                </div>
                <div class="key-matchups">
                    <h3>Quantum Key Matchups</h3>
                    <div class="matchup-grid"></div>
                </div>
            </div>
        `;

        // Initialize quantum visualization
        this.visualizer = new QuantumVisualizer('quantum-visualization');
    }

    createTeamSelector(id) {
        return `
            <select id="${id}" class="team-select">
                ${Object.keys(this.teams).map(team => 
                    `<option value="${team}">${team}</option>`
                ).join('')}
            </select>
        `;
    }

    setupEventListeners() {
        const teamASelect = this.container.querySelector('#team-a-select');
        const teamBSelect = this.container.querySelector('#team-b-select');

        teamASelect.addEventListener('change', () => this.updateMatchup());
        teamBSelect.addEventListener('change', () => this.updateMatchup());
    }

    updateMatchup() {
        const teamA = this.teams[this.container.querySelector('#team-a-select').value];
        const teamB = this.teams[this.container.querySelector('#team-b-select').value];

        // Update quantum signatures
        this.updateQuantumSignatures(teamA, teamB);

        // Calculate and display prediction
        const prediction = this.calculateQuantumPrediction(teamA, teamB);
        this.displayPrediction(prediction);

        // Update visualization
        this.visualizer.updateTeams(teamA, teamB);

        // Show key matchups
        this.displayKeyMatchups(teamA, teamB);
    }

    updateQuantumSignatures(teamA, teamB) {
        const signatureA = this.container.querySelector('#team-a-signature');
        const signatureB = this.container.querySelector('#team-b-signature');

        signatureA.innerHTML = this.createSignatureHTML(teamA);
        signatureB.innerHTML = this.createSignatureHTML(teamB);
    }

    createSignatureHTML(team) {
        return `
            <div class="signature-grid">
                <div class="signature-item">
                    <label>Offense</label>
                    <div class="quantum-bar" style="width: ${team.quantumSignature.offense * 100}%"></div>
                </div>
                <div class="signature-item">
                    <label>Defense</label>
                    <div class="quantum-bar" style="width: ${team.quantumSignature.defense * 100}%"></div>
                </div>
                <div class="signature-item">
                    <label>Special</label>
                    <div class="quantum-bar" style="width: ${team.quantumSignature.special * 100}%"></div>
                </div>
                <div class="signature-item">
                    <label>Momentum</label>
                    <div class="quantum-bar" style="width: ${team.quantumSignature.momentum * 100}%"></div>
                </div>
            </div>
        `;
    }

    calculateQuantumPrediction(teamA, teamB) {
        // Complex quantum calculation
        const offensiveInterference = Math.cos(
            (teamA.quantumSignature.offense - teamB.quantumSignature.defense) * Math.PI
        ) * 0.5 + 0.5;

        const defensiveInterference = Math.cos(
            (teamB.quantumSignature.offense - teamA.quantumSignature.defense) * Math.PI
        ) * 0.5 + 0.5;

        const momentumFactor = (teamA.quantumSignature.momentum + teamB.quantumSignature.momentum) / 2;

        return {
            winProbability: {
                teamA: (offensiveInterference * 0.4 + teamA.quantumSignature.momentum * 0.6),
                teamB: (defensiveInterference * 0.4 + teamB.quantumSignature.momentum * 0.6)
            },
            predictedScore: {
                teamA: Math.round(offensiveInterference * 35),
                teamB: Math.round(defensiveInterference * 35)
            },
            quantumState: this.determineQuantumState(offensiveInterference, defensiveInterference),
            confidence: this.calculateConfidence(teamA, teamB)
        };
    }

    determineQuantumState(offenseA, offenseB) {
        const difference = Math.abs(offenseA - offenseB);
        if (difference < 0.1) return 'Quantum Entangled';
        if (difference < 0.2) return 'Superposition';
        return 'Wave Function Collapsed';
    }

    calculateConfidence(teamA, teamB) {
        return 1 - Math.abs(
            teamA.quantumSignature.momentum - teamB.quantumSignature.momentum
        );
    }

    displayPrediction(prediction) {
        const container = this.container.querySelector('.prediction-container');
        container.innerHTML = `
            <div class="prediction-card">
                <h4>Quantum Prediction</h4>
                <div class="score-prediction">
                    <span>${prediction.predictedScore.teamA}</span>
                    <span>-</span>
                    <span>${prediction.predictedScore.teamB}</span>
                </div>
                <div class="quantum-state">
                    State: ${prediction.quantumState}
                </div>
                <div class="confidence">
                    Confidence: ${Math.round(prediction.confidence * 100)}%
                </div>
            </div>
        `;
    }

    displayKeyMatchups(teamA, teamB) {
        const container = this.container.querySelector('.matchup-grid');
        container.innerHTML = this.generateKeyMatchupsHTML(teamA, teamB);
    }

    generateKeyMatchupsHTML(teamA, teamB) {
        // Generate HTML for key player matchups
        return Object.entries(teamA.players).map(([playerA, statsA]) => {
            const matchingPlayerB = Object.entries(teamB.players)
                .find(([_, statsB]) => statsB.position === statsA.position);
            
            if (!matchingPlayerB) return '';

            const [playerBName, statsB] = matchingPlayerB;
            
            return `
                <div class="key-matchup">
                    <div class="player-a">
                        <h4>${playerA}</h4>
                        <div class="quantum-rating">
                            QR: ${statsA.quantumRating}
                        </div>
                    </div>
                    <div class="vs">vs</div>
                    <div class="player-b">
                        <h4>${playerBName}</h4>
                        <div class="quantum-rating">
                            QR: ${statsB.quantumRating}
                        </div>
                    </div>
                </div>
            `;
        }).join('');
    }
}

export default QuantumMatchup;
