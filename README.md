# AI-Based Language Learning Assistant

The AI-Based Language Learning Assistant is an interactive web application built using **Streamlit**, **Hugging Face's GPT-2 Model**, and **Deep Translator**. This tool is designed to help users learn new languages through **text translation, AI-generated exercises, and progress tracking**. By leveraging machine learning, it provides real-time feedback and engaging exercises that adapt to the user's skill level. 

This project aims to provide **an accessible, intuitive, and efficient** way for users to enhance their language learning experience. Whether you're a beginner trying to learn the basics or an advanced learner looking for practice exercises, this app offers **personalized assistance** based on user input.


## Features
### 🔤 Translate Text
- Users can **input text** in any language, select a target language, and receive an **instant translation**.
- Uses **Deep Translator's Google Translate API** for accurate and reliable translations.
- Supports multiple languages including **Spanish, French, German, Chinese, and Arabic**.

### 📝 Generate Language Exercises
- Users can generate **custom exercises** based on their **skill level (Beginner, Intermediate, Advanced)** and topic of interest.
- Uses **Hugging Face's GPT-2 Model** instead of OpenAI to generate engaging exercises such as fill-in-the-blank questions and vocabulary practice.
- Promotes **active learning** by adapting to different proficiency levels.

### 📊 Track Learning Progress
- Users can **log their learning progress** and save notes for future reference.
- Saves progress in a JSON file (`progress.json`) to maintain session history.
- Helps learners reflect on their improvement over time.


## File Descriptions
### 1️⃣ `project.py` (Main Application)
This is the **core script** that powers the Streamlit web application. It contains:
- **User Interface (UI)**: Uses Streamlit to create interactive elements such as buttons, dropdowns, and text inputs.
- **Main Functions**:
  - `translate_text(text, target_language)`: Translates input text using Deep Translator.
  - `generate_language_exercise(skill_level, topic)`: Uses Hugging Face's GPT-2 model to generate exercises.
  - `track_learning_progress(user_data)`: Saves learning progress to a JSON file.

### 2️⃣ `test_project.py` (Unit Tests)
This file contains **pytest unit tests** to ensure all functions work correctly. It includes:
- **Mocking API calls** to avoid actual API requests during testing.
- **Test cases** for:
  - Translation accuracy
  - Correct exercise generation
  - Proper progress tracking in JSON format

### 3️⃣ `requirements.txt` (Dependencies)
A list of all **required Python packages** for the project:
- `streamlit` (Web UI framework)
- `deep-translator` (Translation services)
- `transformers` (AI-based text generation)
- `torch` (Required for Hugging Face models)
- `pytest` (Automated testing)


## Design Choices & Challenges
### 1️⃣ **Why Streamlit?**
We chose **Streamlit** because it allows for **quick deployment** and an **intuitive interface** without requiring extensive front-end development. The focus remains on language learning functionality rather than UI complexity.

### 2️⃣ **Why Deep Translator instead of GoogleTrans?**
GoogleTrans is outdated and frequently breaks due to **API changes**. Deep Translator offers **better stability and reliability** for real-world applications.

### 3️⃣ **Why Hugging Face's GPT-2 Instead of OpenAI's GPT-3.5?**
Initially, we planned to use **OpenAI's GPT-3.5 Turbo** to generate exercises. However, OpenAI's API requires **payment after a limited free quota**, which could be a challenge for users who want a completely free tool.

To overcome this limitation, we switched to **Hugging Face's GPT-2 model**, which is:
- **Completely free to use**.
- **Runs locally** without API restrictions.
- **Still capable of generating useful language exercises**.

### 4️⃣ **Handling Performance and Model Limitations**
While GPT-2 is free, it is less powerful than GPT-3.5. To improve performance:
- We **fine-tuned prompts** to generate coherent language exercises.
- We **limited output length** to keep responses concise and useful.
- Future versions may integrate **larger free models** from Hugging Face for improved quality.

## Academic Integrity & AI Usage
For this final project, We use r AI-based software: ChatGPT, GitHub Copilot, Bing Chat, but the essence of the work must still be OUR own. We have used such tools as **Help us to amplify productivity**, not to replace original work. 

This project was designed and implemented independently, with AI being used to optimize code, debug errors, and assist with documentation. However, all fundamental design choices, logic, and core implementations were done manually.

## How to Run the Project
### 📌 Install Dependencies
```bash
pip install -r requirements.txt
```

### 📌 Run the Application
```bash
streamlit run project.py
```

### 📌 Run Tests
```bash
pytest test_project.py
```

## Future Improvements
✅ **More Languages**: Expand supported languages for translation and exercises.
✅ **Speech-to-Text**: Allow users to speak instead of typing text.
✅ **Grammar Correction**: Use AI to suggest grammar improvements.
✅ **Leaderboard System**: Gamify learning with user progress comparisons.
✅ **Upgrade AI Model**: Consider using a larger Hugging Face model (e.g., GPT-neo) for better exercise generation.


## Conclusion
This project demonstrates the power of **AI in education**, offering a **practical and interactive** way to learn languages. By integrating **Streamlit, Hugging Face's GPT-2, and Deep Translator**, we created an accessible tool for **language learners of all levels**. 🚀

