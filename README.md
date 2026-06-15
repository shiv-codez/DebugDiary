# 📔 DebugDiary — Your Code's Emotional Journal

> *Your code has feelings. Let it speak.*

Built for the **Agents League Hackathon 2026** · Microsoft AI Skills Fest · Creative Apps Track

---

## 🤔 What is this?

DebugDiary turns your buggy code into a dramatic, emotional diary entry — written from the code's own perspective. Then it actually fixes the bug.

Because sometimes your code just needs to vent.

---

## ✨ Features

- 📖 Generates a unique, funny diary entry for ANY buggy code
- 🔍 Identifies the exact bug with specific variable names
- ✅ Provides the corrected code at the end
- 🌐 Supports Python, Java, JavaScript, C++ and more

---

## 🏗️ Architecture

+------------------+

    |User|

+------------------+

|

v

+------------------+

| HTML/CSS Frontend|

|  + JavaScript UI |

+------------------+

|

| Fetch API Request

v

+------------------+

| Python Flask API |

+------------------+

|

| Build Prompt

v

+---------------------------+

| Google Gemini 2.5 Flash   |

+---------------------------+

|

| Returns:

| • Dramatic Diary Entry

| • Bug Explanation

| • Fixed Code

v

+------------------+

| Python Flask API |

+------------------+

|

| JSON Response

v

+------------------+

| JavaScript UI    |

+------------------+

|

v

+------------------+

| User Sees:       |

| • Debug Diary    |

| • Bug Fix        |

+------------------+

## 🛠 How GitHub Copilot Was Used

GitHub Copilot was used throughout development to:
- Generate Flask route structure and API integration code
- Suggest the HTML/CSS layout and dark theme styling
- Help debug the Gemini API connection issues
- Autocomplete repetitive boilerplate code

---

## 🚀 How to Run

1. Clone the repo
2. Install dependencies: pip install flask
3. Add your Gemini API key in `app.py`
4. Run:python app.py
5. Open `http://127.0.0.1:5000`

---

## 🧠 Tech Stack

- **Backend:** Python + Flask
- **Frontend:** HTML, CSS, JavaScript
- **AI:** Google Gemini 2.5 Flash API
- **Dev Tool:** GitHub Copilot

---

## 👨‍💻 Built by

Shiv · Agents League Hackathon 2026
