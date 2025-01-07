// NFL Quantum Game Simulator Frontend
class GameSimulator {
    constructor() {
        this.initializeTeamSelectors();
        this.setupDarkMode();
        this.setupCharts();
        
        this.gameState = {
            homeTeam: '',
            awayTeam: '',
            quarter: 1,
            timeRemaining: 900,
            homeScore: 0,
            awayScore: 0,
            possession: '',
            fieldPosition: 20,
            down: 1,
            yardsToGo: 10,
            momentum: 0.5
        };
        
        this.stats = {
            totalYards: 0,
            passingYards: 0,
            rushingYards: 0,
            sacks: 0,
            interceptions: 0,
            fumbles: 0,
            fieldGoals: {made: 0, attempted: 0},
            punts: 0,
            returnYards: 0
        };
        
        this.plays = [];
        this.simInterval = null;
        this.chart = null;
    }

    initializeTeamSelectors() {
        const homeSelect = document.getElementById('home-team');
        const awaySelect = document.getElementById('away-team');
        
        // Sort teams by name
        const sortedTeams = Object.entries(NFL_TEAMS).sort((a, b) => 
            a[1].name.localeCompare(b[1].name)
        );
        
        // Populate selectors
        sortedTeams.forEach(([code, team]) => {
            const homeOption = new Option(`${team.icon} ${team.name}`, code);
            const awayOption = new Option(`${team.icon} ${team.name}`, code);
            
            homeSelect.add(homeOption);
            awaySelect.add(awayOption);
        });
        
        // Set default selections
        homeSelect.value = 'GB';
        awaySelect.value = 'CHI';
        
        // Add change listeners for icons
        homeSelect.addEventListener('change', () => this.updateTeamIcon('home'));
        awaySelect.addEventListener('change', () => this.updateTeamIcon('away'));
        
        // Initial icon update
        this.updateTeamIcon('home');
        this.updateTeamIcon('away');
    }

    setupDarkMode() {
        const darkMode = window.matchMedia('(prefers-color-scheme: dark)').matches;
        document.documentElement.classList.toggle('dark', darkMode);
        
        document.getElementById('theme-toggle').addEventListener('click', () => {
            document.documentElement.classList.toggle('dark');
        });
    }

    setupCharts() {
        const ctx = document.getElementById('stats-chart').getContext('2d');
        this.chart = new Chart(ctx, {
            type: 'line',
            data: {
                labels: [],
                datasets: [
                    {
                        label: 'Quantum Momentum',
                        data: [],
                        borderColor: '#3B82F6',
                        tension: 0.4
                    },
                    {
                        label: 'Yards Gained',
                        data: [],
                        borderColor: '#10B981',
                        tension: 0.4
                    }
                ]
            },
            options: {
                responsive: true,
                maintainAspectRatio: false,
                animation: {
                    duration: 0
                },
                scales: {
                    y: {
                        beginAtZero: true
                    }
                }
            }
        });
    }

    updateTeamIcon(team) {
        const select = document.getElementById(`${team}-team`);
        const iconDiv = document.getElementById(`${team}-team-icon`);
        const teamData = NFL_TEAMS[select.value];
        
        if (teamData) {
            iconDiv.textContent = teamData.icon;
            select.style.backgroundColor = teamData.colors.primary;
            select.style.color = 'white';
        }
    }

    initializeGame(homeTeam, awayTeam) {
        const homeData = NFL_TEAMS[homeTeam];
        const awayData = NFL_TEAMS[awayTeam];
        
        this.gameState = {
            homeTeam,
            awayTeam,
            quarter: 1,
            timeRemaining: 900,
            homeScore: 0,
            awayScore: 0,
            possession: Math.random() > 0.5 ? homeTeam : awayTeam,
            fieldPosition: 20,
            down: 1,
            yardsToGo: 10,
            momentum: 0.5
        };
        
        // Reset stats
        this.stats = {
            totalYards: 0,
            passingYards: 0,
            rushingYards: 0,
            sacks: 0,
            interceptions: 0,
            fumbles: 0,
            fieldGoals: {made: 0, attempted: 0},
            punts: 0,
            returnYards: 0
        };
        
        // Update team displays
        document.getElementById('home-team-display').innerHTML = `${homeData.icon} ${homeTeam}`;
        document.getElementById('away-team-display').innerHTML = `${awayData.icon} ${awayTeam}`;
        
        // Show game sections
        document.getElementById('game-simulation').classList.remove('hidden');
        document.getElementById('game-stats').classList.remove('hidden');
        
        // Reset chart
        this.chart.data.labels = [];
        this.chart.data.datasets.forEach(dataset => dataset.data = []);
        this.chart.update();
        
        this.updateDisplay();
    }

