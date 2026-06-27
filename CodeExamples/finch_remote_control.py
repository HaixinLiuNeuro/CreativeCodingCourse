"""
Finch Robot 2.0 — Keyboard Remote Control
==========================================
Control your Finch in real time using keyboard keys.

Requirements:
  1. BlueBird Connector running and Finch connected via Bluetooth
  2. BirdBrain Python library installed (BirdBrain.py)
     Download: https://github.com/BirdBrainTechnologies/BirdBrain-Python-Library
  3. pynput library: pip install pynput

Controls:
  W / Up Arrow    — Drive forward
  S / Down Arrow  — Drive backward
  A / Left Arrow  — Turn left (in place)
  D / Right Arrow — Turn right (in place)
  Q / E           — Curve left / Curve right (while moving forward)
  Space           — Stop
  1 / 2 / 3       — Speed: Slow / Medium / Fast
  B               — Toggle beak LED color
  T               — Toggle tail LED color
  X               — Show sensor readings (distance, light, line)
  Esc             — Quit and disconnect

Author: CS Robotics Curriculum
"""

from BirdBrain import Finch
from pynput import keyboard
import time
import sys
import os

# ─── Configuration ──────────────────────────────────────────────
SPEEDS = {
    "slow":   30,
    "medium": 50,
    "fast":   80
}

BEAK_COLORS = [
    (0,   255, 0),    # Green
    (0,   0,   255),  # Blue
    (255, 0,   0),    # Red
    (255, 255, 0),    # Yellow
    (255, 0,   255),  # Purple
    (0,   255, 255),  # Cyan
    (255, 255, 255),  # White
    (0,   0,   0),    # Off
]

TAIL_COLORS = [
    (0,   255, 0),    # Green
    (0,   0,   255),  # Blue
    (255, 0,   0),    # Red
    (255, 128, 0),    # Orange
    (0,   0,   0),    # Off
]


