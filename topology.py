import torch
import numpy as np

class SphericalResonantNode:
    """
    A single point in the 3D mapped intelligence.
    Positioned by Radius (Abstraction Layer), Theta, and Phi.
    """
    def __init__(self, radius, theta, phi):
        self.r = radius  # Layer depth (0.0 = Core, 1.0 = Surface/Raw Data)
        self.theta = theta
        self.phi = phi
        self.resonance = 0.0  # Current 'vibration' state
        self.damping = 0.1 * (1 - radius)  # Core layers have higher damping/stability

    def get_cartesian(self):
        """Converts spherical address to XYZ for 3D distance calculations."""
        x = self.r * np.sin(self.theta) * np.cos(self.phi)
        y = self.r * np.sin(self.theta) * np.sin(self.phi)
        z = self.r * np.cos(self.theta)
        return torch.tensor([x, y, z])

class ResonantGainStage(torch.nn.Module):
    """
    The 'Pre-amp'. Instead of static weights, gain is determined by 
    how well the input signal resonates with the node's geometry.
    """
    def __init__(self, num_layers=7):
        super().__init__()
        self.num_layers = num_layers
        
    def calculate_gain(self, input_vector, node_pos):
        # Gain is a function of phase alignment and radial depth
        # Core layers (low r) require more 'energy' to trigger
        distance = torch.norm(input_vector - node_pos)
        resonance_factor = torch.exp(-distance) # High resonance at low distance
        return resonance_factor / (node_pos[0] + 1e-6) # Gain increases with depth/radius

# --- The 'Bored Skeptic' (Overseer Lite) ---
class OverseerMonitor:
    def __init__(self, threshold=0.95):
        self.threshold = threshold
        self.history = []

    def check_for_feedback(self, signal_pattern):
        """Identifies high-Q, non-musical loops."""
        variance = torch.var(signal_pattern)
        if variance < (1 - self.threshold):
            return "MUTE: Feedback loop detected. Signal is too static."
        return "PASS: Signal is resonant."
