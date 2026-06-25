## ASL Finger-Spelling Translator

A real-time computer vision application that translates American Sign Language (ASL) finger-spelling (A–Z) into text using live webcam input and API-based inference.

[Insert a 5-second GIF here showing you spelling a word on camera and the text appearing on screen]

## Features

* **Real-Time API Inference:** Processes live webcam image frames and sends them to a vision-language API using highly engineered prompts for structured, accurate letter predictions.
* **Smart Buffering & Throttling:** Implements custom debouncing and sequential buffering to seamlessly stitch individual letter predictions into cohesive, meaningful words.
* **Secure Backend Architecture:** Features a dedicated backend for API authentication, request routing, and payload optimization to minimize latency during live inference.

## How It Works

1. **Capture:** The frontend captures continuous frames from the user's webcam.
2. **Throttle:** Frames are throttled to prevent API rate-limiting and ensure only clear, stable gestures are processed.
3. **Inference:** The backend routes the frame to the LLM/Vision API using a strict prompt template designed to return only structured letter outputs.
4. **Compile:** A buffering algorithm tracks sequential letters, accounting for duplicates and transitions, to output complete words.

## Tech Stack

* **Frontend:** [e.g., HTML/JS, React, OpenCV-Python]
* **Backend:** [e.g., Python, Flask, FastAPI, Node.js]
* **API Integration:** [e.g., OpenAI GPT-4o, Claude 3.5 Sonnet, Gemini Pro Vision]

## Quick Start

**1. Clone the repository**
git clone https://github.com/YourUsername/ASL-Translator.git
cd ASL-Translator

**2. Install dependencies**
pip install -r requirements.txt

**3. Set up environment variables**
Rename `.env.example` to `.env` and add your API key:
VISION_API_KEY=your_api_key_here

**4. Run the application**
python app.py
