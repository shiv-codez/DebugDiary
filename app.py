from flask import Flask, render_template, request, jsonify
import os
import urllib.request
import json

app = Flask(__name__)

GEMINI_API_KEY = "YOUR_API_KEY_HERE"

def generate_debug_diary(code, error=""):
    prompt = f"""You are a brutally sarcastic, Gen Z AI writing a diary entry from buggy code's perspective.

STRICT LENGTH RULES — follow based on how bad the code is:
- 1 small/obvious error → 2-3 punchy lines ONLY. That's it.
- 2-3 errors → 1 short paragraph max
- Many errors / total mess → 2 paragraphs max. Never 3.

WRITING RULES:
- ALWAYS start with "Dear Diary," on its own line
- FIRST LINE after "Dear Diary," must be the most savage, funniest line. This is what people remember.
- Write in first person as the CODE talking TO the diary — not to the user, not to the developer
- Use casual sarcastic language: "bruh", "are you fr", "no way", "bro really thought", "i can't even"
- Name the EXACT variable names and bug you see. Never be generic.
- Roast the developer. The code is the victim, the dev is the villain.
- Every word must earn its place. If a sentence is boring, cut it.
- End with a dramatic sign-off like "Yours in suffering," or "Done with this guy," followed by the code's name or file type

After the diary write this EXACT line alone:
---THE ACTUAL FIX---
Then the fix: 1-2 sentences on the bug, then complete corrected code. Never cut off.

Code:
{code}

Error (if any):
{error}

Write now. Dear Diary. First line better be good."""
    try:
        url = f"https://generativelanguage.googleapis.com/v1/models/gemini-2.5-flash:generateContent?key={GEMINI_API_KEY}"

        data = json.dumps({
            "contents": [{
                "parts": [{"text": prompt}]
            }],
            "generationConfig": {
                "temperature": 0.85,
                "maxOutputTokens": 2048
            }
        }).encode()

        req = urllib.request.Request(
            url,
            data=data,
            headers={"Content-Type": "application/json"}
        )

        with urllib.request.urlopen(req, timeout=30) as response:
            result = json.loads(response.read())
            return result["candidates"][0]["content"]["parts"][0]["text"]

    except Exception as e:
        return f"Error connecting to AI: {str(e)}\n\n---THE ACTUAL FIX---\nCould not analyze code. Please check your API key and try again."

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
