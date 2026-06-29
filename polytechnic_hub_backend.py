from flask import Flask, render_template, jsonify
import time

app = Flask(__name__)

# --- यह आपका डमी डेटाबेस है ---
# भविष्य में आप इस डेटा को Python के ज़रिए किसी असली डेटाबेस (जैसे MySQL या MongoDB) से जोड़ सकते हैं
APP_DATA = {
    "app_info": {
        "name": "Polytechnic Hub",
        "version": "1.0",
        "developer": "Admin"
    },
    "semesters": [1, 2, 3, 4, 5, 6],
    "branches": [
        "Computer Science", 
        "Electrical Eng.", 
        "Mechanical Eng.", 
        "Civil Eng.", 
        "Electronics"
    ],
    "subjects": {
        "1": ["Applied Math I", "Applied Physics I", "Eng. Drawing", "Fundamentals of IT"],
        "2": ["Applied Math II", "Applied Physics II", "Applied Chemistry", "Programming in C"],
        "default": ["Core Subject 1", "Core Subject 2", "Elective Subject", "Practical Lab"]
    },
    "content": {
        "videos": [
            {"id": 1, "title": "Complete Concept & Introduction", "duration": "45:00"},
            {"id": 2, "title": "Important Formulas & Derivations", "duration": "30:20"},
            {"id": 3, "title": "Previous Year Question Solutions", "duration": "55:10"}
        ],
        "pdfs": [
            {"id": 1, "title": "Chapter 1 - Handwritten Notes", "size": "2.4 MB"},
            {"id": 2, "title": "Important Questions Bank", "size": "1.1 MB"},
            {"id": 3, "title": "Syllabus Copy", "size": "0.5 MB"}
        ]
    }
}

# 1. यह रूट (Route) आपकी HTML फाइल को ब्राउज़र में लोड करेगा
@app.route('/')
def home():
    # Flask डिफ़ॉल्ट रूप से 'templates' फ़ोल्डर के अंदर HTML फ़ाइलें ढूँढता है
    return render_template('index.html')

# 2. यह API रूट (Route) है। आपका HTML/JS इस लिंक से डेटा मांगेगा।
@app.route('/api/get_data')
def get_data():
    # हम डेटा को JSON फॉर्मेट में फ्रंटएंड को भेज रहे हैं
    return jsonify(APP_DATA)

if __name__ == '__main__':
    # सर्वर चालू करने के लिए कोड
    print("🚀 Polytechnic Hub Server is starting...")
    app.run(debug=True, port=5000)