    calculateQuantumProbability(baseProb) {
        const quantumNoise = (Math.random() - 0.5) * 0.2;
        const teamRating = NFL_TEAMS[this.gameState.possession].quantumRating;
        const momentumFactor = this.gameState.momentum;
        
        return Math.min(Math.max(baseProb + quantumNoise + (teamRating - 0.8) + (momentumFactor - 0.5), 0), 1);
    }

    simulatePlay() {
        const playType = Math.random();
        let playResult = '';
        let yards = 0;
        let momentumChange = 0;

        if (playType < this.calculateQuantumProbability(0.4)) { // Run play
            const success = Math.random() < this.calculateQuantumProbability(0.6);
            if (success) {
                yards = Math.floor(Math.random() * 8) + 2;
                playResult = `Run for ${yards} yards`;
                this.stats.rushingYards += yards;
                momentumChange = 0.05;
            } else {
                yards = Math.floor(Math.random() * 2) - 1;
                playResult = `Run for ${yards} yards`;
                this.stats.rushingYards += yards;
                momentumChange = -0.05;
            }
        } else if (playType < this.calculateQuantumProbability(0.9)) { // Pass play
            const completion = Math.random() < this.calculateQuantumProbability(0.65);
            if (completion) {
                yards = Math.floor(Math.random() * 20) + 5;
                playResult = `Pass complete for ${yards} yards`;
                this.stats.passingYards += yards;
                momentumChange = 0.1;
            } else {
                playResult = 'Incomplete pass';
                momentumChange = -0.05;
                
                // Possible interception
                if (Math.random() < this.calculateQuantumProbability(0.1)) {
                    playResult = 'Pass INTERCEPTED!';
                    this.stats.interceptions++;
                    this.changePossession();
                    momentumChange = -0.2;
                }
            }
        } else { // Special teams
            if (this.gameState.down === 4) {
                if (this.gameState.fieldPosition > 65) {
                    // Field goal attempt
                    const distance = 100 - this.gameState.fieldPosition + 17;
                    const success = Math.random() < this.calculateQuantumProbability(1 - distance/100);
                    this.stats.fieldGoals.attempted++;
                    if (success) {
                        this.stats.fieldGoals.made++;
                        playResult = `${distance} yard field goal is GOOD!`;
                        this.updateScore(3);
                        momentumChange = 0.15;
                    } else {
                        playResult = `${distance} yard field goal is NO GOOD`;
                        momentumChange = -0.1;
                    }
                } else {
                    // Punt
                    yards = -(Math.floor(Math.random() * 20) + 30);
                    playResult = `Punt for ${-yards} yards`;
                    this.stats.punts++;
                    
                    // Possible return
                    const returnYards = Math.floor(Math.random() * 15);
                    if (returnYards > 0) {
                        playResult += `, returned for ${returnYards} yards`;
                        this.stats.returnYards += returnYards;
                        yards += returnYards;
                    }
                }
            }
        }

        // Update momentum
        this.gameState.momentum = Math.min(Math.max(this.gameState.momentum + momentumChange, 0), 1);
        document.getElementById('momentum-bar').style.width = `${this.gameState.momentum * 100}%`;

        // Update game state
        this.updateGameState(yards);
        
        // Add play to history
        this.addPlayToHistory(playResult);
        
        // Update chart
        this.updateChart(yards);
        
        // Update display
        this.updateDisplay();
        
        // Update stats
        this.updateStats();
    }

