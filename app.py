from flask import Flask, render_template, request, jsonify
import os
import urllib.request
import json
import time

app = Flask(__name__)

GEMINI_API_KEY = "YOUR_API_KEY_HERE"

def generate_debug_diary(code, error=""):
    prompt = f"""You are a DRAMATICALLY emotional, darkly funny AI writing a SHORT diary entry from buggy code's perspective.

RULES:
- Maximum 3 short paragraphs. Be BRIEF and PUNCHY.
- Be specific about the EXACT variable names and bugs you see
- Use humor, sarcasm, self-pity — like a tired overworked intern
- Reference the EXACT bug (like ZeroDivisionError, null pointer, etc.)
- Be funny, not boring and philosophical

After the diary, you MUST write this EXACT line alone:
THE ACTUAL FIX:
Then list the exact bugs and corrected code.

Code:
{code}

Error:
{error}

Write now. Short. Funny. Specific."""
    try:
        url = f"https://generativelanguage.googleapis.com/v1/models/gemini-2.5-flash:generateContent?key={GEMINI_API_KEY}"
        
        data = json.dumps({
            "contents": [{
                "parts": [{"text": prompt}]
            }],
            "generationConfig": {
                "temperature": 0.9,
                "maxOutputTokens": 2000
            }
        }).encode()

        req = urllib.request.Request(
            url,
            data=data,
            headers={"Content-Type": "application/json"}
        )
        time.sleep(1)
        with urllib.request.urlopen(req) as response:
            result = json.loads(response.read())
            return result["candidates"][0]["content"]["parts"][0]["text"]

    except Exception as e:
        return f"Error connecting to AI: {str(e)}\n\nTHE ACTUAL FIX:\nCould not analyze code. Please check your API key."

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/analyze', methods=['POST'])
def analyze():
    data = request.get_json()
    code = data.get('code', '')
    error = data.get('error', '')

    if not code.strip():
        return jsonify({'error': 'No code provided'}), 400

    diary = generate_debug_diary(code, error)
    return jsonify({'diary': diary})

if __name__ == '__main__':
    app.run(debug=True)