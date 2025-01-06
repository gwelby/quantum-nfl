"""Visualization engine for dashboard."""
from typing import Dict, Any, List
import numpy as np
from dataclasses import dataclass

@dataclass
class VisualizationConfig:
    width: int = 800
    height: int = 600
    color_blind_safe: bool = True
    high_contrast: bool = False
    text_size: str = "medium"

class VisualizationEngine:
    def __init__(self):
        self.config = VisualizationConfig()
        
    def render_network(self, data: Dict[str, Any]) -> Dict[str, Any]:
        """Render network visualization."""
        return {
            "width": self.config.width,
            "height": self.config.height,
            "elements": self._prepare_network_elements(data)
        }
        
    def _prepare_network_elements(self, data: Dict[str, Any]) -> List[Dict[str, Any]]:
        """Prepare network elements for visualization."""
        elements = []
        
        # Add nodes
        for node in data.get("nodes", []):
            elements.append({
                "data": {
                    "id": node["id"],
                    "label": node["id"],
                    "value": node.get("value", 0)
                },
                "position": self._calculate_position(len(elements))
            })
            
        # Add edges
        for edge in data.get("edges", []):
            elements.append({
                "data": {
                    "source": edge["source"],
                    "target": edge["target"],
                    "weight": edge.get("value", 1)
                }
            })
            
        return elements
        
    def _calculate_position(self, index: int) -> Dict[str, float]:
        """Calculate node position."""
        angle = (index * 2 * np.pi) / 32  # 32 NFL teams
        radius = min(self.config.width, self.config.height) * 0.4
        
        return {
            "x": self.config.width/2 + radius * np.cos(angle),
            "y": self.config.height/2 + radius * np.sin(angle)
        }
        
    def get_accessibility_settings(self) -> Dict[str, Any]:
        """Get accessibility settings."""
        return {
            "color_blind_safe": self.config.color_blind_safe,
            "high_contrast": self.config.high_contrast,
            "text_size": self.config.text_size
        }
        
    def get_responsive_layouts(self) -> Dict[str, Any]:
        """Get responsive layout configurations."""
        return {
            "mobile": {
                "grid": [1],
                "width": 360,
                "height": 640
            },
            "tablet": {
                "grid": [2, 2],
                "width": 768,
                "height": 1024
            },
            "desktop": {
                "grid": [3, 2],
                "width": 1920,
                "height": 1080
            }
        }
        
    def update_config(self, new_config: Dict[str, Any]):
        """Update visualization configuration."""
        for key, value in new_config.items():
            if hasattr(self.config, key):
                setattr(self.config, key, value)
