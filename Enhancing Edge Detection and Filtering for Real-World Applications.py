import cv2
import numpy as np
from tkinter import *
from tkinter import filedialog, messagebox
from PIL import Image, ImageTk
original = None
processed = None
def show_image(img):
    img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    img_pil = Image.fromarray(img_rgb)
    img_pil.thumbnail((500, 500))
    photo = ImageTk.PhotoImage(img_pil)
    image_label.config(image=photo)
    image_label.image = photo
def upload_image():
    global original, processed
    path = filedialog.askopenfilename(
        filetypes=[("Images", "*.jpg *.png *.jpeg *.bmp")]
    )
    if path:
        original = cv2.imread(path)
        processed = original.copy()
        show_image(processed)
def gaussian():
    global processed
    if original is None:
        return
    processed = cv2.GaussianBlur(original, (9, 9), 0)
    show_image(processed)
def median():
    global processed
    if original is None:
        return
    processed = cv2.medianBlur(original, 9)
    show_image(processed)
def sobel():
    global processed
    if original is None:
        return
    gray = cv2.cvtColor(original, cv2.COLOR_BGR2GRAY)
    sx = cv2.Sobel(gray, cv2.CV_64F, 1, 0, ksize=3)
    sy = cv2.Sobel(gray, cv2.CV_64F, 0, 1, ksize=3)
    sob = cv2.magnitude(sx, sy)
    sob = np.uint8(np.clip(sob, 0, 255))
    processed = cv2.cvtColor(sob, cv2.COLOR_GRAY2BGR)
    show_image(processed)
def laplacian():
    global processed
    if original is None:
        return
    gray = cv2.cvtColor(original, cv2.COLOR_BGR2GRAY)
    lap = cv2.Laplacian(gray, cv2.CV_64F)
    lap = np.uint8(np.absolute(lap))
    processed = cv2.cvtColor(lap, cv2.COLOR_GRAY2BGR)
    show_image(processed)
def canny():
    global processed
    if original is None:
        return
    gray = cv2.cvtColor(original, cv2.COLOR_BGR2GRAY)
    edges = cv2.Canny(gray, 100, 200)
    processed = cv2.cvtColor(edges, cv2.COLOR_GRAY2BGR)
    show_image(processed)
def reset():
    global processed
    if original is None:
        return
    processed = original.copy()
    show_image(processed)
def save():
    if processed is None:
        return
    path = filedialog.asksaveasfilename(
        defaultextension=".jpg",
        filetypes=[("JPEG", ".jpg"), ("PNG", ".png")]
    )
    if path:
        cv2.imwrite(path, processed)
        messagebox.showinfo("Saved", "Image Saved Successfully!")
root = Tk()
root.title("Interactive Image Processing Application")
root.geometry("900x650")
image_label = Label(root)
image_label.pack(pady=10)
frame = Frame(root)
frame.pack()
Button(frame, text="Upload Image", width=15, command=upload_image).grid(row=0, column=0, padx=5, pady=5)
Button(frame, text="Gaussian Blur", width=15, command=gaussian).grid(row=0, column=1, padx=5, pady=5)
Button(frame, text="Median Blur", width=15, command=median).grid(row=0, column=2, padx=5, pady=5)
Button(frame, text="Sobel", width=15, command=sobel).grid(row=1, column=0, padx=5, pady=5)
Button(frame, text="Laplacian", width=15, command=laplacian).grid(row=1, column=1, padx=5, pady=5)
Button(frame, text="Canny", width=15, command=canny).grid(row=1, column=2, padx=5, pady=5)
Button(frame, text="Reset", width=15, command=reset).grid(row=2, column=0, padx=5, pady=5)
Button(frame, text="Save Image", width=15, command=save).grid(row=2, column=1, padx=5, pady=5)
Button(frame, text="Exit", width=15, command=root.destroy).grid(row=2, column=2, padx=5, pady=5)
root.mainloop()