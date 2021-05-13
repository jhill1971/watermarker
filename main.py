# Image Watermarking Program
# 2021 James Hill

# You will need a watermark.png in the CWD for this to work, or add an absolute path to your watermark image.

# import necessary modules
from tkinter import *
import time


def add_watermark(input_path, output_path, watermarked_image_path, position):
    from PIL import Image
    """Takes the users input and creates a new file with the watermarked image"""
    start_image = Image.open(input_path)
    watermark = Image.open(watermarked_image_path)

    # add watermark to image
    start_image.paste(watermark, position)
    start_image.show()
    start_image.save(output_path)


def get_info():
    """Get necessary info and call add-watermark function"""
    img = e1.get()
    img = str(img)
    print(img)
    wimg = ("watermarked" + img)
    add_watermark(img, wimg, 'watermark.png', position=(100, 100))


# UI Setup
# Window
window = Tk()
window.title("Photo File Path")
window.config(padx=25, pady=50)
Label(window, text="Enter the path to the photo you want to watermark:").grid(row=0, column=0)
# Data Entry
e1 = Entry(window, width=55)
e1.grid(row=0, column=1)
# Button
go = Button(text="Go", command=get_info)
go.grid(column=0, row=1, sticky="w")
# Close input window after 15 seconds
window.after(15000, window.destroy)
window.mainloop()
