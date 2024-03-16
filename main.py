from tkinter import *                                # import tkinter lib
from tkinter import messagebox                       # import messagebox module from tkinter lib
from random import randint, choice, shuffle          # import random integer, random choice and shuffle from random
import json
# import pyperclip                                   # optional lib to allow copying to the clipboard
# -----------------------------------CONSTANTS----------------------------------- #
MIN_NUMBER_LETTERS = 8                               # min number of letters to include in the password
MAX_NUMBER_LETTERS = 10                              # max number of letters to include in the password
MIN_NUMBER_NUMBERS = 2                               # min number of numbers to include in the password
MAX_NUMBER_NUMBERS = 4                               # max number of letters to include in the password
MIN_NUMBER_SYMBOLS = 2                               # min number of symbols to include in the password
MAX_NUMBER_SYMBOLS = 4                               # min number of symbols to include in the password
DEFAULT_EMAIL = "default@email.com"                  # default email to be prefilled in the username/email field

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    """function that generates a random password and displays it in the password field"""

    # created lists to contain the possible characters to be included in the password
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password = []            # empty password list to contain the added password characters

    password += [choice(letters) for _ in range(randint(MIN_NUMBER_LETTERS, MAX_NUMBER_LETTERS))] # adding to the password random letters based on the chosen min and max values
    password += [choice(symbols) for _ in range(randint(MIN_NUMBER_SYMBOLS, MAX_NUMBER_SYMBOLS))] # adding to the password random symbols based on the chosen min and max values
    password += [choice(numbers) for _ in range(randint(MIN_NUMBER_NUMBERS, MAX_NUMBER_NUMBERS))] # adding to the password random numbers based on the chosen min and max values

    shuffle(password)      # shuffling the order of the password characters

    password_string = "".join(password)      # creating the final password string based on the password list
    password_entry.insert(0, password_string) # inserting the generated password in the password entry field
    # pyperclip.copy(password_string)   # OPTIONAL: copying the generated password to the clipboard using pyperclip lib

# ---------------------------- SAVE PASSWORD ------------------------------- #


def add_password():
    """function that appends the website, username/email and generated password to the data file after users confirmation and shows a warning in case of a missing field"""
    website = website_entry.get().capitalize()       # storing the string from website_entry in website variable
    username = username_entry.get()     # storing the string from username_entry in username variable
    password = password_entry.get()     # storing the string from password_entry in password variable
    new_data = {
        website:
            {
                "email": username,
                "password": password
            }
    }
    if len(password) == 0 or len(website) == 0 or len(username) == 0:   # verifying that all fields have values
        messagebox.showwarning(title = "Error!", message= "Please fill all the fields")  # showing an error message in case on an empty field
    else:  # else condition (all fields are filled)
        is_ok = messagebox.askokcancel(title=f"Add Password? for {website}",
                                       message=f"There are the details that you entered: \nEmail: {username}\nPassword: {password}\nDo you want to save? Confirm by clicking OK")
        # asking for user's confirmation and storing it in is_ok variable
        if is_ok:    # saving the password to the data file based on user's response
            try:
                with open("data.json","r") as data_file:             # opening the data file in read mode
                    data = json.load(data_file)                      # reading old data
            except FileNotFoundError:
                with open("data.json", "w") as data_file:            # opening the data file in write mode
                    json.dump(new_data, data_file, indent= 4)        # saving new data to the JSON file
            else:
                data.update(new_data)                                # updating old data with new data
                with open("data.json", "w") as data_file:            # opening the data file in write mode
                    json.dump(data, data_file, indent= 4)            # saving updated data to the JSON file
            finally:
                website_entry.delete(0, END)                # clearing the website entry
                password_entry.delete(0,END)                # clearing the password entry

# ---------------------------- SAVE PASSWORD ------------------------------- #


def find_password():
    """function that searches for saved password in the data file and displays the saved credentials or an error"""
    website = website_entry.get().capitalize()  # storing the string from website_entry in website variable
    try:
        with open("data.json", "r") as data_file:  # opening the data file in read mode
            data = json.load(data_file)  # reading old data
    except FileNotFoundError:   # exception in case data.json does not exit
        messagebox.showinfo(title="Error!", message="File data not found!")   # display error message
    else:
        if website in data:                         # check if there are saved credentials for the specified website
            email = data[website]['email']          # variable to store the email/username value saved for the specified website
            password = data[website]['password']    # variable to store the password value saved for the specified website
            messagebox.showinfo(title=website, message=f"Email: {email}\nPassword: {password}")   # displaying the saved credentials for the specified website
        else:      # else statement to be triggered in case there are no saved credentials for the saved website
            messagebox.showinfo(title="Error!", message="No data for the specified website!")   # display error message


# ---------------------------- UI SETUP ------------------------------- #


window = Tk()                     # creating a window
window.title("Password Manager")  # setting the window title
window.config(padx=50, pady=50, bg="white")  # setting window background color and padding for x-axis and y-axis

# Setting fixed dimensions for columns
window.grid_columnconfigure(0, minsize=100)  # Setting a fixed width for column 0
window.grid_columnconfigure(1, minsize=120)  # Setting a fixed width for column 1
window.grid_columnconfigure(2, minsize=80)  # Setting a fixed width for column 2

canvas = Canvas(width=200, height=200, bg="white", highlightthickness=0)  # creating a canvas for the image and setting dimension and colors
image_file = PhotoImage(file="logo.png")                       # setting the desired image path
canvas.create_image(100,100, image=image_file)           # loading the image into the canvas
canvas.grid(column= 1, row=0)                                  # choosing alignment in the grid


# create the website label
website_label = Label(text="Website:", bg="white", width=21,pady=5)
website_label.grid(column=0, row=1)   # choosing alignment in the grid

# create the email/username label
username_label = Label(text="Email/Username:", bg="white")
username_label.grid(column=0, row=2)  # choosing alignment in the grid

# create the password label
password_label = Label(text="Password:", bg="white",pady=5)
password_label.grid(column=0, row=3)  # choosing alignment in the grid

# create the website entry
website_entry = Entry(width= 40)
website_entry.focus()    # using the focus function to start with a cursor in the website entry
website_entry.grid(column=1, row=1)  # choosing alignment in the grid

# create the username entry
username_entry = Entry(width=60)
username_entry.insert(0, DEFAULT_EMAIL)         # inserting the DEFAULT_EMAIL as a prefilled value for the username entry field
username_entry.grid(column=1, row=2, columnspan = 2)  # choosing alignment in the grid

# create the password entry
password_entry = Entry(width= 40)
password_entry.grid(column=1, row=3)   # choosing alignment in the grid

# create the generate button and assign it to the generate_password function
generate_button = Button(text="Generate Password", bg="white", command=generate_password, width=15)
generate_button.grid(column=2, row=3)   # choosing alignment in the grid

# create the search button and assign it to the generate_password function
search_button = Button(text="Search", bg="white", command=find_password, width=15)
search_button.grid(column=2, row=1)   # choosing alignment in the grid

# create the add button and assign it to the add_password function
add_button = Button(text="Add", width=50, bg="white", command=add_password)
add_button.grid(column=1, row=4, columnspan=2)    # choosing alignment in the grid

window.mainloop()   # main loop to keep the window from closing