class FinchRemoteControl:
    """Keyboard-based remote control for the Finch Robot 2.0."""

    def __init__(self):
        self.speed = SPEEDS["medium"]
        self.speed_name = "medium"
        self.beak_index = 0
        self.tail_index = 0
        self.running = True
        self.current_action = "Stopped"
        self.finch = None

    def connect(self):
        """Connect to the Finch via BlueBird Connector."""
        print("\n╔══════════════════════════════════════════════════╗")
        print("║       Finch Robot — Keyboard Remote Control     ║")
        print("╚══════════════════════════════════════════════════╝")
        print("\nConnecting to Finch...")
        print("(Make sure BlueBird Connector is running)\n")

        try:
            self.finch = Finch()
            print("✓ Connected to Finch!\n")
            # Flash beak green to confirm connection
            self.finch.setBeak(0, 255, 0)
            time.sleep(0.5)
            self.finch.setBeak(0, 0, 0)
            return True
        except Exception as e:
            print(f"✗ Could not connect to Finch: {e}")
            print("  Make sure BlueBird Connector is running")
            print("  and your Finch is paired via Bluetooth.\n")
            return False

    def print_controls(self):
        """Display the control reference."""
        print("┌──────────────────────────────────────────────────┐")
        print("│  CONTROLS                                        │")
        print("│                                                   │")
        print("│    W / ↑    Forward        1  Slow speed          │")
        print("│    S / ↓    Backward       2  Medium speed        │")
        print("│    A / ←    Turn left      3  Fast speed          │")
        print("│    D / →    Turn right                            │")
        print("│    Q        Curve left     B  Cycle beak color    │")
        print("│    E        Curve right    T  Cycle tail color    │")
        print("│    Space    Stop           X  Show sensors        │")
        print("│    Esc      Quit                                  │")
        print("└──────────────────────────────────────────────────┘")
        print(f"\n  Speed: {self.speed_name} ({self.speed}%)")
        print(f"  Status: {self.current_action}\n")

    def update_status(self, action):
        """Update and display current action."""
        self.current_action = action
        # Clear line and print status
        sys.stdout.write(f"\r  Speed: {self.speed_name} ({self.speed}%)  |  {action}          ")
        sys.stdout.flush()

    def show_sensors(self):
        """Read and display all sensor values."""
        try:
            distance = self.finch.getDistance()
            light_L = self.finch.getLight("L")
            light_R = self.finch.getLight("R")
            line_L = self.finch.getLine("L")
            line_R = self.finch.getLine("R")

            print(f"\n\n  ┌─ Sensor Readings ──────────────────┐")
            print(f"  │  Distance:    {distance:>4} cm              │")
            print(f"  │  Light (L/R): {light_L:>4} / {light_R:<4}          │")
            print(f"  │  Line  (L/R): {line_L:>4} / {line_R:<4}          │")
            print(f"  └──────────────────────────────────────┘\n")
        except Exception as e:
            print(f"\n  Could not read sensors: {e}\n")

    def on_key_press(self, key):
        """Handle key press events."""
        if not self.running or self.finch is None:
            return False

        try:
            # ── Character keys ──────────────────────────
            if hasattr(key, 'char') and key.char is not None:
                char = key.char.lower()

                if char == 'w':
                    self.finch.setMotors(self.speed, self.speed)
                    self.update_status("▲ Forward")

                elif char == 's':
                    self.finch.setMotors(-self.speed, -self.speed)
                    self.update_status("▼ Backward")

                elif char == 'a':
                    self.finch.setMotors(-self.speed, self.speed)
                    self.update_status("◄ Turning left")

                elif char == 'd':
                    self.finch.setMotors(self.speed, -self.speed)
                    self.update_status("► Turning right")

                elif char == 'q':
                    self.finch.setMotors(self.speed * 0.3, self.speed)
                    self.update_status("↰ Curving left")

                elif char == 'e':
                    self.finch.setMotors(self.speed, self.speed * 0.3)
                    self.update_status("↱ Curving right")

                elif char == '1':
                    self.speed = SPEEDS["slow"]
                    self.speed_name = "slow"
                    self.update_status("Speed: SLOW")

                elif char == '2':
                    self.speed = SPEEDS["medium"]
                    self.speed_name = "medium"
                    self.update_status("Speed: MEDIUM")

                elif char == '3':
                    self.speed = SPEEDS["fast"]
                    self.speed_name = "fast"
                    self.update_status("Speed: FAST")

                elif char == 'b':
                    self.beak_index = (self.beak_index + 1) % len(BEAK_COLORS)
                    r, g, b = BEAK_COLORS[self.beak_index]
                    self.finch.setBeak(r, g, b)
                    self.update_status(f"Beak: ({r},{g},{b})")

                elif char == 't':
                    self.tail_index = (self.tail_index + 1) % len(TAIL_COLORS)
                    r, g, b = TAIL_COLORS[self.tail_index]
                    self.finch.setTail("all", r, g, b)
                    self.update_status(f"Tail: ({r},{g},{b})")

                elif char == 'x':
                    self.finch.stop()
                    self.show_sensors()

            # ── Special keys ────────────────────────────
            elif key == keyboard.Key.up:
                self.finch.setMotors(self.speed, self.speed)
                self.update_status("▲ Forward")

            elif key == keyboard.Key.down:
                self.finch.setMotors(-self.speed, -self.speed)
                self.update_status("▼ Backward")

            elif key == keyboard.Key.left:
                self.finch.setMotors(-self.speed, self.speed)
                self.update_status("◄ Turning left")

            elif key == keyboard.Key.right:
                self.finch.setMotors(self.speed, -self.speed)
                self.update_status("► Turning right")

            elif key == keyboard.Key.space:
                self.finch.stop()
                self.update_status("■ Stopped")

            elif key == keyboard.Key.esc:
                self.running = False
                return False

        except Exception as e:
            self.update_status(f"Error: {e}")

    def on_key_release(self, key):
        """Stop motors when movement keys are released."""
        if not self.running or self.finch is None:
            return

        try:
            stop_keys_char = {'w', 'a', 's', 'd', 'q', 'e'}
            stop_keys_special = {
                keyboard.Key.up, keyboard.Key.down,
                keyboard.Key.left, keyboard.Key.right
            }

            if hasattr(key, 'char') and key.char and key.char.lower() in stop_keys_char:
                self.finch.stop()
                self.update_status("■ Stopped")

            elif key in stop_keys_special:
                self.finch.stop()
                self.update_status("■ Stopped")

        except Exception:
            pass

    def run(self):
        """Main control loop."""
        if not self.connect():
            return

        self.print_controls()

        # Start keyboard listener
        with keyboard.Listener(
            on_press=self.on_key_press,
            on_release=self.on_key_release
        ) as listener:
            try:
                listener.join()
            except KeyboardInterrupt:
                pass

        # Cleanup
        self.shutdown()

    def shutdown(self):
        """Safely disconnect from the Finch."""
        print("\n\n  Disconnecting from Finch...")
        try:
            if self.finch:
                self.finch.stop()
                self.finch.setBeak(0, 0, 0)
                self.finch.setTail("all", 0, 0, 0)
                self.finch.close()
            print("  ✓ Disconnected. Goodbye!\n")
        except Exception as e:
            print(f"  Disconnect error: {e}\n")


# ─── Entry point ────────────────────────────────────────────────
if __name__ == "__main__":
    controller = FinchRemoteControl()
    controller.run()
