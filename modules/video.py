import requests
import cv2
import tkinter as tk
from PIL import Image, ImageTk

root = tk.Tk()
root.attributes("-fullscreen", True)
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

canvas = tk.Canvas(root, width=screen_width, height=screen_height)
canvas.pack(fill='both', expand=True)



def download_video(file_name):
    resp = requests.get(f"https://api.olhar.media/videos/{file_name}").content
    with open('temp/video.mp4', 'wb') as file:
        file.write(resp)

async def view_video():

    overlay_image = Image.open("temp/qr_code.png")
    overlay_width = screen_width // 2
    overlay_height = screen_height // 2
    if overlay_width > overlay_height:
        overlay_width = overlay_height
    else:
        overlay_height = overlay_width
    overlay_image = overlay_image.resize((overlay_width, overlay_height), Image.LANCZOS)
    overlay_img_tk = ImageTk.PhotoImage(overlay_image)

    cap = cv2.VideoCapture('temp/video.mp4')

    fps = cap.get(cv2.CAP_PROP_FPS)
    total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
    duration = total_frames / fps

    while True:
        ret, frame = cap.read()
        if not ret:
            break
        
        current_frame = int(cap.get(cv2.CAP_PROP_POS_FRAMES))
        current_time = current_frame / fps
        
        frame = cv2.resize(frame, (screen_width, screen_height))

        cv2_im = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        img = Image.fromarray(cv2_im)
        img_tk = ImageTk.PhotoImage(image=img)
        
        canvas.create_image(0, 0, anchor='nw', image=img_tk)
        
        if duration - current_time <= 5:
            canvas.create_image(screen_width - overlay_width, 0, anchor='nw', image=overlay_img_tk)
        
        root.update()

    cap.release()

def destroy_overlay():
    root.destroy()