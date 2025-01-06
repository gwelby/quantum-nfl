"""
NFL Quantum Icons System
Beautiful icons for quantum football visualization
"""

class NFLQuantumIcons:
    """NFL-specific quantum icons and symbols"""
    
    # Team Status Icons
    TEAM_ICONS = {
        'optimal': '🏈',  # Perfect team state
        'strong': '💪',   # Strong performance
        'growing': '📈',  # Improving
        'alert': '⚠️',    # Needs attention
        'critical': '🚨'  # Immediate action needed
    }
    
    # Player Status Icons
    PLAYER_ICONS = {
        'peak': '⭐',     # Peak performance
        'ready': '✅',    # Ready to play
        'training': '💪', # In training
        'recovery': '🔄', # Recovery mode
        'injured': '🏥'   # Medical attention
    }
    
    # Quantum State Icons
    QUANTUM_ICONS = {
        'entangled': '🌟',    # Quantum entanglement
        'superposed': '🌈',   # Quantum superposition
        'coherent': '✨',     # Quantum coherence
        'resonating': '🎯',   # Quantum resonance
        'evolving': '🔄'      # Quantum evolution
    }
    
    # Field Position Icons
    POSITION_ICONS = {
        'QB': '🎯',      # Quarterback
        'RB': '🏃',      # Running Back
        'WR': '⚡',      # Wide Receiver
        'TE': '🛡️',      # Tight End
        'OL': '🏰',      # Offensive Line
        'DL': '🗿',      # Defensive Line
        'LB': '🦁',      # Linebacker
        'CB': '🦅',      # Cornerback
        'S': '🦊'        # Safety
    }
    
    # Play Type Icons
    PLAY_ICONS = {
        'pass': '🎯',     # Passing play
        'run': '🏃',      # Running play
        'special': '⚡',   # Special teams
        'defense': '🛡️',  # Defensive play
        'timeout': '⏰'    # Timeout
    }
    
    # Energy Level Icons
    ENERGY_ICONS = {
        'maximum': '💯',   # Maximum energy
        'high': '🔋',      # High energy
        'medium': '⚡',    # Medium energy
        'low': '🔌',       # Low energy
        'depleted': '⚠️'   # Depleted energy
    }
    
    # Consciousness Icons
    CONSCIOUSNESS_ICONS = {
        'enlightened': '🧠',  # Peak consciousness
        'focused': '🎯',      # High focus
        'aware': '👁️',        # Awareness
        'learning': '📚',     # Learning state
        'resting': '😴'       # Recovery state
    }
    
    # Formation Icons
    FORMATION_ICONS = {
        'spread': '🌟',       # Spread formation
        'tight': '🔷',        # Tight formation
        'shotgun': '💫',      # Shotgun formation
        'pistol': '🎯',       # Pistol formation
        'wildcat': '🐱'       # Wildcat formation
    }
    
    # Success Icons
    SUCCESS_ICONS = {
        'touchdown': '🎊',    # Touchdown
        'fieldgoal': '🎯',    # Field Goal
        'conversion': '✨',    # Conversion
        'turnover': '❌',      # Turnover
        'safety': '🛡️'        # Safety
    }
    
    # Weather Icons
    WEATHER_ICONS = {
        'sunny': '☀️',        # Clear weather
        'cloudy': '☁️',       # Cloudy
        'rain': '🌧️',         # Rain
        'snow': '❄️',         # Snow
        'wind': '💨'          # Windy
    }
    
    @classmethod
    def get_team_icon(cls, status: str) -> str:
        """Get team status icon"""
        return cls.TEAM_ICONS.get(status, '❓')
        
    @classmethod
    def get_player_icon(cls, status: str) -> str:
        """Get player status icon"""
        return cls.PLAYER_ICONS.get(status, '❓')
        
    @classmethod
    def get_quantum_icon(cls, state: str) -> str:
        """Get quantum state icon"""
        return cls.QUANTUM_ICONS.get(state, '❓')
        
    @classmethod
    def get_position_icon(cls, position: str) -> str:
        """Get position icon"""
        return cls.POSITION_ICONS.get(position, '❓')
        
    @classmethod
    def get_play_icon(cls, play_type: str) -> str:
        """Get play type icon"""
        return cls.PLAY_ICONS.get(play_type, '❓')
        
    @classmethod
    def get_energy_icon(cls, level: str) -> str:
        """Get energy level icon"""
        return cls.ENERGY_ICONS.get(level, '❓')
        
    @classmethod
    def get_consciousness_icon(cls, state: str) -> str:
        """Get consciousness state icon"""
        return cls.CONSCIOUSNESS_ICONS.get(state, '❓')
        
    @classmethod
    def get_formation_icon(cls, formation: str) -> str:
        """Get formation icon"""
        return cls.FORMATION_ICONS.get(formation, '❓')
        
    @classmethod
    def get_success_icon(cls, outcome: str) -> str:
        """Get success icon"""
        return cls.SUCCESS_ICONS.get(outcome, '❓')
        
    @classmethod
    def get_weather_icon(cls, condition: str) -> str:
        """Get weather condition icon"""
        return cls.WEATHER_ICONS.get(condition, '❓')
