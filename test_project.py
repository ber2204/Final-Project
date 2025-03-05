import pytest
import json
from project import translate_text, generate_language_exercise, track_learning_progress
from unittest.mock import patch
from deep_translator import GoogleTranslator
from transformers import pipeline

def test_translate_text():
    with patch.object(GoogleTranslator, "translate", return_value="Hola"):
        result = translate_text("Hello", "es")
        assert result == "Hola"

def test_generate_language_exercise():
    with patch("project.generator") as mock_generator:
        mock_generator.return_value = [{"generated_text": "Fill in the blank: Hello, ___ you?"}]
        result = generate_language_exercise("Beginner", "greetings")
        assert "Fill in the blank" in result

def test_track_learning_progress(tmp_path):
    test_data = {"progress": "Completed lesson 1"}
    test_file = tmp_path / "progress.json"

    result = track_learning_progress(test_data)

    assert "Progress saved successfully" in result

    with open("progress.json", "r") as f:
        saved_data = json.load(f)
        assert saved_data == test_data