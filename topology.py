import torch
import numpy as np
import random

class ResonantSphereKernel:
    """
    The Core 3D Topology Engine. 
    Maps signals to a spherical coordinate system where gain is determined by resonance.
    """
    def __init__(self, layers=7):
        self.layers = layers
        self.energy_grid = {} # The 'subconscious' latent heat grid
        self.epsilon = 1e-6    # Limiter for the Core singularity

    def get_cartesian(self, r, theta, phi):
        """Converts spherical address to XYZ for distance calculations."""
        x = r * np.sin(theta) * np.cos(phi)
        y = r * np.sin(theta) * np.sin(phi)
        z = r * np.cos(theta)
        return torch.tensor([x, y, z], dtype=torch.float32)

    def calculate_resonant_gain(self, input_vector, node_pos_spherical):
        """
        The Pre-amp: G = (e^-dist) / max(r, eps)
        """
        r, theta, phi = node_pos_spherical
        node_xyz = self.get_cartesian(r, theta, phi)
        
        # Distance calculation (Phasing/Alignment)
        distance = torch.norm(input_vector - node_xyz)
        resonance = torch.exp(-distance)
        
        # Gain is 'stiffer' at the Core (lower r)
        gain = resonance / max(r, self.epsilon)
        return gain

    def fractal_dissipation(self, coordinate, energy_magnitude):
        """
        Takes a muted loop and scatters it through fractal pathways.
        This energy becomes 'latent heat' in the energy_grid.
        """
        r, theta, phi = coordinate
        num_sparks = 8
        energy_per_spark = (energy_magnitude * 0.8) / num_sparks # 20% friction loss
        
        sparks = []
        for _ in range(num_sparks):
            # Move randomly, favoring the 'outward' direction (increasing r)
            dr = random.uniform(0.05, 0.15) 
            dt = random.uniform(-0.1, 0.1)
            dp = random.uniform(-0.1, 0.1)
            
            new_coord = (min(1.0, r + dr), theta + dt, phi + dp)
            sparks.append((new_coord, energy_per_spark))
            
            # Update the latent heat (Dither/Inspiration floor)
            self.energy_grid[new_coord] = self.energy_grid.get(new_coord, 0) + energy_per_spark
            
        return sparks

class OverseerMonitor:
    """The 'Bored Skeptic' monitor."""
    def __init__(self, threshold=0.95):
        self.threshold = threshold

    def check_for_feedback(self, signal_history):
        variance = torch.var(torch.tensor(signal_history))
        if variance < (1 - self.threshold):
            return "MUTE" # Feedback detected
        return "PASS"
