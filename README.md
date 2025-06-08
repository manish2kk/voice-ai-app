# voice-ai-app

🎙️ Voice AI App

### Convert Text to Speech | Noise Removal | Voice Change

## 🚀 Overview

Voice AI App is a powerful tool that allows users to **convert text into speech**, **remove background noise**, and **modify voice properties** for a seamless audio experience. Ideal for content creators, accessibility solutions, and interactive AI applications.

## 🌟 Features

✅ **Text-to-Speech (TTS)** – Converts written text into natural-sounding speech.

✅ **Speech-to-Text (STT)** – Converts speech to written text.

✅ **Voice Change** – Change your voice with a model voice.

✅ **Noise Removal** – Filters out background noise for crystal-clear studio level audio.

✅ **Voice Dub** – Change the language in the speech.

✅ **Accent change** – Change the accent in the speech.

✅ **Background music generation** – Create ambient music tracks

✅ **Sound effects** –Generate various sound effects

🛠️ Technologies Used

- **Frontend:** React.js
- **Backend:** Python (Flask/FastAPI)
- **AI & Processing:**
  - OpenAI Whisper for speech enhancements
  - Google TTS / Amazon Polly for text-to-speech
  - Librosa & Pydub for audio processing

## 🏗️ Setup & Installation

### Clone the repository

```bash
git clone https://github.com/manish2kk/voice-ai-app.git
cd voice-ai-app
```

### Install dependencies

#### 🖥️ Backend (Python)

```bash
cd backend
pip install -r requirements.txt
python app.py
```

#### 🖥️ Frontend (React)

```bash
cd frontend
npm install
npm start
```

## 📌 Usage

1️⃣ **Enter text** in the provided input field.
2️⃣ **Select voice options** (pitch, speed, noise filtering).
3️⃣ **Click ‘Generate Voice’** to process the audio.
4️⃣ **Download or play the generated audio** instantly.

## 📝 Contribution

Feel free to submit **pull requests** to enhance features!

```bash
git checkout -b new-feature
git add .
git commit -m "Added feature X"
git push origin new-feature
```

Then, create a **pull request** on GitHub.

## 📜 License

This project is licensed under **MIT License** – feel free to use, modify, and distribute.

# GenAI Web + Mobile App Backend (Dummy Implementation)

This repository contains a dummy backend implementation for a GenAI web and mobile application, following a microservices architecture. It demonstrates the high-level interactions between services for various audio processing capabilities.

**IMPORTANT:** This is a **simplified and dummy** implementation for demonstration and development purposes. It uses in-memory storage instead of databases, direct HTTP calls instead of message queues,and simulated AI processing with dummy audio files. **DO NOT use this code in a production environment as-is.**

## Capabilities Implemented (Dummy):

1. **Convert text to speech (TTS)** - (simulated with `gen-ai-worker-tts-service`)
2. **Convert speech to text (STT)** - (simulated with `gen-ai-worker-stt-service`)
3. **Remove noise from voice** - (simulated with `gen-ai-worker-noise-removal-service`)

   *(Other capabilities are outlined in the design but not implemented in this dummy code)*

## Architecture Overview:

* **API Gateway:** Single entry point, handles routing and basic JWT authentication.
* **User Management Service:** Manages user registration, login,and profile.
* **Payment Service:** Simulates payment processing and minute deduction/addition.
* **Storage Service:** Simulates file storage (locally on disk in a `data/` folder).
* **Audio Processing Orchestrator Service:** Dispatches audio processing jobs to various AI worker services.
* **GenAI Worker Services (TTS, STT, Noise Removal):** Individual microservices that simulate AI model inference.
* **Notification Service:** Simulates sending notifications.

## Getting Started

Follow these steps to set up and run the backend services locally using Docker Compose.

### Prerequisites

* **Docker Desktop** (for Windows/macOS)or **Docker Engine & Docker Compose** (for Linux) installed on your system.

### Setup Instructions

1. **Clone this Repository (or create the folder structure):**

   Ensure you have the exact folder structure as defined in the project design (copied below for reference).

   ```

   .

   ├── apps/

   │   ├── web/

   │   ├── mobile/

   │   └── admin-panel/

   ├── services/

   │   ├── api-gateway/

   │   ├── user-management-service/

   │   ├── payment-service/

   │   ├── storage-service/

   │   │   └── data/               # <-- IMPORTANT: Create this folder

   │   ├── audio-processing-orchestrator-service/

   │   ├── gen-ai-worker-tts-service/

   │   ├── gen-ai-worker-stt-service/

   │   ├── gen-ai-worker-noise-removal-service/

   │   └── notification-service/

   ├── shared/

   ├── infra/

   └── README.md

   ```
