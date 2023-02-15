#!/usr/bin/env python
# coding: utf-8

# In[1]:


import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox
from tkinter import Text
from PIL import Image, ImageTk
import pytesseract

root = tk.Tk()
root.geometry("1024x720")
root.title("Image to Text Converter")

def open_file():
    file_path = filedialog.askopenfilename()
    display_image(file_path)
    text = pytesseract.image_to_string(Image.open(file_path))
    display_text(text)

def display_image(file_path):
    global panel
    image = Image.open(file_path)
    image = image.resize((250, 250), Image.LANCZOS)
    image = ImageTk.PhotoImage(image)
    
    if panel is None:
        panel = tk.Label(image_frame, image=image)
        panel.image = image
        panel.pack(side="left", padx=10, pady=10)
    else:
        panel.configure(image=image)
        panel.image = image

def display_text(text):
    extracted_text.delete("1.0", tk.END)
    extracted_text.insert("1.0", text)

def zoom_in():
    pass

def zoom_out():
    pass

def reset_image():
    pass

image_frame = tk.Frame(root, bg="#dddddd")
image_frame.pack(side="left", padx=10, pady=10)

display_frame = tk.Frame(root, bg="#dddddd")
display_frame.pack(side="right", padx=10, pady=10)

select_image = tk.Button(root, text="Select Image", command=open_file)
select_image.pack(pady=10)

zoom_in_button = tk.Button(image_frame, text="Zoom In", command=zoom_in)
zoom_in_button.pack(side="bottom", pady=10)

zoom_out_button = tk.Button(image_frame, text="Zoom Out", command=zoom_out)
zoom_out_button.pack(side="bottom", pady=10)

reset_button = tk.Button(image_frame, text="Reset Image", command=reset_image)
reset_button.pack(side="bottom", pady=10)

extracted_text = Text(display_frame, height=35, width=50)
extracted_text.pack(fill="both", expand=True)

panel = None

root.mainloop()


# In[ ]:




