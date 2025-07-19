# AI-Chatbot-Development-Using-Python-and-Free-Tools-or-APIs
🤖 AiChatBot with Voice Recognition and Real-time Chat
This project is a smart and interactive AI chatbot powered by the Groq API (using the LLaMA 3 model), voice input, and a beautiful Streamlit UI. It supports multi-language voice input, auto-translates it to English, and responds with intelligent answers in real-time.

📁 Project Structure
bash
Copy
Edit
├── Backend/
│   ├── Chatbot.py           # Handles AI response logic using Groq API
│   └── SpeechToText.py      # Handles speech recognition + language translation
│
├── Frontend/
│   └── Files/
│       └── Status.data      # Internal assistant status indicator
│
├── Data/
│   └── ChatLog.json         # Persistent chat history
│
├── main.py                  # Streamlit app with styled chat interface
├── .env                     # Environment variables (API key, language, etc.)
├── requirements.txt         # Python dependencies
1️⃣ Chatbot.py — AI Chat Backend
Purpose:
Handles text-based conversation with a powerful LLaMA3 model via the Groq API.

Key Features:

Loads settings from .env (e.g., GroqAPIKey, assistant/user name).

Maintains chat history in ChatLog.json.

Injects real-time date & time into system prompt.

Formats user input and AI output cleanly.

Handles API failures and retries automatically.

python
Copy
Edit
# Example usage:
response = ChatBot("What is the capital of Japan?")
print(response)
2️⃣ SpeechToText.py — Voice Recognition + Translation
Purpose:
Captures voice input using a local HTML + JavaScript interface and translates non-English speech to English using mtranslate.

Key Features:

Generates Voice.html to capture microphone input in browser.

Auto-detects spoken language (set via .env).

Translates to English if input is not English.

Modifies queries for grammatical consistency.

Fully automated via headless Chrome + Selenium.

python
Copy
Edit
# Example usage:
spoken_text = SpeechRecognition()
print(spoken_text)  # -> Returns cleaned English query
3️⃣ main.py — Streamlit Frontend
Purpose:
Provides a clean and interactive chatbot UI for both text and voice interactions.

Key Features:

Beautiful modern design using custom CSS.

Session-based chat history.

Voice input with “🎤 Speak” button.

Text input with “🚀 Send” button.

Dynamic responses from ChatBot backend.

Auto-scroll conversation area using HTML/CSS.

bash
Copy
Edit
# To run:
streamlit run main.py
🔐 .env Configuration
Create a .env file with:

ini
Copy
Edit
GroqAPIKey=your_groq_api_key
Username=jawed
Assistantname=ai chatbot
InputLanguage=hi-IN  # Example: 'en-US' for English, 'hi-IN' for Hindi
🛠 Requirements
Install all dependencies:

bash
Copy
Edit
pip install -r requirements.txt
Recommended packages:

streamlit

selenium

mtranslate

python-dotenv

webdriver-manager

groq

🚀 How to Use
Clone the repo

Set up .env with your Groq API key

Run the app:

bash
Copy
Edit
streamlit run main.py
Type or speak to interact with the chatbot!
Author

Made by [J.JAWED AHAMED] GitHub: Jawed2127
