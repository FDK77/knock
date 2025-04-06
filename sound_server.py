from flask import Flask, request
import os
import pygame


app = Flask(__name__)
pygame.mixer.init()

# Папка со звуками
SOUND_FOLDER = "./sounds"
current_channel = None
paused = False

@app.route('/play/<sound_name>', methods=['POST'])
def play_sound(sound_name):
    global current_channel, paused
    try:
        base_dir = os.path.dirname(__file__)
        sound_path = os.path.join(base_dir, "sounds", f"{sound_name}.mp3")

        if not os.path.exists(sound_path):
            return f"Файл {sound_name}.mp3 не найден", 404

        pygame.mixer.music.load(sound_path)
        pygame.mixer.music.play()
        paused = False
        return f"Playing: {sound_name}"
    except Exception as e:
        return f"Error: {str(e)}", 500


@app.route('/pause', methods=['POST'])
def pause_sound():
    global paused
    if pygame.mixer.music.get_busy():
        pygame.mixer.music.pause()
        paused = True
        return "Paused"
    return "Nothing playing", 400

@app.route('/resume', methods=['POST'])
def resume_sound():
    global paused
    if paused:
        pygame.mixer.music.unpause()
        paused = False
        return "Resumed"
    return "Nothing paused", 400

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
