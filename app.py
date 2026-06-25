import os
import base64
import json
from flask import Flask, render_template, request, jsonify
from dotenv import load_dotenv
import google.generativeai as genai
import numpy as np
import cv2

# Load private environmental keys
load_dotenv()
API_KEY = os.getenv("VISION_API_KEY")

# Initialize Flask App and configure Google Gemini API
app = Flask(__name__)
if API_KEY:
    genai.configure(api_key=API_KEY)

def format_image_for_api(base64_string):
    """Converts raw base64 webcam data from the frontend into Gemini vision format."""
    encoded_data = base64_string.split(',')[1]
    image_data = base64.b64decode(encoded_data)
    
    return {
        'mime_type': 'image/jpeg',
        'data': image_data
    }

@app.route('/')
def index():
    """Renders the main control panel workspace interface."""
    return render_template('index.html')

@app.route('/api/translate-frame', methods=['POST'])
def translate_frame():
    """Handles incoming frames, performs inference, and enforces structured returns."""
    if not API_KEY:
        return jsonify({'error': 'Server missing Gemini API Key entry config'}), 500
        
    data = request.json
    frame_data = data.get('image')
    
    if not frame_data:
        return jsonify({'error': 'No image frame sequence detected'}), 400

    try:
        # Convert frame string to vision input package
        vision_frame = format_image_for_api(frame_data)
        
        # Engine prompt targeting structured translation definitions
        prompt_instruction = (
            "Analyze the hand gesture shown in this webcam frame. "
            "Identify if it maps to an American Sign Language (ASL) finger-spelling letter (A-Z). "
            "Respond with a strict JSON format containing exactly one key: 'letter'. "
            "The value must be a single uppercase letter from A to Z, or 'SPACE' if the hand indicates a word break, "
            "or 'UNKNOWN' if no clear gesture is visible. Do not include markdown code block formatting."
        )

        model = genai.GenerativeModel('gemini-1.5-flash')
        response = model.generate_content([prompt_instruction, vision_frame])
        
        # Parse output data cleanly
        clean_text = response.text.strip().replace('```json', '').replace('```', '')
        result = json.loads(clean_text)
        
        return jsonify(result)

    except Exception as e:
        return jsonify({'error': f'Inference processing pipeline failed: {str(e)}'}), 500

if __name__ == '__main__':
    # Run the server locally on port 5000
    app.run(debug=True, port=5000)