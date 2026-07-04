# VoiceCraft API & App

### Production-Level Multi-Track Audio Editing & AI Enhancement Pipeline

VoiceCraft is a high-performance web application designed to handle non-destructive audio cutting, multi-file concatenation, and AI-driven background noise isolation. Driven by our proprietary `dhwanim_v0` neural model, it bridges the gap between raw field recordings and studio-grade outputs.

---

## 🌟 Key Functional Requirements

* **Non-Destructive Splitting & Slicing:** Isolate, delete, or export specific timestamps from large audio files without re-encoding delays.
* **Sequential Merging (Join):** Stitch multiple audio tracks into a single unified stream, managing varying bitrates and sample rates on the fly.
* **Neural Noise Suppression:** Leverage `dhwanim_v0` to isolate human speech frequencies and eliminate ambient environmental noise.
* **Studio-Grade Enhancer:** Apply automatic multi-band compression, dynamic equalization, and loudness normalization.

---

## 🏗️ System Architecture & Technology Stack

The platform separates fast binary file manipulation from heavy AI inference to maintain low latency across the pipeline:

```
                  ┌───────────────────┐
                  │   React.js Web    │
                  │   UI Engine       │
                  └─────────┬─────────┘
                            │ REST / WebSockets
                            ▼
                  ┌───────────────────┐
                  │  FastAPI Gateway  │
                  └─────────┬─────────┘
                            │ Task Queue (Redis / BullMQ)
                            ▼
        ┌───────────────────────────────────────┐
        │        Asynchronous Workers           │
        ├───────────────────┬───────────────────┤
        │    FFmpeg / Pydub │    dhwanim_v0     │
        │ (Binary Slicing)  │ (AI Model Node)   │
        └───────────────────┴───────────────────┘

```

### Core Stack

* **Frontend Interface:** React.js built around the HTML5 **Web Audio API** for real-time wave rendering and low-latency canvas visualizers.
* **Backend Orchestrator:** Python (FastAPI) handling chunked file uploads, multi-part form data processing, and client connection streaming.
* **Processing Core:** Native `FFmpeg` wrapper instances paired with `Pydub` and `Librosa` for ultra-fast audio manipulation and wave analysis.
* **AI Inference Layer:** Our proprietary `dhwanim_v0` audio enhancement framework optimized for rapid speech isolation.

---

## 🛠️ Step-by-Step Technical Setup

Follow this sequence exactly to boot up your local development environment.

### Prerequisites

Ensure you have `FFmpeg` installed and linked globally to your system variables.

```bash
# macOS
brew install ffmpeg

# Ubuntu/Debian
sudo apt update && sudo apt install ffmpeg

```

### 1. Backend Processing Engine Installation

```bash
# Clone and enter directory
git clone https://github.com/YOUR_USERNAME/voice-editing-app.git
cd voice-editing-app/backend

# Initialize isolation environment
python -m venv venv
source venv/bin/activate  # On Windows use: venv\Scripts\activate

# Install native dependencies and core modules
pip install -r requirements.txt

```

### 2. Frontend Interface Deployment

```bash
# Navigate to interface directory
cd ../frontend

# Install dependencies and launch local server
npm install
npm run dev

```

---

## 📜 Licensing & Usage Guidelines

This codebase is distributed under the **MIT License**. You are completely free to modify, branch, and scale this project for both personal and commercial product architectures.

---
