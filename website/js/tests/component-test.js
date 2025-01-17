// NFL Quantum Experience Component Tests

class ComponentTester {
    constructor() {
        this.tests = [];
        this.results = {
            passed: 0,
            failed: 0,
            total: 0
        };
    }

    async runTests() {
        console.log('Starting NFL Quantum Experience Component Tests...');
        
        // Test Core Components
        await this.testQuantumClock();
        await this.testTeamsVisualization();
        await this.testCelebrations();
        await this.testMobileSupport();

        // Test Integrations
        await this.testSoundSystem();
        await this.testAnimations();
        await this.testPerformance();

        this.reportResults();
    }

    async testQuantumClock() {
        console.log('Testing Quantum Clock...');
        try {
            const clock = window.nflQuantum.components.clock;
            
            // Test initialization
            this.assert(clock !== undefined, 'Clock should be initialized');
            this.assert(typeof clock.update === 'function', 'Clock should have update method');
            
            // Test game states
            this.assert(Object.keys(clock.timeStates).length > 0, 'Clock should have time states');
            
            // Test animations
            const beforePhase = clock.quantumPhase;
            clock.update();
            this.assert(clock.quantumPhase !== beforePhase, 'Clock should animate');
            
            console.log('✓ Quantum Clock tests passed');
        } catch (error) {
            console.error('✗ Quantum Clock test failed:', error);
            this.results.failed++;
        }
    }

    async testTeamsVisualization() {
        console.log('Testing Teams Visualization...');
        try {
            const teams = window.nflQuantum.components.teams;
            
            // Test initialization
            this.assert(teams !== undefined, 'Teams visualization should be initialized');
            this.assert(typeof teams.update === 'function', 'Teams should have update method');
            
            // Test team data
            this.assert(teams.teamData && Object.keys(teams.teamData).length > 0, 'Teams should have data');
            
            console.log('✓ Teams Visualization tests passed');
        } catch (error) {
            console.error('✗ Teams Visualization test failed:', error);
            this.results.failed++;
        }
    }

    async testCelebrations() {
        console.log('Testing Celebrations System...');
        try {
            const celebrations = window.nflQuantum.components.celebrations;
            
            // Test initialization
            this.assert(celebrations !== undefined, 'Celebrations should be initialized');
            this.assert(Object.keys(celebrations.animations).length > 0, 'Should have animations');
            this.assert(Object.keys(celebrations.sounds).length > 0, 'Should have sounds');
            
            // Test celebration trigger
            const testCelebration = celebrations.playCelebration('touchdown', { x: 0, y: 0 });
            this.assert(testCelebration !== undefined, 'Should trigger celebration');
            
            console.log('✓ Celebrations System tests passed');
        } catch (error) {
            console.error('✗ Celebrations System test failed:', error);
            this.results.failed++;
        }
    }

    async testMobileSupport() {
        console.log('Testing Mobile Support...');
        try {
            const mobile = window.nflQuantum.components.mobile;
            
            // Test initialization
            this.assert(mobile !== undefined, 'Mobile support should be initialized');
            this.assert(typeof mobile.handleTouch === 'function', 'Should handle touch events');
            this.assert(typeof mobile.handleOrientation === 'function', 'Should handle orientation');
            
            console.log('✓ Mobile Support tests passed');
        } catch (error) {
            console.error('✗ Mobile Support test failed:', error);
            this.results.failed++;
        }
    }

    async testSoundSystem() {
        console.log('Testing Sound System...');
        try {
            const celebrations = window.nflQuantum.components.celebrations;
            
            // Test audio context
            this.assert(celebrations.audioContext instanceof (window.AudioContext || window.webkitAudioContext), 
                'Should have audio context');
            
            // Test sound loading
            const testSound = await celebrations.loadSound('sounds/test.mp3');
            this.assert(testSound !== null, 'Should load sounds');
            
            console.log('✓ Sound System tests passed');
        } catch (error) {
            console.error('✗ Sound System test failed:', error);
            this.results.failed++;
        }
    }

    async testAnimations() {
        console.log('Testing Animations...');
        try {
            const app = window.nflQuantum;
            
            // Test animation frame
            this.assert(typeof app.updateDemos === 'function', 'Should have animation loop');
            
            // Test pause/resume
            app.pauseAnimations();
            this.assert(document.hidden || !app.components.clock.isAnimating, 'Should pause animations');
            
            app.resumeAnimations();
            this.assert(!document.hidden && app.components.clock.isAnimating, 'Should resume animations');
            
            console.log('✓ Animations tests passed');
        } catch (error) {
            console.error('✗ Animations test failed:', error);
            this.results.failed++;
        }
    }

    async testPerformance() {
        console.log('Testing Performance...');
        try {
            const startTime = performance.now();
            
            // Run a complete update cycle
            window.nflQuantum.updateDemos();
            
            const endTime = performance.now();
            const updateTime = endTime - startTime;
            
            // Test frame time (should be under 16ms for 60fps)
            this.assert(updateTime < 16, 'Frame time should be under 16ms');
            
            console.log('✓ Performance tests passed');
        } catch (error) {
            console.error('✗ Performance test failed:', error);
            this.results.failed++;
        }
    }

    assert(condition, message) {
        if (condition) {
            this.results.passed++;
        } else {
            this.results.failed++;
            throw new Error(message);
        }
        this.results.total++;
    }

    reportResults() {
        console.log('\nTest Results:');
        console.log('-------------');
        console.log(`Passed: ${this.results.passed}`);
        console.log(`Failed: ${this.results.failed}`);
        console.log(`Total: ${this.results.total}`);
        console.log(`Success Rate: ${((this.results.passed / this.results.total) * 100).toFixed(2)}%`);
    }
}

// Run tests when page is loaded
document.addEventListener('DOMContentLoaded', async () => {
    const tester = new ComponentTester();
    await tester.runTests();
});
