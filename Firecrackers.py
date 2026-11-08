#!/usr/bin/env python3
"""
Realistic Sky Firecrackers Animation
===================================
A clean, cinematic sky fireworks simulation directly matching the photographic references.
- Pitch-black night sky with a few subtle twinkling stars.
- Zero UI text, zero overlays, zero control bars.
- Highly detailed particle dynamics:
  * Needle Chrysanthemum with radiating rays and hot core (Image 4 & Ref 1)
  * Imperial Chrysanthemum with colorful pistil stars (Image 5)
  * Weeping Golden Willows with cascading trails (Ref images.jpg)
  * Multi-break shells with delayed secondary bursts (Ref images (3).jpg)
  * Ascending rockets with fiery spark tails (Ref images (2).jpg)
- Complete 30-second choreographed display with continuous seamless looping.
- Click anywhere to launch realistic custom firecrackers.
- Works out of the box in VS Code using Python's built-in Tkinter.
"""

import sys
import os
import math
import random
import time
import threading
import tkinter as tk

# Windows native sound support
try:
    import winsound
    HAS_WINSOUND = True
except ImportError:
    HAS_WINSOUND = False


class SoundFX:
    """Threaded audio effects via winsound."""
    @staticmethod
    def play_launch():
        if not HAS_WINSOUND:
            return
        threading.Thread(target=SoundFX._launch_worker, daemon=True).start()

    @staticmethod
    def _launch_worker():
        try:
            for freq in (220, 360, 580, 820):
                winsound.Beep(freq, 22)
        except Exception:
            pass

    @staticmethod
    def play_boom(is_heavy=False):
        if not HAS_WINSOUND:
            return
        threading.Thread(target=SoundFX._boom_worker, args=(is_heavy,), daemon=True).start()

    @staticmethod
    def _boom_worker(is_heavy):
        try:
            if is_heavy:
                winsound.Beep(130, 160)
                winsound.Beep(85, 200)
            else:
                winsound.Beep(160, 100)
                winsound.Beep(110, 120)
        except Exception:
            pass


class Rocket:
    """Ballistic ascending rocket with fiery trailing sparks."""
    def __init__(self, start_x, start_y, target_x, target_y, shell_type):
        self.start_x = start_x
        self.start_y = start_y
        self.x = start_x
        self.y = start_y
        self.target_x = target_x
        self.target_y = target_y
        self.shell_type = shell_type
        dist = math.hypot(target_x - start_x, target_y - start_y)
        self.duration = max(26, min(50, int(dist / 14)))
        self.step = 0
        self.trail = []
        SoundFX.play_launch()

    def update(self):
        self.step += 1
        progress = self.step / self.duration
        ease = 1 - math.pow(1 - progress, 2.2)
        self.x = self.start_x + (self.target_x - self.start_x) * ease
        self.y = self.start_y + (self.target_y - self.start_y) * ease
        self.trail.append((self.x, self.y))
        if len(self.trail) > 10:
            self.trail.pop(0)
        return self.step < self.duration


class Particle:
    """Individual firework spark with drag, gravity, and trajectory history."""
    def __init__(self, x, y, vx, vy, color, size, decay, gravity=0.10, is_willow=False, max_hist=8):
        self.x = x
        self.y = y
        self.vx = vx
        self.vy = vy
        self.color = color
        self.size = size
        self.alpha = 1.0
        self.decay = decay
        self.gravity = gravity
        self.drag = 0.965
        self.is_willow = is_willow
        self.max_hist = max_hist
        self.history = []

    def update(self):
        self.history.append((self.x, self.y))
        if len(self.history) > self.max_hist:
            self.history.pop(0)
        self.vx *= self.drag
        self.vy *= self.drag
        self.vy += self.gravity
        self.x += self.vx
        self.y += self.vy
        self.alpha -= self.decay
        return self.alpha > 0.04


class RealisticSkyFireworksApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Sky Firecrackers Animation")
        self.root.geometry("1100x750")
        self.root.minsize(800, 600)
        self.root.configure(bg="#000000")

        self.width = 1100
        self.height = 750

        # Simulation State
        self.current_time = 0.0
        self.total_duration = 30.0
        self.last_tick = time.time()
        self.executed_events = set()

        # Canvas (Pure fullscreen black canvas, ZERO UI text or buttons)
        self.canvas = tk.Canvas(
            self.root,
            bg="#000000",
            highlightthickness=0,
            cursor="crosshair"
        )
        self.canvas.pack(fill=tk.BOTH, expand=True)

        # Entities
        self.rockets = []
        self.particles = []
        self.flashes = []

        # Color palettes matching reference images
        self.gold_palette = ["#fff9c4", "#ffecb3", "#ffe082", "#ffd54f", "#ffb300", "#ff8f00"]
        self.needle_palette = ["#ffffff", "#ffeb3b", "#ff9800", "#f44336"]
        self.pistil_colors = ["#00e676", "#ff4081", "#00e5ff", "#ffd700"]

        self._init_stars()
        self._init_timeline()

        self.canvas.bind("<Configure>", self._on_resize)
        self.canvas.bind("<Button-1>", self._on_click)

        self._loop()

    def _init_stars(self):
        # A few subtle, faint twinkling stars on pitch black
        self.stars = []
        count = max(35, (self.width * self.height) // 20000)
        for _ in range(count):
            self.stars.append({
                "x": random.randint(0, self.width),
                "y": random.randint(0, int(self.height * 0.9)),
                "color": random.choice(["#333333", "#555555", "#777777", "#999999", "#cccccc"]),
                "size": random.choice([1, 1, 2])
            })

    def _init_timeline(self):
        # 30-Second scripted showcase (exceeds 20 seconds)
        self.events = [
            # 0 - 3s: Solitary needle rocket
            (1.0, 0.42, 0.26, "needle"),
            # 3 - 7s: Twin imperial chrysanthemums with pistils (Image 5)
            (3.8, 0.28, 0.28, "imperial"),
            (4.5, 0.72, 0.25, "imperial"),
            # 7 - 11s: Multi-break & Needle
            (7.2, 0.50, 0.22, "needle"),
            (9.0, 0.34, 0.32, "multi"),
            (10.4, 0.68, 0.28, "palm"),
            # 11 - 16s: Sky Salvo
            (12.2, 0.20, 0.26, "imperial"),
            (13.0, 0.80, 0.24, "needle"),
            (14.0, 0.50, 0.20, "multi"),
            (15.2, 0.38, 0.30, "palm"),
            (16.0, 0.62, 0.26, "imperial"),
            # 16 - 20s: Pre-Finale Building Momentum
            (17.5, 0.25, 0.22, "needle"),
            (18.2, 0.75, 0.24, "multi"),
            (19.0, 0.50, 0.18, "imperial"),
            # 20 - 25s: GRAND FINALE (Continuous massive barrage)
            (20.2, 0.15, 0.26, "imperial"),
            (20.6, 0.85, 0.26, "imperial"),
            (21.0, 0.35, 0.20, "needle"),
            (21.4, 0.65, 0.20, "multi"),
            (21.9, 0.50, 0.16, "imperial"),
            (22.4, 0.25, 0.28, "palm"),
            (22.8, 0.75, 0.28, "needle"),
            (23.4, 0.45, 0.20, "imperial"),
            (24.0, 0.55, 0.22, "multi")
        ]

    def _on_resize(self, event):
        if event.width > 200 and event.height > 200:
            self.width = event.width
            self.height = event.height
            self._init_stars()

    def _on_click(self, event):
        click_x = event.x
        click_y = event.y
        shell_type = random.choice(["needle", "imperial", "multi", "palm"])
        start_x = click_x + random.randint(-50, 50)
        self.rockets.append(Rocket(start_x, self.height + 10, click_x, click_y, shell_type))

    def _explode_shell(self, x, y, shell_type):
        self.flashes.append({"x": x, "y": y, "r": 220, "life": 5})

        if shell_type == "needle":
            # IMAGE 4 & REF 1: Sharp needle chrysanthemum with hot core
            SoundFX.play_boom(is_heavy=False)
            rays = 80
            for i in range(rays):
                ang = (i / float(rays)) * math.pi * 2
                spd = 7.5
                self.particles.append(Particle(
                    x, y, math.cos(ang) * spd, math.sin(ang) * spd,
                    "#ffd54f", 2.0, 0.024, gravity=0.04, is_willow=False, max_hist=10
                ))
            # Floating crimson sparks
            for _ in range(40):
                ang = random.uniform(0, math.pi * 2)
                spd = random.uniform(0.6, 3.4)
                self.particles.append(Particle(
                    x, y, math.cos(ang) * spd, math.sin(ang) * spd,
                    "#ff1744", 2.2, 0.016, gravity=0.03, is_willow=False, max_hist=6
                ))
            # Blinding white center
            for _ in range(20):
                ang = random.uniform(0, math.pi * 2)
                spd = random.uniform(0.3, 2.0)
                self.particles.append(Particle(
                    x, y, math.cos(ang) * spd, math.sin(ang) * spd,
                    "#ffffff", 2.8, 0.04, gravity=0.02, is_willow=False, max_hist=4
                ))

        elif shell_type == "imperial":
            # IMAGE 5: Massive golden chrysanthemum with colorful pistils
            SoundFX.play_boom(is_heavy=True)
            count = 130
            for _ in range(count):
                ang = random.uniform(0, math.pi * 2)
                spd = math.pow(random.random(), 0.6) * 7.2 + 1.2
                col = random.choice(self.gold_palette)
                self.particles.append(Particle(
                    x, y, math.cos(ang) * spd, math.sin(ang) * spd,
                    col, 2.2, random.uniform(0.012, 0.022), gravity=0.08, is_willow=True, max_hist=12
                ))
            # Colorful pistil stars inside core (Image 5)
            for _ in range(45):
                ang = random.uniform(0, math.pi * 2)
                spd = random.uniform(0.8, 3.8)
                p_col = random.choice(self.pistil_colors)
                self.particles.append(Particle(
                    x, y, math.cos(ang) * spd, math.sin(ang) * spd,
                    p_col, 2.5, 0.020, gravity=0.05, is_willow=False, max_hist=6
                ))

        elif shell_type == "multi":
            # REF IMAGES (3).JPG: Multi-Break Shell
            SoundFX.play_boom(is_heavy=True)
            for _ in range(100):
                ang = random.uniform(0, math.pi * 2)
                spd = math.pow(random.random(), 0.7) * 7.0 + 1.2
                self.particles.append(Particle(
                    x, y, math.cos(ang) * spd, math.sin(ang) * spd,
                    "#ffffff", 2.2, 0.014, gravity=0.09, is_willow=True, max_hist=12
                ))
            self.root.after(220, lambda: self._explode_sub_shell(x - 14, y - 10, ["#ea80fc", "#ba68c8", "#ffffff"]))
            self.root.after(420, lambda: self._explode_sub_shell(x + 18, y + 12, ["#ffd54f", "#ffb300", "#ffffff"]))

        elif shell_type == "palm":
            # REF IMAGES (2).JPG: Crackling Palm
            SoundFX.play_boom(is_heavy=False)
            arms = 14
            for a in range(arms):
                ang = (a / float(arms)) * math.pi * 2
                spd = 6.4
                for k in range(5):
                    self.particles.append(Particle(
                        x, y, math.cos(ang) * (spd - k * 0.4), math.sin(ang) * (spd - k * 0.4),
                        "#ffb300", 2.4, 0.018, gravity=0.07, is_willow=True, max_hist=10
                    ))

    def _explode_sub_shell(self, x, y, colors):
        SoundFX.play_boom(is_heavy=False)
        self.flashes.append({"x": x, "y": y, "r": 150, "life": 4})
        for _ in range(50):
            ang = random.uniform(0, math.pi * 2)
            spd = random.uniform(1.2, 4.4)
            col = random.choice(colors)
            self.particles.append(Particle(
                x, y, math.cos(ang) * spd, math.sin(ang) * spd,
                col, 2.2, 0.022, gravity=0.05, is_willow=False, max_hist=6
            ))

    def _loop(self):
        now = time.time()
        dt = min(now - self.last_tick, 0.1)
        self.last_tick = now

        self.current_time += dt
        if self.current_time > self.total_duration:
            self.current_time = 0.0
            self.executed_events.clear()

        # Check timeline events
        for i, ev in enumerate(self.events):
            t_event, x_r, y_r, s_type = ev
            if self.current_time >= t_event and i not in self.executed_events:
                self.executed_events.add(i)
                start_x = int(self.width * (x_r + random.uniform(-0.08, 0.08)))
                target_x = int(self.width * x_r)
                target_y = int(self.height * y_r)
                self.rockets.append(Rocket(start_x, self.height + 10, target_x, target_y, s_type))

        # Update Rockets
        surviving_rockets = []
        for r in self.rockets:
            if r.update():
                surviving_rockets.append(r)
            else:
                self._explode_shell(r.target_x, r.target_y, r.shell_type)
        self.rockets = surviving_rockets

        # Update Particles
        surviving_particles = []
        for p in self.particles:
            if p.update():
                surviving_particles.append(p)
        self.particles = surviving_particles

        # Update Flashes
        for f in self.flashes:
            f["life"] -= 1
        self.flashes = [f for f in self.flashes if f["life"] > 0]

        # Draw Frame
        self._render()

        self.root.after(22, self._loop)

    def _render(self):
        c = self.canvas
        c.delete("all")

        # 1. Subtle Background Stars
        for s in self.stars:
            c.create_rectangle(s["x"], s["y"], s["x"] + s["size"], s["y"] + s["size"], fill=s["color"], outline="")

        # 2. Detonation Ambient Glow
        for f in self.flashes:
            r = f["r"]
            c.create_oval(f["x"] - r, f["y"] - r, f["x"] + r, f["y"] + r, fill="#1a1410", outline="")

        # 3. Rockets
        for r in self.rockets:
            if len(r.trail) > 1:
                flat_trail = [coord for pt in r.trail for coord in pt]
                c.create_line(*flat_trail, fill="#ffa000", width=2)
            c.create_oval(r.x - 3, r.y - 3, r.x + 3, r.y + 3, fill="#ffffff", outline="#ff9800")

        # 4. Particles & Silky Trails
        for p in self.particles:
            if len(p.history) > 1 and p.is_willow:
                flat_h = [coord for pt in p.history for coord in pt]
                c.create_line(*flat_h, fill=p.color, width=max(1, int(p.size * 0.7)))

            sz = max(1, int(p.size))
            c.create_oval(p.x - sz, p.y - sz, p.x + sz, p.y + sz, fill=p.color, outline="")


def main():
    root = tk.Tk()
    app = RealisticSkyFireworksApp(root)
    root.mainloop()


if __name__ == "__main__":
    main()