    updateGameState(yards) {
        // Update field position
        this.gameState.fieldPosition += yards;
        
        // Update field position marker
        const marker = document.getElementById('field-position-marker');
        marker.style.left = `${this.gameState.fieldPosition}%`;
        
        // Check for touchdown
        if (this.gameState.fieldPosition >= 100) {
            this.updateScore(7);
            this.gameState.fieldPosition = 20;
            this.gameState.down = 1;
            this.gameState.yardsToGo = 10;
            this.changePossession();
            return;
        }
        
        // Update downs
        if (yards >= this.gameState.yardsToGo) {
            this.gameState.down = 1;
            this.gameState.yardsToGo = 10;
        } else {
            this.gameState.down++;
            this.gameState.yardsToGo -= yards;
        }
        
        // Update yards progress bar
        const progress = ((10 - this.gameState.yardsToGo) / 10) * 100;
        document.getElementById('yards-progress').style.width = `${progress}%`;
        
        // Check for turnover on downs
        if (this.gameState.down > 4) {
            this.changePossession();
            this.gameState.down = 1;
            this.gameState.yardsToGo = 10;
        }
        
        // Update time
        this.gameState.timeRemaining -= Math.floor(Math.random() * 20) + 25;
        if (this.gameState.timeRemaining <= 0) {
            if (this.gameState.quarter < 4) {
                this.gameState.quarter++;
                this.gameState.timeRemaining = 900;
            } else {
                this.endGame();
            }
        }
    }

    updateChart(yards) {
        const timeLabel = `${this.gameState.quarter}Q ${Math.floor(this.gameState.timeRemaining / 60)}:${(this.gameState.timeRemaining % 60).toString().padStart(2, '0')}`;
        
        this.chart.data.labels.push(timeLabel);
        this.chart.data.datasets[0].data.push(this.gameState.momentum);
        this.chart.data.datasets[1].data.push(yards);
        
        // Keep last 20 plays visible
        if (this.chart.data.labels.length > 20) {
            this.chart.data.labels.shift();
            this.chart.data.datasets.forEach(dataset => dataset.data.shift());
        }
        
        this.chart.update();
    }

    changePossession() {
        this.gameState.possession = 
            this.gameState.possession === this.gameState.homeTeam ? 
            this.gameState.awayTeam : this.gameState.homeTeam;
        this.gameState.momentum = 0.5;
    }

    updateScore(points) {
        if (this.gameState.possession === this.gameState.homeTeam) {
            this.gameState.homeScore += points;
        } else {
            this.gameState.awayScore += points;
        }
    }

    updateDisplay() {
        // Update score
        document.getElementById('score-display').textContent = 
            `${this.gameState.homeScore} - ${this.gameState.awayScore}`;
        
        // Update quarter and time
        const minutes = Math.floor(this.gameState.timeRemaining / 60);
        const seconds = this.gameState.timeRemaining % 60;
        document.getElementById('quarter-display').textContent = 
            `${this.gameState.quarter}${this.getQuarterSuffix()} Quarter - ${minutes}:${seconds.toString().padStart(2, '0')}`;
        
        // Update drive info
        document.getElementById('drive-info').textContent = 
            `${this.gameState.down}${this.getDownSuffix()} & ${this.gameState.yardsToGo} at ${this.gameState.possession} ${this.gameState.fieldPosition}`;
    }

    addPlayToHistory(playResult) {
        const playDiv = document.createElement('div');
        playDiv.className = 'p-2 border-b dark:border-gray-600';
        
        const timeStamp = document.createElement('span');
        timeStamp.className = 'text-sm text-gray-500 dark:text-gray-400';
        timeStamp.textContent = `${this.gameState.quarter}Q ${Math.floor(this.gameState.timeRemaining / 60)}:${(this.gameState.timeRemaining % 60).toString().padStart(2, '0')} - `;
        
        const playText = document.createElement('span');
        playText.textContent = playResult;
        
        playDiv.appendChild(timeStamp);
        playDiv.appendChild(playText);
        
        const playByPlay = document.getElementById('play-by-play');
        playByPlay.insertBefore(playDiv, playByPlay.firstChild);
        
        document.getElementById('last-play').textContent = playResult;
    }

