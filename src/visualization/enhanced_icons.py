"""
Enhanced NFL Quantum Icons System
Comprehensive icon set for quantum football visualization
"""

class NFLEnhancedIcons:
    """Extended NFL-specific quantum icons and symbols"""
    
    # Quantum Field Icons
    QUANTUM_FIELD = {
        'entangled': '🌌',     # Quantum entanglement field
        'superposed': '🎆',    # Quantum superposition field
        'coherent': '✨',      # Quantum coherence field
        'resonating': '💫',    # Quantum resonance field
        'evolving': '🌀',      # Quantum evolution field
        'harmonized': '🎵',    # Field harmony
        'synchronized': '⚡',   # Field synchronization
        'amplified': '🔆',     # Field amplification
        'protected': '🛡️',     # Field protection
        'optimized': '🎯'      # Field optimization
    }
    
    # Player Development Icons
    DEVELOPMENT = {
        'leveling': '📈',      # Level increase
        'mastering': '🏆',     # Mastery achieved
        'learning': '📚',      # Learning process
        'practicing': '🎯',    # Practice mode
        'analyzing': '🔍',     # Analysis mode
        'innovating': '💡',    # Innovation
        'adapting': '🔄',      # Adaptation
        'evolving': '🦋',      # Evolution
        'transforming': '⚡',   # Transformation
        'perfecting': '💎'     # Perfection
    }
    
    # Team Synergy Icons
    SYNERGY = {
        'unified': '🤝',       # Team unity
        'coordinated': '⚙️',   # Coordination
        'harmonious': '🎭',    # Harmony
        'synchronized': '⚡',   # Synchronization
        'resonating': '🎵',    # Resonance
        'collaborating': '👥', # Collaboration
        'supporting': '🛡️',    # Support
        'protecting': '🏰',    # Protection
        'attacking': '⚔️',     # Attack
        'defending': '🛡️'      # Defense
    }
    
    # Mental State Icons
    MENTAL_STATE = {
        'focused': '🎯',       # Deep focus
        'alert': '👁️',         # High alert
        'calm': '🌊',          # Calmness
        'energized': '⚡',     # Energized
        'confident': '💪',     # Confidence
        'determined': '🦁',    # Determination
        'strategic': '♟️',     # Strategic thinking
        'creative': '🎨',      # Creativity
        'intuitive': '🔮',     # Intuition
        'mindful': '🧘'        # Mindfulness
    }
    
    # Game Momentum Icons
    MOMENTUM = {
        'surging': '🌊',       # Strong momentum
        'building': '📈',      # Building momentum
        'steady': '➡️',        # Steady momentum
        'shifting': '↔️',      # Shifting momentum
        'reversing': '↩️',     # Momentum reversal
        'explosive': '💥',     # Explosive momentum
        'dominating': '👑',    # Dominating momentum
        'recovering': '🔄',    # Recovering momentum
        'accelerating': '🚀',  # Accelerating momentum
        'peaking': '⭐'        # Peak momentum
    }
    
    # Field Conditions Icons
    FIELD_CONDITIONS = {
        'perfect': '✨',       # Perfect conditions
        'good': '👍',         # Good conditions
        'challenging': '💪',   # Challenging conditions
        'wet': '💧',          # Wet field
        'dry': '☀️',          # Dry field
        'windy': '💨',        # Windy conditions
        'cold': '❄️',         # Cold weather
        'hot': '🔥',          # Hot weather
        'indoor': '🏟️',       # Indoor stadium
        'outdoor': '🌳'       # Outdoor stadium
    }
    
    # Fan Energy Icons
    FAN_ENERGY = {
        'electric': '⚡',      # Electric atmosphere
        'loud': '📢',         # Loud crowd
        'cheering': '🎉',     # Cheering fans
        'excited': '🔥',      # Excited fans
        'tense': '😰',        # Tense atmosphere
        'celebrating': '🎊',   # Celebration
        'supporting': '📣',    # Support
        'anticipating': '🤔',  # Anticipation
        'unified': '🤝',      # Unity
        'passionate': '❤️'     # Passion
    }
    
    # Team Spirit Icons
    TEAM_SPIRIT = {
        'legendary': '🌟',     # Legendary status
        'elite': '👑',        # Elite status
        'rising': '🚀',       # Rising team
        'determined': '💪',    # Determined
        'united': '🤝',       # United
        'focused': '🎯',      # Focused
        'inspired': '💫',     # Inspired
        'dominant': '🦁',     # Dominant
        'resilient': '🛡️',    # Resilient
        'innovative': '💡'     # Innovative
    }
    
    # Packers Special Icons
    PACKERS = {
        'cheese': '🧀',       # Cheese power
        'crown': '👑',        # Championship
        'tradition': '🏆',    # Tradition
        'frozen': '❄️',       # Frozen tundra
        'legendary': '🌟',    # Legendary status
        'titletown': '🏰',    # Titletown
        'victory': '✌️',      # Victory
        'heritage': '📜',     # Heritage
        'power': '💪',        # Power
        'glory': '✨'         # Glory
    }
    
    @classmethod
    def get_icon(cls, category: str, state: str) -> str:
        """Get icon from any category"""
        categories = {
            'quantum': cls.QUANTUM_FIELD,
            'development': cls.DEVELOPMENT,
            'synergy': cls.SYNERGY,
            'mental': cls.MENTAL_STATE,
            'momentum': cls.MOMENTUM,
            'field': cls.FIELD_CONDITIONS,
            'fans': cls.FAN_ENERGY,
            'spirit': cls.TEAM_SPIRIT,
            'packers': cls.PACKERS
        }
        return categories.get(category, {}).get(state, '❓')
