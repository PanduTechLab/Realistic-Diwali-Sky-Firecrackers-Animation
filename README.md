# 🎆 Realistic Diwali Sky Firecrackers Animation

[![Language](https://img.shields.io/badge/Language-Python%20%7C%20HTML5%20%2F%20JS-blue.svg)](https://github.com)
[![Dependencies](https://img.shields.io/badge/Dependencies-Zero%20(Pure%20Standard%20Library)-success.svg)](https://github.com)
[![Platform](https://img.shields.io/badge/Platform-VS%20Code%20%7C%20Any%20Browser-orange.svg)](https://github.com)
[![License](https://img.shields.io/badge/License-MIT-purple.svg)](LICENSE)

A high-performance, cinematic Diwali sky fireworks simulation inspired by authentic night-sky fireworks photography. Features realistic particle physics, aerodynamic drag, multi-break shells, weeping golden willows with multi-color pistils, atmospheric smoke haze, and zero third-party dependencies.

Available in both a **Standard Realistic Version** and a **High Blast Speed Version**, playable as a standalone Python desktop app (via VS Code) or directly in any web browser (ready for GitHub Pages).

---

## 📸 Reference Firecracker Styles

| Firework Style | Inspiration | Physics & Visual Effect |
| :--- | :--- | :--- |
| **Needle Chrysanthemum** | *Image 4 & Ref 1* | Intense white-hot core with razor-sharp straight golden needle rays radiating in 360°, surrounded by floating crimson strobe sparks. |
| **Imperial Willow with Pistils** | *Image 5 & Ref 1* | 260+ weeping golden/salmon streamers cascading with realistic gravity, embedded with vivid emerald, magenta, and cyan pistil stars. |
| **Multi-Break Shell** | *Image 3* | Primary silver-white weeping willow shell followed by delayed secondary core bursts in violet and amber. |
| **Crackling Palm (Kamuro)** | *Image 2* | Fast outward-streaking comets leaving crackling sparklet trails. |
| **Ascending Rockets** | *Image 2 & 5* | Ballistic launches rising from below the screen with fiery exhaust trails and natural flight wobble. |

---

## 📂 Repository File Structure

```text
├── index.html               # 🌐 Standard realistic web simulation (GitHub Pages entry)
├── fast_firecrackers.html   # ⚡ High blast speed web simulation (1.8x - 2x velocity)
├── main.py                  # 🐍 Standard Python desktop application (VS Code ready)
├── fast_main.py             # ⚡ High blast speed Python application
├── images.jpg               # 🖼️ Reference photo: Imperial willow over water
├── images (1).jpg           # 🖼️ Reference photo: Needle chrysanthemum
├── images (2).jpg           # 🖼️ Reference photo: Ascending sky rockets
├── images (3).jpg           # 🖼️ Reference photo: Multi-break Hanabi shell
└── README.md                # 📖 Project documentation and guide
```

---

## 🚀 How to Run the Code to Get the Output

### Option 1: Running in Visual Studio Code (Python)

Both Python scripts use Python's built-in `tkinter` and `winsound` libraries—**no `pip install` required!**

1. **Open the project in VS Code**:
   - Launch VS Code.
   - Go to **File** > **Open Folder...** and select this directory.
2. **Choose a version to run**:
   - For the **Standard Realistic Version**: Open [main.py](main.py).
   - For the **High Blast Speed Version**: Open [fast_main.py](fast_main.py).
3. **Execute**:
   - Click the **▷ Run Python File** button in the top-right corner of VS Code, or
   - Open the integrated terminal (`Ctrl + ~`) and run:
     ```powershell
     py main.py
     ```
     *(or `py fast_main.py` for the fast version)*
4. A dedicated desktop window will launch immediately with 60 FPS particle physics and sound effects.

---

### Option 2: Running in Any Web Browser (HTML5 / JavaScript)

The web versions are self-contained and run locally offline in Google Chrome, Microsoft Edge, Mozilla Firefox, Brave, or Safari.

1. **Direct Double-Click**:
   - Double-click [index.html](index.html) or [fast_firecrackers.html](fast_firecrackers.html) in your file explorer.
2. **From VS Code**:
   - Right-click `index.html` > **Open with Live Server** (if the Live Server extension is installed), or
   - In the VS Code terminal, run:
     ```powershell
     start index.html
     ```
     *(or `start fast_firecrackers.html`)*
3. **Sound**: Click anywhere on the screen to initialize browser audio (Web Audio API).

---

## 🌐 How to Host Live for Free on GitHub Pages

You can publish this project as a live website on your GitHub profile in under 2 minutes:

1. **Create a GitHub Repository**:
   - Go to [GitHub](https://github.com/new).
   - Name your repository (e.g., `diwali-sky-firecrackers`).
   - Choose **Public** and click **Create repository**.
2. **Push your code**:
   ```bash
   git init
   git add .
   git commit -m "Initial commit: Realistic Diwali sky firecrackers animation"
   git branch -M main
   git remote add origin https://github.com/<your-username>/<your-repo-name>.git
   git push -u origin main
   ```
3. **Enable GitHub Pages**:
   - In your GitHub repository, click on **Settings** (gear icon at the top).
   - In the left sidebar, click on **Pages**.
   - Under **Build and deployment** > **Branch**:
     - Select branch: `main`
     - Select folder: `/(root)`
     - Click **Save**.
4. **Access your live link**:
   - Within 1–2 minutes, GitHub will generate your live link:
     ```text
     https://<your-username>.github.io/<your-repo-name>/
     ```
   - Anyone visiting this link can watch the animation directly in their browser without downloading any files!

---

## 🎮 Interactivity & Controls

- **Interactive Launches**: Click or tap anywhere on the dark sky at any time to launch a custom firecracker directly to your cursor coordinates.
- **Audio Effects**:
  - **Browser (`index.html`)**: Procedurally synthesized Web Audio API (launch whoosh, sub-bass detonation thump, sharp explosion crack, and sizzling sparkler crackles). Zero external MP3 files needed.
  - **Python (`main.py`)**: Threaded Windows `winsound` audio beeps and detonation pops.
- **Continuous Showcase**: Runs a choreographed beginning-to-end firework display that loops seamlessly.

---

## 🛠️ Technical Details

- **Rendering**: HTML5 2D Canvas with `globalCompositeOperation = 'lighter'` for authentic light emission bloom.
- **Physics Modeling**:
  - Velocity vectors: $\vec{v} = (v_x, v_y)$
  - Air resistance drag: $\vec{v} \leftarrow \vec{v} \times \text{drag}$
  - Gravity acceleration: $v_y \leftarrow v_y + g$
  - Particle history buffering for curved light trails.
- **Dependencies**: **0** (Zero external libraries or npm packages).

---

## 📄 License

This project is open-source and available under the [MIT License](LICENSE).