    updateStats() {
        // Update stat values
        document.getElementById('total-yards').textContent = this.stats.passingYards + this.stats.rushingYards;
        document.getElementById('passing-yards').textContent = this.stats.passingYards;
        document.getElementById('rushing-yards').textContent = this.stats.rushingYards;
        document.getElementById('sacks').textContent = this.stats.sacks;
        document.getElementById('interceptions').textContent = this.stats.interceptions;
        document.getElementById('fumbles').textContent = this.stats.fumbles;
        document.getElementById('field-goals').textContent = `${this.stats.fieldGoals.made}/${this.stats.fieldGoals.attempted}`;
        document.getElementById('punts').textContent = this.stats.punts;
        document.getElementById('return-yards').textContent = this.stats.returnYards;
        
        // Update stat bars
        const maxYards = 400;
        document.getElementById('total-yards-bar').style.width = `${Math.min((this.stats.passingYards + this.stats.rushingYards) / maxYards * 100, 100)}%`;
        document.getElementById('passing-yards-bar').style.width = `${Math.min(this.stats.passingYards / maxYards * 100, 100)}%`;
        document.getElementById('rushing-yards-bar').style.width = `${Math.min(this.stats.rushingYards / maxYards * 100, 100)}%`;
        document.getElementById('sacks-bar').style.width = `${Math.min(this.stats.sacks / 10 * 100, 100)}%`;
        document.getElementById('interceptions-bar').style.width = `${Math.min(this.stats.interceptions / 5 * 100, 100)}%`;
        document.getElementById('fumbles-bar').style.width = `${Math.min(this.stats.fumbles / 5 * 100, 100)}%`;
        document.getElementById('field-goals-bar').style.width = `${this.stats.fieldGoals.attempted ? (this.stats.fieldGoals.made / this.stats.fieldGoals.attempted * 100) : 0}%`;
        document.getElementById('punts-bar').style.width = `${Math.min(this.stats.punts / 10 * 100, 100)}%`;
        document.getElementById('return-yards-bar').style.width = `${Math.min(this.stats.returnYards / 200 * 100, 100)}%`;
    }

    getQuarterSuffix() {
        const suffixes = ['st', 'nd', 'rd', 'th'];
        return suffixes[Math.min(this.gameState.quarter - 1, 3)];
    }

    getDownSuffix() {
        const suffixes = ['st', 'nd', 'rd', 'th'];
        return suffixes[Math.min(this.gameState.down - 1, 3)];
    }

    endGame() {
        clearInterval(this.simInterval);
        this.addPlayToHistory('🏁 Game Over 🏁');
        
        const homeTeam = NFL_TEAMS[this.gameState.homeTeam];
        const awayTeam = NFL_TEAMS[this.gameState.awayTeam];
        const winner = this.gameState.homeScore > this.gameState.awayScore ? homeTeam : awayTeam;
        
        setTimeout(() => {
            alert(`${winner.icon} ${winner.name} wins!\n\nFinal Score:\n${homeTeam.name}: ${this.gameState.homeScore}\n${awayTeam.name}: ${this.gameState.awayScore}`);
        }, 1000);
    }
}

// Initialize the simulator
document.addEventListener('DOMContentLoaded', () => {
    const simulator = new GameSimulator();
    
    document.getElementById('start-game').addEventListener('click', () => {
        const homeTeam = document.getElementById('home-team').value;
        const awayTeam = document.getElementById('away-team').value;
        
        // Clear previous game
        document.getElementById('play-by-play').innerHTML = '';
        
        // Initialize new game
        simulator.initializeGame(homeTeam, awayTeam);
        
        // Start simulation
        if (simulator.simInterval) {
            clearInterval(simulator.simInterval);
        }
        
        simulator.simInterval = setInterval(() => {
            simulator.simulatePlay();
        }, 2000); // Simulate a play every 2 seconds
    });
});

// Quantum NFL Simulator
class QuantumSimulator {
    constructor() {
        this.teams = {};
        this.quantumStates = new Map();
        this.entanglementPatterns = new Map();
        this.initializeSimulator();
    }

