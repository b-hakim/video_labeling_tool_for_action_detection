import PIL
import cv2
from PIL import ImageTk


def get_batch_from_video(cap, start, end):
    video_frames = []

    while True:
        has_frame, frame = cap.read()

        if start > end or not has_frame:
            break

        video_frames.append(frame)
        start += 1

    return video_frames


def update_canvas_from_cv_image(canvas, image):
    ch, cw = canvas.winfo_height(), canvas.winfo_width()
    image = image[:, :, ::-1]
    image = cv2.resize(image, (cw, ch))
    photo = ImageTk.PhotoImage(image=PIL.Image.fromarray(image))
    canvas.image = photo
    canvas.create_image(0, 0, image=photo, anchor="nw")
    canvas.update()