import os
from PIL import Image, ImageTk
import tkinter as tk

# set the path to the folder containing the images
folder_path = "images"

# create a list to store the PhotoImage objects
photo_list = []

# define a function to create a new window and display the image
def open_image_window(index):
    # create a new window and label to display the image
    image_window = tk.Toplevel()
    image_label = tk.Label(image_window, image=photo_list[index])
    image_label.pack()

    # create a button to reopen the window
    reopen_button = tk.Button(image_window, text="Reopen", command=lambda: open_image_window(index))
    reopen_button.pack()

# create the main Tkinter window
root = tk.Tk()

# loop through all the files in the folder
for filename in os.listdir(folder_path):
    # check if the file is an image file
    if filename.endswith(".jpeg") or filename.endswith(".png"):
        # load the image using PIL
        image_path = os.path.join(folder_path, filename)
        image = Image.open(image_path)

        # create a PhotoImage object from the image
        photo = ImageTk.PhotoImage(image)

        # add the PhotoImage object to the list
        photo_list.append(photo)

        # create a label to display the image
        label = tk.Label(root, image=photo)
        label.pack()

        # create a button to open a new window with the same image
        button = tk.Button(root, text="Open in new window", command=lambda index=len(photo_list)-1: open_image_window(index))
        button.pack()

# start the main event loop
root.mainloop()
