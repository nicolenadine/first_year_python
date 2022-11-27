from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip
import json


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
               'n',
               'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A',
               'B',
               'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O',
               'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_list = []

    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = password_letters + password_symbols + password_numbers
    shuffle(password_list)

    random_password = "".join(password_list)
    password_entry.insert(0, random_password)
    pyperclip.copy(random_password)  # copy generated password to clipboard


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_password():
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()
    new_entry = {
        website: {
            "email": email,
            "password": password,
        }
    }

    if len(website) == 0 or len(email) == 0 or len(password) == 0:
        messagebox.showinfo(title="Oops", message="Please make sure you "
                                                  "haven't left any fields "
                                                  "blank")
    else:
        try:
            with open("passwords.json", "r") as password_file:
                # Read existing file
                add_password = json.load(password_file)
        except FileNotFoundError:
            with open("passwords.json", "w") as password_file:
                json.dump(new_entry, password_file, indent=4)
        except json.decoder.JSONDecodeError:     # File empty
            with open("passwords.json", "w") as password_file:
                json.dump(new_entry, password_file, indent=4)
        else:
            # Update data in json file.
            add_password.update(new_entry)

            with open("passwords.json", "w") as password_file:
                # Save new password entry to json file
                json.dump(add_password, password_file, indent=4)
        finally:
            # Clear user input to make room for a new entry
            website_entry.delete(0, END)
            password_entry.delete(0, END)


# ---------------------------- SEARCH FOR PASSWORD -------------------- #
def find_password():
    website = website_entry.get()
    with open("passwords.json") as password_file:
        password_list = json.load(password_file)
        if website in password_list:
            email = password_list[website]["email"]
            password = password_list[website]["password"]
            messagebox.showinfo(title="Success", message=f"Here is the login "
                                                         f"info for "
                                                         f"{website}\n Email: {email}\n "
                                                         f"Password:"
                                                         f" {password}")

        else:  # Entry not found
            messagebox.showinfo(title="Error", message=f"No entry matching "
                                               f"{website} found in "
                                               f"password manager")


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(height=200, width=200)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(row=0, column=1)

# Labels
website_label = Label(text="Website:")
website_label.grid(row=1, column=0)
email_label = Label(text="Email/Username:")
email_label.grid(row=2, column=0)
password_label = Label(text="Password:")
password_label.grid(row=3, column=0)

# Entries
website_entry = Entry(width=21)
website_entry.grid(row=1, column=1)
website_entry.focus()
email_entry = Entry(width=35)
email_entry.grid(row=2, column=1, columnspan=2)
# email_entry.insert(0, "fivepennies88@gmail.com")  optional auto populate common email
password_entry = Entry(width=21)
password_entry.grid(row=3, column=1)

# Buttons
search_passwords_button = Button(text="Search", width=13,
                                 command=find_password)
search_passwords_button.grid(row=1, column=2)
generate_password_button = Button(text="Generate Password",
                                  command=generate_password)
generate_password_button.grid(row=3, column=2)
add_button = Button(text="Add", width=36, command=save_password)
add_button.grid(row=4, column=1, columnspan=2)

window.mainloop()