2. **Create Dummy Audio Files:**

   * Navigate to the `services/storage-service/data/` directory.
   * Create two small, valid `.wav` audio files:

     * `dummy_input.wav` (e.g., a few seconds of silence or a simple sound)
     * `dummy_output.wav` (e.g., another simple sound, distinct from `dummy_input.wav`)
   * These files will be copied into the Docker images and used by the services.
3. **Build and Run Services:**

   * Open your terminal or command prompt.
   * Navigate to the project root directory to see the `apps`, `services`, `shared`, `infra` folders.
   * Run the following command to build the Docker images and start all services:

     ```bash

     docker compose -f infra/docker-compose.yml build --no-cache

     ```
   * This command will:

     * Build a Docker image for each service based on its `Dockerfile`.
     * Start all services as defined in `docker-compose.yml`.
     * You should see logs fromall services in your terminal.

## Accessing and Testing the APIs

Once all services are up and running, you can interact with the API Gateway using tools like Postman, curl,or by accessing the Swagger UI.

* **API Gateway Swagger UI:** `http://localhost:8000/docs`

### Testing Flow (Example)

1. **Register a User:**

   * Go to `http://localhost:8000/docs`.
   * Expand `user-management-service`.
   * Find the `POST /api/users/register` endpoint.
   * Click "Try it out".
   * Provide a `username`, `email`,and `password`.
   * Click "Execute".
   * You should get a `200 OK` response with a `user_id`.
2. **Login to get a Token:**

   * Find the `POST /api/users/login` endpoint.
   * Click "Try it out".
   * Enter the `username` and `password` you just registered.
   * Click "Execute".
   * You will receive an `access_token`. **Copy this token.**
3. **Authorize in Swagger UI:**

   * At the top right of the Swagger UI, click the "Authorize" button.
   * Paste your `access_token` into the `value` field (prefixed with `Bearer ` ifnot already added by Swagger: `Bearer <your_token_here>`).
   * Click "Authorize"and then "Close". Your subsequent requests will now include the JWT.
4. **Check Account Status:**

   * Find `GET /api/users/account-status`.
   * Click "Try it out", then "Execute". (It uses the `user_id` from your token automatically).
   * You should see `paid_status: false` and `minutes_remaining:0`.
5. **Simulate a Payment:**

   * Find `POST /api/payments/create-checkout-session`.
   * Click "Try it out".
   * The `user_id` should be pre-filled from your token. Set `amount`, `currency`, `plan_name`.
   * Click "Execute". You'll get a `transaction_id` and a `redirect_url` (dummy).
   * **Simulate payment completion:**

     * Go to `POST /api/payments/webhook`.
     * Click "Try it out".
     * Enter the `transaction_id` you just got.
     * Set `status` to `completed`.
     * Set `minutes_added` to `60`.
     * Provide the `user_id` from your registered user.
     * Click "Execute".
     * Check your terminal logs for the `notification-service` to see the payment success message.
6. **Verify Account Status (after payment):**

   * Go back to `GET /api/users/account-status`.
   * Execute again. You should now see `paid_status: true` and `minutes_remaining:60`.
7. **Upload a Dummy Audio File (for processing):**

   * To simulate uploading a real audio file:

     * You'll need to base64 encode your `services/storage-service/data/dummy_input.wav` file.
     * You can use online tools or a Python script:

       ```python

       ```

import base64

withopen("services/storage-service/data/dummy_input.wav","rb")as f:

    encoded_string = base64.b64encode(f.read()).decode('utf-8')

print(encoded_string)

    ```

    * Copy the output base64 string.

    * Find`POST /api/storage/upload-audio`.

    * Click "Try it out".

    * Paste the`encoded_string` into `audio_b64`.

    * Provide a`file_name` (e.g., `my_input.wav`).

    * Click "Execute". You'll get the`file_path` for the uploaded dummy audio.

8. **Initiate Audio Processing (e.g., STT):**

   * Find `POST /api/audio/process-audio`.
   * Click "Try it out".
   * Set `capability` to `stt`.
   * Set `model_name` to `Whisper`.
   * Paste the `audio_b64` from your `dummy_input.wav` (the one you encoded).
   * Click "Execute". You'll get a `job_id`.
   * Check your terminal logs to see the orchestrator dispatching to the STT worker and the worker "processing".
9. **Check Job Status:**

   * Find `GET /api/audio/job-status/{job_id}`.
   * Click "Try it out".
   * Enter the `job_id` you received.
   * Click "Execute" repeatedly until the `status` changes to `completed`. You should also see `output_text`.
10. **Download Processed Audio (and debit minutes):**

    * Find `GET /api/audio/download-audio/{job_id}`.
    * Click "Try it out".
    * Enter the `job_id` (from the STT job).
    * Click "Execute".
    * You will receive `audio_b64` which is the base64 encoded `dummy_output.wav` file.
    * **Verify minutes:** Check `GET /api/users/account-status` again; you should see your `minutes_remaining` reduced.

---

This should be a solid foundation! Let me know if you want to tweak anything. 🚀🎧