    initializeSimulator() {
        // Initialize quantum states for all teams
        NFL_TEAMS.forEach(team => {
            this.teams[team.id] = {
                name: team.name,
                stats: this.generateQuantumStats(),
                history: []
            };
            this.quantumStates.set(team.id, this.createQuantumState());
        });

        // Setup event listeners
        document.getElementById('simulateButton').addEventListener('click', () => this.runSimulation());
        this.populateTeamSelects();
    }

    generateQuantumStats() {
        return {
            offense: Math.random() * 100,
            defense: Math.random() * 100,
            specialTeams: Math.random() * 100,
            momentum: Math.random() * 100,
            quantumPotential: Math.random()
        };
    }

    createQuantumState() {
        return {
            superposition: Math.random(),
            entanglement: Math.random(),
            coherence: Math.random()
        };
    }

    populateTeamSelects() {
        const homeSelect = document.getElementById('homeTeam');
        const awaySelect = document.getElementById('awayTeam');

        NFL_TEAMS.forEach(team => {
            const option = document.createElement('option');
            option.value = team.id;
            option.textContent = team.name;
            homeSelect.appendChild(option.cloneNode(true));
            awaySelect.appendChild(option);
        });
    }

    calculateQuantumProbability(teamA, teamB) {
        const stateA = this.quantumStates.get(teamA);
        const stateB = this.quantumStates.get(teamB);
        
        return (stateA.superposition * stateB.coherence + 
                stateA.entanglement * stateB.superposition) / 2;
    }

    simulateQuantumPlay(offense, defense) {
        const quantumInterference = Math.random() * Math.PI;
        const waveFunctionCollapse = Math.sin(quantumInterference) ** 2;
        
        return (offense.stats.offense * waveFunctionCollapse - 
                defense.stats.defense * (1 - waveFunctionCollapse));
    }

    async runSimulation() {
        const homeTeamId = document.getElementById('homeTeam').value;
        const awayTeamId = document.getElementById('awayTeam').value;
        
        const homeTeam = this.teams[homeTeamId];
        const awayTeam = this.teams[awayTeamId];

        const results = document.getElementById('simulationResults');
        results.innerHTML = '<div class="quantum-loader"></div>';
        results.classList.remove('hidden');

        // Simulate quantum entanglement
        await this.simulateEntanglement(homeTeam, awayTeam);

        // Calculate probabilities
        const homeProb = this.calculateQuantumProbability(homeTeamId, awayTeamId);
        const awayProb = 1 - homeProb;

        // Simulate multiple universe outcomes
        const universes = this.simulateMultiverseOutcomes(homeTeam, awayTeam);

        // Display results
        this.displayResults(homeTeam, awayTeam, universes, homeProb, awayProb);
        this.updateCharts(homeTeam, awayTeam, universes);
    }

    async simulateEntanglement(teamA, teamB) {
        return new Promise(resolve => {
            setTimeout(() => {
                const entanglementStrength = Math.random();
                this.entanglementPatterns.set(`${teamA.name}-${teamB.name}`, entanglementStrength);
                resolve();
            }, 1000);
        });
    }

    simulateMultiverseOutcomes(teamA, teamB) {
        const universes = [];
        const numUniverses = 1000;

        for (let i = 0; i < numUniverses; i++) {
            const scoreA = this.simulateQuantumPlay(teamA, teamB);
            const scoreB = this.simulateQuantumPlay(teamB, teamA);
            
            universes.push({
                universe: i,
                scoreA: Math.max(0, Math.round(scoreA / 10)),
                scoreB: Math.max(0, Math.round(scoreB / 10))
            });
        }

        return universes;
    }

