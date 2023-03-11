from tkinter import *
from tkinter import filedialog, font

import tkinter as tk
from PIL import Image
from PIL import ImageTk


# Create a function to convert the image to the desired format
def convert_image(file_path, format):
    image = Image.open(file_path)
    new_file_path = file_path.split('.')[0] + '.' + format
    image.save(new_file_path)


# Create a function to handle the button click event
def browse_file():
    file_path = filedialog.askopenfilename()
    return file_path


# Create a function to handle the conversion event
def convert_file():
    file_path = browse_file()
    format = format_var.get()
    convert_image(file_path, format)
    status_label.config(text="File converted successfully!")


# Create a Tkinter window
window = Tk()
window.geometry('600x400')
window.title('Convert that image')

# Format Tkinter window
font = font.Font(family="Consolas", size=12)

# Create a frame to hold the buttons
button_frame = tk.Frame(window)
button_frame.pack()

# Create the buttons
button1 = tk.Button(button_frame, text="Button 1", font=font,
                     relief="flat", borderwidth=0, command=lambda: animate(button1, button2))
button1.config(bg="lightgray", activebackground="gray")

button2 = tk.Button(button_frame, text="Button 2", font=font,
                     relief="flat", borderwidth=0, command=lambda: animate(button1, button2))
button2.config(bg="lightgray", activebackground="gray")

# Pack the buttons
button1.pack(side="left", padx=10)
button2.pack(side="left", padx=10)

def animate(button1, button2):
    # Create a subtle animation
    for i in range(2):
        button1.config(bg="gray")
        button1.update()
        button1.config(bg="lightgray")
        button1.update()

        button2.config(bg="gray")
        button2.update()
        button2.config(bg="lightgray")
        button2.update()

# Create a label for the file format selection
format_label = Label(window, text="Select your target format:")
format_label.pack()

# Create a variable to store the selected format
format_var = StringVar(window)
format_var.set('png')

# Create a dropdown menu for the target format
format_dropdown = OptionMenu(window, format_var, 'png', 'jpg', 'jpeg', 'gif')
format_dropdown.pack()

# Create a button to browse for the image file
browse_button = Button(window, text="Select File", command=browse_file)
browse_button.pack()

# Create a button to convert the image file
convert_button = Button(window, text="Convert File", command=convert_file)
convert_button.pack()

# Create a label to display the status of the conversion
status_label = Label(window, text="")
status_label.pack()

# Start the Tkinter event loop
window.mainloop()