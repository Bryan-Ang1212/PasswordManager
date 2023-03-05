from tkinter import *
from tkinter import messagebox
from random import randint, choice, shuffle
import pyperclip
import json
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

def generate_password():
    password_input.delete(0, END)
    password_letter = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = password_numbers + password_symbols + password_letter
    shuffle(password_list)

    password = "".join(password_list)
    password_input.insert(0, password)
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def add():
    email = email_input.get()
    password = password_input.get()
    website = website_input.get()
    new_data = {
        website: {
            "email": email,
            "password": password,
        }
    }

    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title="Oops", message="Please make sure you haven't left any fields empty.")
    else:
        # is_ok = messagebox.askokcancel(title=website, message=f"These are the details entered: \nEmail: {email} \n"
        #                                               f"Password: {password} \nIt is okay to save?")
        # if is_ok:

        try:
            with open("data.json", mode="r") as data_file:
                # data.write(f"{website} / {email} / {password} \n")
                # Reading old data
                data = json.load(data_file)
        except FileNotFoundError:
            with open("data.json", mode="w") as data_file:
                json.dump(new_data, data_file, indent=4)
        else:
            # updating old data with new data
            data.update(new_data)

            with open("data.json", mode="w") as data_file:
                # saving updata data
                json.dump(data, data_file, indent=4)
        finally:
            website_input.delete(0, END)
            password_input.delete(0, END)


# ---------------------------- FIND PASSWORD ------------------------------- #
def find_password():
    # try:
    #     with open("data.json", mode="r") as data_file:
    #         data = json.load(data_file)
    #         search_value = data[website_input.get()]
    #         messagebox.showinfo(title=website_input.get(), message=f"Email: {search_value['email']} "
    #                                                                f"\nPassword: {search_value['password']}")
    # except FileNotFoundError:
    #     messagebox.showinfo(title="Oops", message=f"No Data File Found")
    # except KeyError:
    #     messagebox.showinfo(title="Oops", message=f"No detail for the {website_input.get()} exist")
    try:
        website = website_input.get()
        with open("data.json", mode="r") as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        messagebox.showinfo(title="Error", message="No Data File Found")
    else:
        if website in data:
            email = data[website]["email"]
            password = data[website]["password"]
            messagebox.showinfo(title=website, message=f"Email: {email}\nPassword: {password}")
        else:
            messagebox.showinfo(title="Error", message=f"No detail for the {website} exist")


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("My Password Manager")
window.config(padx=50, pady=50, bg=YELLOW)

canvas = Canvas(width=200, height=200, bg=YELLOW, highlightthickness=0)
lock_image = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=lock_image)
canvas.grid(column=1, row=0)

# label
website_label = Label(text="Website:", bg=YELLOW)
website_label.grid(column=0, row=1)
# website_label.focus()
email_username_label = Label(text="Email/UserName:", bg=YELLOW)
email_username_label.grid(column=0, row=2)
password_label = Label(text="Password:", bg=YELLOW)
password_label.grid(column=0, row=3)

# Entry
website_input = Entry(width=35)
website_input.grid(column=1, row=1)
email_input = Entry(width=53)
email_input.grid(columnspan=2, column=1, row=2)
email_input.insert(0, "Bryan0917ang@gmail.com")
password_input = Entry(width=35)
password_input.grid(column=1, row=3)

# Button
generate_button = Button(text="Generate Password", command=generate_password, bg=GREEN)
generate_button.grid(column=2, row=3)
add_button = Button(text="Add", width=45, command=add)
add_button.grid(columnspan=2, column=1, row=4)
search_button = Button(text="Search", width=14, command=find_password)
search_button.grid(column=2, row=1,)

window.mainloop()
