# 🎆 Realistic Sky Firecrackers Animation

[![Language](https://img.shields.io/badge/Language-Python%20%7C%20HTML5%20%2F%20JavaScript-blue.svg)](https://github.com)
[![Dependencies](https://img.shields.io/badge/Dependencies-Zero%20(Pure%20Standard%20Library)-success.svg)](https://github.com)
[![Platform](https://img.shields.io/badge/Platform-VS%20Code%20%7C%20Any%20Browser-orange.svg)](https://github.com)
[![License](https://img.shields.io/badge/License-MIT-purple.svg)](LICENSE)

A clean, cinematic sky firecrackers animation featuring realistic particle physics, aerodynamic drag, multi-break shells, weeping golden willows with multi-color pistil stars, atmospheric smoke haze, and procedural audio.

Built with **zero external dependencies**—runs out of the box in **VS Code** via Python (`main.py`) or in **any web browser** via HTML5/JavaScript (`index.html`).

---

## 📂 Project Structure

```text
├── Firecrackers.html       # 🌐 Web animation (HTML5 Canvas + Web Audio API)
├── Firecrackers.py          # 🐍 Desktop animation (Python standard library Tkinter)
├── LICENSE          # 📄 MIT License
└── README.md        # 📖 Documentation and usage guide
```

---

## 🌟 Key Features

- **Realistic Shell Physics & Particle Dynamics**:
  - **Needle Chrysanthemums**: Blinding white-hot core with razor-sharp straight golden needle rays radiating in 360°, accompanied by floating crimson strobe sparks.
  - **Imperial Willows with Pistils**: 260+ weeping golden/salmon streamers cascading gracefully under gravity, embedded with vivid emerald, magenta, and cyan pistil stars.
  - **Multi-Break Hanabi Shells**: Silver-white weeping willow shell followed by delayed secondary bursts in violet and amber.
  - **Crackling Palms (Kamuro)**: Fast outward comets leaving crackling sparklet trails.
  - **Ascending Sky Rockets**: Ballistic launches rising from below the screen with fiery exhaust trails and natural flight wobble.
- **Deep Pitch-Black Sky (`#000000`)**: Decorated with a few faint, gently twinkling stars and illuminated drifting smoke clouds.
- **Zero UI Clutter**: Clean, full-screen cinematic presentation with no buttons, text overlays, or progress bars.
- **Continuous 30-Second Showcase**: Scripted beginning-to-end choreographed display that loops seamlessly.
- **Interactive**: Click or tap anywhere on the dark sky at any time to launch custom shells directly to your cursor.
- **Procedural Sound Effects**:
  - Web Audio API in `index.html` (whoosh, deep bass detonation thump, sharp crack, and crackling embers).
  - Windows `winsound` in `main.py`.

---

## 🚀 How to Run the Code to Get the Output

### Method 1: Running in Visual Studio Code (Python Desktop App)

The Python version uses standard library `tkinter` and `winsound`. No `pip install` commands are needed.

1. **Open the Project in VS Code**:
   - Launch VS Code.
   - Go to **File** > **Open Folder...** and select this project folder.
2. **Open the Script**:
   - Click on [Firecrackers.py](Firecrackers.py) in the VS Code file explorer.
3. **Run the Code**:
   - Click the **▷ Run Python File** button in the top-right corner of the editor, or
   - Open the integrated terminal (`Ctrl + ~`) and type:
     ```powershell
     py Firecrackers.py
     ```
     *(or `python Firecrackers.py` depending on your environment)*
4. **Result**: A dedicated desktop window will launch immediately, displaying the real-time particle fireworks animation and playing sound effects.

---

### Method 2: Running in Any Web Browser (HTML5 / JavaScript)

The web version is self-contained in a single file and works 100% offline in Chrome, Edge, Firefox, Brave, Safari, or Opera.

1. **Direct Double-Click**:
   - Open your file explorer and double-click [Firecrackers.html](Firecrackers.html). It will open immediately in your default browser.
2. **From VS Code Terminal**:
   - Open the VS Code terminal (`Ctrl + ~`) and run:
     ```powershell
     start Firecrackers.html
     ```
3. **Using VS Code Live Server**:
   - Right-click `Firecrackers.html` in the file explorer and select **Open with Live Server**.
4. **Result**: A full-screen dark sky animation opens. Click anywhere on the screen to initialize browser audio and interactively launch firecrackers.

---

## 🎮 Interactivity

- **Click / Tap**: Click anywhere in the sky to launch a custom firecracker directly to that coordinate.
- **Continuous Show**: The simulation runs automatically and seamlessly loops after the grand finale.

---

## 📄 License

This project is open-source under the [MIT License](LICENSE).
