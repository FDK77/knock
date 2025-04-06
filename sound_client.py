import tkinter as tk
import requests
SERVER_URL = "http://<IP_СЕРВЕРА>:5000"  # Заменить на IP сервера

def play_sound(sound_name):
    requests.post(f"{SERVER_URL}/play/{sound_name}")

def pause_sound():
    requests.post(f"{SERVER_URL}/pause")

def resume_sound():
    requests.post(f"{SERVER_URL}/resume")

root = tk.Tk()
root.title("Звуковой контроллер")
root.geometry("300x300")

sounds = ["aaa", "medium_knock", "hand_knock", "blurp", "fork", "small_knock"]

tk.Label(root, text="Выбери звук:").pack(pady=5)

for sound in sounds:
    tk.Button(root, text=sound, width=20, command=lambda s=sound: play_sound(s)).pack(pady=2)

tk.Button(root, text="Пауза", width=20, command=pause_sound).pack(pady=10)
tk.Button(root, text="Возобновить", width=20, command=resume_sound).pack(pady=2)

root.mainloop()