    displayResults(homeTeam, awayTeam, universes, homeProb, awayProb) {
        const results = document.getElementById('simulationResults');
        
        // Calculate average scores
        const avgScores = universes.reduce((acc, universe) => {
            acc.homeScore += universe.scoreA;
            acc.awayScore += universe.scoreB;
            return acc;
        }, { homeScore: 0, awayScore: 0 });

        avgScores.homeScore = Math.round(avgScores.homeScore / universes.length);
        avgScores.awayScore = Math.round(avgScores.awayScore / universes.length);

        // Find most probable outcome
        const mostProbable = this.findMostProbableOutcome(universes);

        results.innerHTML = `
            <div class="space-y-6">
                <h3 class="text-2xl font-bold mb-4">Quantum Simulation Results</h3>
                
                <div class="grid grid-cols-2 gap-4">
                    <div class="text-center">
                        <div class="text-lg font-bold">${homeTeam.name}</div>
                        <div class="text-3xl font-bold quantum-text">${avgScores.homeScore}</div>
                        <div class="text-sm">Win Probability: ${(homeProb * 100).toFixed(1)}%</div>
                    </div>
                    <div class="text-center">
                        <div class="text-lg font-bold">${awayTeam.name}</div>
                        <div class="text-3xl font-bold quantum-text">${avgScores.awayScore}</div>
                        <div class="text-sm">Win Probability: ${(awayProb * 100).toFixed(1)}%</div>
                    </div>
                </div>

                <div class="mt-6">
                    <h4 class="text-lg font-bold mb-2">Most Probable Outcome</h4>
                    <div class="quantum-card p-4">
                        <div class="text-center">
                            ${homeTeam.name} ${mostProbable.scoreA} - ${mostProbable.scoreB} ${awayTeam.name}
                        </div>
                    </div>
                </div>

                <div class="mt-6">
                    <h4 class="text-lg font-bold mb-2">Quantum Analysis</h4>
                    <div class="quantum-card p-4">
                        <ul class="space-y-2">
                            <li>Entanglement Strength: ${(this.entanglementPatterns.get(`${homeTeam.name}-${awayTeam.name}`) * 100).toFixed(1)}%</li>
                            <li>Quantum Coherence: ${((homeTeam.stats.quantumPotential + awayTeam.stats.quantumPotential) / 2 * 100).toFixed(1)}%</li>
                            <li>Universe Variants: ${universes.length}</li>
                        </ul>
                    </div>
                </div>
            </div>
        `;
    }

    findMostProbableOutcome(universes) {
        const outcomes = {};
        
        universes.forEach(universe => {
            const key = `${universe.scoreA}-${universe.scoreB}`;
            outcomes[key] = (outcomes[key] || 0) + 1;
        });

        const mostProbableKey = Object.entries(outcomes)
            .sort(([,a], [,b]) => b - a)[0][0];
        
        const [scoreA, scoreB] = mostProbableKey.split('-').map(Number);
        return { scoreA, scoreB };
    }

    updateCharts(homeTeam, awayTeam, universes) {
        // Update superposition chart
        this.updateSuperpositionChart(universes);
        
        // Update entanglement chart
        this.updateEntanglementChart(homeTeam, awayTeam);
        
        // Update wave function chart
        this.updateWaveFunctionChart(universes);
    }

    updateSuperpositionChart(universes) {
        const canvas = document.getElementById('superpositionChart');
        const ctx = canvas.getContext('2d');
        
        // Clear previous chart
        ctx.clearRect(0, 0, canvas.width, canvas.height);
        
        // Implementation of superposition visualization
        // (Add your preferred charting library implementation here)
    }

    updateEntanglementChart(teamA, teamB) {
        const canvas = document.getElementById('entanglementChart');
        const ctx = canvas.getContext('2d');
        
        // Clear previous chart
        ctx.clearRect(0, 0, canvas.width, canvas.height);
        
        // Implementation of entanglement visualization
        // (Add your preferred charting library implementation here)
    }

    updateWaveFunctionChart(universes) {
        const canvas = document.getElementById('waveFunctionChart');
        const ctx = canvas.getContext('2d');
        
        // Clear previous chart
        ctx.clearRect(0, 0, canvas.width, canvas.height);
        
        // Implementation of wave function visualization
        // (Add your preferred charting library implementation here)
    }
}

// Initialize the simulator when the page loads
document.addEventListener('DOMContentLoaded', () => {
    window.quantumSimulator = new QuantumSimulator();
});
