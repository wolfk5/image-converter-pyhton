import os
from tkinter import *
from tkinter import filedialog
from PIL import Image, ImageTk, ImageFilter, ImageOps

# Create folders for different image types
if not os.path.exists('jpeg'):
    os.makedirs('jpeg')
if not os.path.exists('png'):
    os.makedirs('png')
if not os.path.exists('thumbnails_200'):
    os.makedirs('thumbnails_200')
if not os.path.exists('thumbnails_400'):
    os.makedirs('thumbnails_400')
if not os.path.exists('thumbnails_600'):
    os.makedirs('thumbnails_600')
if not os.path.exists('rotation'):
    os.makedirs('rotation')
if not os.path.exists('black_and_white'):
    os.makedirs('black_and_white')

# Create main window
root = Tk()
root.title("Image Editor")

# Function to open file dialog and select images
def open_image():
    # Select files to open
    filetypes = (("JPEG files", "*.jpg"), ("PNG files", "*.png"), ("All files", "*.*"))
    filenames = filedialog.askopenfilenames(initialdir="./", title="Select image file", filetypes=filetypes)
    
    # Show selected images
    global images
    images = []
    for i in range(len(filenames)):
        image = Image.open(filenames[i])
        images.append(image)
        photo = ImageTk.PhotoImage(image)
        image_label = Label(image=photo)
        image_label.photo = photo
        image_label.grid(row=0, column=i+1)
        
# Function to save images as PNG
def save_as_png():
    for i in range(len(images)):
        png_path = os.path.join('png', os.path.basename(filenames[i])[:-4] + '.png')
        images[i].save(png_path)
        
# Function to create thumbnails
def create_thumbnail(size):
    for i in range(len(images)):
        thumbnail = images[i].copy()
        thumbnail.thumbnail((size, size))
        thumbnail_path = os.path.join('thumbnails_{}'.format(size), os.path.basename(filenames[i]))
        thumbnail.save(thumbnail_path)
        
# Function to rotate images
def rotate_image():
    try:
        angle = int(angle_entry.get())
        for i in range(len(images)):
            rotated_image = images[i].rotate(angle, expand=True)
            rotated_image_path = os.path.join('rotation', os.path.basename(filenames[i]))
            rotated_image.save(rotated_image_path)
    except ValueError:
        messagebox.showerror("Error", "Please enter a valid angle (integer)")
        
# Function to convert images to black and white
def convert_to_bw():
    for i in range(len(images)):
        bw_image = ImageOps.grayscale(images[i])
        bw_image_path = os.path.join('black_and_white', os.path.basename(filenames[i]))
        bw_image.save(bw_image_path)
        

def blur_image():
    try:
        radius = int(radius_entry.get())
        for i in range(len(images)):
            blurred_image = images[i].filter(ImageFilter.GaussianBlur(radius=radius))
            blurred_image_path = os.path.join('jpeg', os.path.basename(filenames[i]))
            blurred_image.save(blurred_image_path)
    except ValueError:
        messagebox.showerror("Error", "Please enter a valid blur radius (integer)")
        

def change_image_feature():
    for i in range(len(images)):
        brightness = brightness_slider.get()
        adjusted_image = ImageOps.autocontrast(images[i], cutoff=brightness)

choose = int(input('put number to choose which image to show'))

if (choose == 1):
    image1 = Image.open('khuaaoxanh.jpg')
    image1.show()
    while (choose == 1):
        converttype = int(input('put number to choose type of converter'))
        if (converttype == 1):
            save_as_png()
            break
        

