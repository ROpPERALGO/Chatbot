from gtts import gTTS
import pygame
import time
import os


def tts(text, lang="en"):
    # Create a gTTS object
    tts = gTTS(text=text, lang=lang)
    # Save the audio to a file
    audio_file = "temp_audio.mp3"
    tts.save(audio_file)
    # Initialize pygame mixer
    pygame.mixer.init()
    # Load the audio file
    pygame.mixer.music.load(audio_file)
    # Play the audio file
    pygame.mixer.music.play()
    # Wait until the audio file is done playing
    while pygame.mixer.music.get_busy():
        time.sleep(1)
    # Remove the audio file after playing
    os.remove(audio_file)
