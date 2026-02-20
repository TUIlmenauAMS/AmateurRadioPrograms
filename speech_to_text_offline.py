#!/usr/bin/env python3
"""
Grok: Can you make a Python program for Linux to recognize speech (German and English), which works also offline, and which displays the recognized speech in the terminal and also appends it to the file 'recognizedtext.txt'?
Gerald Schuller, November 2025

# Install system dependencies
sudo apt update
sudo apt install pulseaudio python3-pyaudio wget unzip

# Install Python package
pip3 install vosk sounddevice numpy

# Create models directory
mkdir -p vosk-models
cd vosk-models

# English small model (fast, good accuracy, ~50MB)
wget -c https://alphacephei.com/vosk/models/vosk-model-small-en-us-0.15.zip
unzip vosk-model-small-en-us-0.15.zip
mv vosk-model-small-en-us-0.15 en-us

# German small model (fast, good for general use, ~50MB)
wget -c https://alphacephei.com/vosk/models/vosk-model-small-de-0.15.zip
unzip vosk-model-small-de-0.15.zip
mv vosk-model-small-de-0.15 de

# Optional: better accuracy (larger models ~1GB each)
# English: vosk-model-en-us-0.22 (very accurate)
# German:  vosk-model-de-0.21

chmod +x speech_to_text_offline.py
./speech_to_text_offline.py          # English (default)
./speech_to_text_offline.py -l de    # German
"""


import argparse
import queue
import sys
import sounddevice as sd
import json
import os
from vosk import Model, KaldiRecognizer

# Output file
OUTPUT_FILE = "recognizedtext.txt"

q = queue.Queue()

def int_or_str(text):
    try:
        return int(text)
    except ValueError:
        return text

def callback(indata, frames, time, status):
    if status:
        print(status, file=sys.stderr)
    q.put(bytes(indata))

def ensure_model_path(lang):
    model_paths = {
        "en": "vosk-models/en-us",
        "de": "vosk-models/de",
    }
    path = model_paths.get(lang)
    if not path or not os.path.exists(path):
        print(f"Error: Model for '{lang}' not found at '{path}'")
        print("Download small models with:")
        print("  vosk-model-small-en-us-0.15 → folder name 'en-us'")
        print("  vosk-model-small-de-0.15     → folder name 'de'")
        sys.exit(1)
    return path

def save_text(text):
    if text.strip():
        print(f"\n✓ {text}")
        with open(OUTPUT_FILE, "a", encoding="utf-8") as f:
            f.write(text.strip() + "\n")

def main():
    parser = argparse.ArgumentParser(description="Offline speech recognition (English/German)")
    parser.add_argument("-l", "--language", choices=["en", "de"], default="en",
                        help="Language: en = English, de = German (default: en)")
    parser.add_argument("-d", "--device", type=int_or_str, help="Input device (number or substring)")
    args = parser.parse_args()

    model_path = ensure_model_path(args.language)
    print(f"Loading {'German' if args.language == 'de' else 'English'} model ...")
    model = Model(model_path)
    recognizer = KaldiRecognizer(model, 16000)
    recognizer.SetWords(True)

    print("\nListening... Speak now! (Press Ctrl+C to stop and save)\n")
    print("Language:", "German" if args.language == "de" else "English")
    print("-" * 60)

    try:
        with sd.RawInputStream(samplerate=16000, blocksize=8000, dtype='int16',
                               channels=1, callback=callback):

            while True:
                data = q.get()
                if recognizer.AcceptWaveform(data):
                    result = json.loads(recognizer.Result())
                    text = result.get("text", "").strip()
                    #print("text=", text, file=sys.stderr)
                    #os.system('espeak -vde -s 140 ' + text)
                    if text:
                        save_text(text)
                else:
                    partial = json.loads(recognizer.PartialResult())
                    partial_text = partial.get("partial", "")
                    print(f"\r{partial_text.ljust(80)}", end="", flush=True)

    except KeyboardInterrupt:
        # ←←← THIS IS THE IMPORTANT FIX ←←←
        print("\n\nStopping... Saving last phrase...")
        final_result = json.loads(recognizer.FinalResult())
        final_text = final_result.get("text", "").strip()
        if final_text:
            save_text(final_text)
        else:
            print("No final phrase detected.")

        print(f"\nAll done! Transcript saved to → {os.path.abspath(OUTPUT_FILE)}\n")

if __name__ == "__main__":
    main()
