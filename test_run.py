import torch
from topology import ResonantSphereKernel, OverseerMonitor

def simulate_first_cry():
    # 1. Initialize the nervous system
    kernel = ResonantSphereKernel(layers=7)
    skeptic = OverseerMonitor(threshold=0.98) # High sensitivity for the first run

    # 2. Simulate a 'Static' Signal (The Feedback Loop)
    # Injecting the same vector repeatedly at a specific coordinate
    # Coordinate: (0.3 Radius, 1.57 Theta, 3.14 Phi) - Deep in the stack
    target_coord = (0.3, 1.57, 3.14)
    static_signal = torch.tensor([1.0, 0.0, 0.0]) 

    print(f"--- System Boot: Injecting signal at {target_coord} ---")

    signal_history = []
    for i in range(10):
        # Calculate gain for the current pulse
        gain = kernel.calculate_resonant_gain(static_signal, target_coord)
        signal_history.append(gain.item())

        print(f"Pulse {i}: Resonant Gain = {gain:.4f}")

        # 3. The Overseer Checks for Feedback
        if len(signal_history) > 5:
            status = skeptic.check_for_feedback(signal_history[-5:])
            if status == "MUTE":
                print(f"\n[!] OVERSEER ALERT: Feedback loop detected at pulse {i}.")
                print("Action: HARD MUTE engaged. Initiating Fractal Dissipation...")

                # 4. Dissipate the 'Heat'
                energy_to_bleed = sum(signal_history)
                sparks = kernel.fractal_dissipation(target_coord, energy_to_bleed)

                print(f"Success: {len(sparks)} fractal pathways created.")
                print(f"Current Latent Heat in Grid: {len(kernel.energy_grid)} nodes affected.")
                break

if __name__ == "__main__":
    simulate_first_cry()