import math
import random
import os
import time
import re
from datetime import datetime
import os.path
import tkinter as tk
from tkinter import messagebox

#dont touch
dateTimeObj = datetime.now()
timestampStr = dateTimeObj.strftime("%d-%b-%Y (%H:%M:%S)")

#dont touch, unless you want to change the name of the file and location it is stored at. make sure to include the \\ in the path, or else will brokey
save_path = 'C:\\Users\\hugs4\\Desktop'
name_of_file = "saved_passwords"
completeName = os.path.join(save_path, name_of_file+".txt")      

# Create a tkinter window
root = tk.Tk()
root.title("Password Generator")
root.geometry("800x500")  # Adjusted the height for a better look
root.configure(background='#f0f0f0')  # Light gray background

# Make the window non-resizable
root.resizable(width=False, height=False)

# Create a label for the title
title_label = tk.Label(root, text="Password Generator", font=("Helvetica", 24, "bold"), bg='#f0f0f0')
title_label.pack(pady=(10, 0))

# Create a frame to hold the password settings
settings_frame = tk.Frame(root, bg='#f0f0f0')
settings_frame.pack(pady=(10, 20))

# Create a label for the password length
length_label = tk.Label(settings_frame, text="Password Length:", font=("Helvetica", 12), bg='#f0f0f0')
length_label.grid(row=0, column=0, padx=(10, 5), pady=(5, 0), sticky=tk.E)

# Create a slider for the user to choose the length of the password
slider = tk.Scale(settings_frame, from_=8, to=256, orient=tk.HORIZONTAL, length=300,
                  font=("Helvetica", 12), bg='#f0f0f0', highlightthickness=0)

slider.grid(row=0, column=1, padx=(5, 5), pady=(5, 0), sticky=tk.W)

# Create a frame to hold the checkboxes
checkbox_frame = tk.Frame(settings_frame, bg='#f0f0f0')
checkbox_frame.grid(row=1, columnspan=2, padx=(10, 0), pady=(0, 5), sticky=tk.W)

# Create a checkbox for the user to choose if they want to use special characters
special_characters = tk.IntVar(value=1)  # Set initial value to 1 (checked)
checkbox = tk.Checkbutton(checkbox_frame, text="Special Characters", variable=special_characters,
                          font=("Helvetica", 12), bg='#f0f0f0')
checkbox.pack(side=tk.LEFT, padx=(0, 5))

# Create a checkbox for the user to choose if they want to use numbers
numbers = tk.IntVar(value=1)  # Set initial value to 1 (checked)
checkbox = tk.Checkbutton(checkbox_frame, text="Numbers", variable=numbers, font=("Helvetica", 12), bg='#f0f0f0')
checkbox.pack(side=tk.LEFT, padx=(0, 5))

# Create a checkbox for the user to choose if they want to use uppercase letters
uppercase = tk.IntVar(value=1)  # Set initial value to 1 (checked)
checkbox = tk.Checkbutton(checkbox_frame, text="Uppercase Letters", variable=uppercase,
                          font=("Helvetica", 12), bg='#f0f0f0')
checkbox.pack(side=tk.LEFT, padx=(0, 5))

# Create a checkbox for the user to choose if they want to use lowercase letters
lowercase = tk.IntVar(value=1)  # Set initial value to 1 (checked)
checkbox = tk.Checkbutton(checkbox_frame, text="Lowercase Letters", variable=lowercase,
                          font=("Helvetica", 12), bg='#f0f0f0')
checkbox.pack(side=tk.LEFT)
checkbox.pack(side=tk.LEFT)

def saveMessageBox():
    messagebox.showinfo("Password Saved", "Your password has been saved in a text file on your desktop. If you use generate another password, your previous passwords will not be overwritten, just added to the bottom of the last password.")
    f = open(completeName, "a")
    f.write("\n=============================================\nPassword generated: " +  str(password_text.get("1.0", "end-1c")) + "\n\nAt: " + str(timestampStr) + "\n\n")
    f.close()

# Define the generate_password function
def generate_password():
    # Check if no checkboxes are selected
    if (special_characters.get() + numbers.get() + uppercase.get() + lowercase.get()) == 0:
        label4.pack(side=tk.BOTTOM, fill=tk.X)  # Show the label
        password_text.delete(1.0, tk.END)  # Clear the Text widget
        return  # Return early if no checkboxes are selected

    #create a list of all the characters that the user can choose from
    characters = []
    if special_characters.get() == 1:
        characters.extend(list("!@#$%^&*()_+"))
    if numbers.get() == 1:
        characters.extend(list("0123456789"))
    if uppercase.get() == 1:
        characters.extend(list("ABCDEFGHIJKLMNOPQRSTUVWXYZ"))
    if lowercase.get() == 1:
        characters.extend(list("abcdefghijklmnopqrstuvwxyz"))

    #create a variable to store the password
    password = ""

    #create a variable to store the length of the password
    length = slider.get()

    #create a for loop to generate the password
    for i in range(length):
        password += random.choice(characters)

    # Set the password in the Text widget
    password_text.config(state=tk.NORMAL)  # Enable editing temporarily
    password_text.delete(1.0, tk.END)  # Clear previous content
    password_text.insert(tk.END, password)
    password_text.config(state=tk.DISABLED)  # Disable editing

    #create a variable to store the clipboard
    root.clipboard_clear()
    root.clipboard_append(password)

    # Show the label when password is generated
    label4.pack(side=tk.BOTTOM, fill=tk.X)

# Create a frame to hold the buttons
button_frame = tk.Frame(root, bg='#f0f0f0')
button_frame.pack(pady=(5, 0), fill=tk.X, expand=True)

# Create a button to generate the password
generate_button = tk.Button(settings_frame, text="Generate Password", command=generate_password,
                            font=("Helvetica", 12), bg='#1e88e5', fg='#ffffff', padx=10)
generate_button.grid(row=2, columnspan=2, pady=(5, 0))  # Adjusted pady

saveButton = tk.Button(root, text="Save Password", command=saveMessageBox)
saveButton.pack()


# Configure resizing of elements
button_frame.grid_rowconfigure(0, weight=1)
button_frame.grid_columnconfigure(0, weight=1)

# Create a Text widget for displaying the password
password_text = tk.Text(root, wrap=tk.WORD, font=("Helvetica", 16), bg="#ffffff", fg="#333333", height=5,
                       width=50, state=tk.DISABLED)  # Set state to DISABLED
password_text.pack(fill=tk.BOTH, expand=True, padx=(10, 10), pady=(5, 0))  # Adjusted pady

# Create a label saying that the password has been copied to the clipboard
label4 = tk.Label(root, text="Your password has been copied to the clipboard", font=("Helvetica", 12),
                  bg="#f0f0f0", fg="#1e88e5")

label4.pack_forget()  # Hide the label initially

# Configure resizing of elements
root.grid_rowconfigure(2, weight=1)
root.grid_columnconfigure(0, weight=1)

# Run the window when the program is run
root.mainloop()
