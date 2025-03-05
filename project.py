import streamlit as st
import os
from deep_translator import GoogleTranslator
import json
from transformers import pipeline

generator = pipeline("text-generation", model="gpt2")

def translate_text(text, target_language):
    try:
        return GoogleTranslator(source='auto', target=target_language).translate(text)
    except Exception as e:
        return f"Translation Error: {e}"

def generate_language_exercise(skill_level, topic):
    prompt = f"Generate a {skill_level} level language learning exercise about {topic}:"
    try:
        result = generator(prompt, max_length=100, num_return_sequences=1)
        return result[0]['generated_text']
    except Exception as e:
        return f"⚠️ Error generating exercise: {e}"

def track_learning_progress(user_data):
    try:
        with open("progress.json", "w") as file:
            json.dump(user_data, file)
        return "Progress saved successfully!"
    except Exception as e:
        return f"Error saving progress: {e}"

def main():
    st.title("🌍 AI-Based Language Learning Assistant (Free Model Version)")

    st.subheader("🔤 Translate Text")
    user_input = st.text_input("Enter text to translate:")
    target_lang = st.selectbox("Select target language", ["es", "fr", "de", "zh", "ar"])
    
    if st.button("Translate"):
        translated_text = translate_text(user_input, target_lang)
        st.write("**Translated Text:**", translated_text)

    st.subheader("📝 Generate Language Exercise")
    skill_level = st.selectbox("Select Skill Level", ["Beginner", "Intermediate", "Advanced"])
    topic = st.text_input("Enter topic for exercise:")
    
    if st.button("Generate Exercise"):
        exercise = generate_language_exercise(skill_level, topic)
        st.write("**Generated Exercise:**")
        st.write(exercise)

    st.subheader("📊 Track Learning Progress")
    user_progress = st.text_area("Enter your learning progress notes:")
    
    if st.button("Save Progress"):
        message = track_learning_progress({"progress": user_progress})
        st.success(message)

if __name__ == "__main__":
    main()