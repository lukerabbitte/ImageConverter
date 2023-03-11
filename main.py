from tkinter import *
from tkinter import filedialog
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