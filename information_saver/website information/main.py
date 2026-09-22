from tkinter import  *
from tkinter import messagebox
import json
import random


#saving function
def saving():
    # get what was entered
    web_infor = website_entries.get()
    email_infor = email_entries.get()
    password_infor = password_entries.get()

    # information in a dict
    infor_dic = {web_infor: {
        "email": email_infor,
        "password": password_infor
    }
    }

    try:
            # adding more data in the json file since it means it is not the first time adding information since the .json file exist already
            # reading the json file
            with open("information.json","r") as file:
                data = json.load(file)
                # updating with the new information
                data.update(infor_dic)
                # writing the new information in the json file
                if web_infor == "" or email_infor =="" or password_infor =="":
                    messagebox.showerror(title="Empty field",message="Don't leave any field empty")
                else:
                    with open("information.json", "w") as file:
                        json.dump(data, file, indent=6)
                        messagebox.showinfo(title="Success save ", message=f"Your information of {web_infor} with  \n Email : {email_infor}  \n password : {password_infor} \n is saved successfully")
    except FileNotFoundError:
        with open("information.json", "w") as file:
            # write in the json file
            if web_infor == "" or email_infor == "" or password_infor == "":
                messagebox.showerror(title="Empty field", message="Don't leave any field empty")
            else:
                json.dump(infor_dic, file, indent=6)
                messagebox.showinfo(title="Success save ",message=f"Your information of {web_infor} with  \n Email : {email_infor}  \n password : {password_infor} \n is saved successfully")
    finally:
        website_entries.delete(0,END)
        email_entries.delete(0, END)
        password_entries.delete(0, END)



#searching function
def searching ():
    web_infor = website_entries.get()
    if web_infor =="":
        messagebox.showerror(title="Empty field",message="You have to write the website name for the information you are looking for")
    else:
        try:
            with open("information.json") as file:
                data=json.load(file)
                found_email=data[web_infor]["email"]
                found_password = data[web_infor]["password"]
                messagebox.showinfo(title="Here you go",message=f"your email: {found_email}  \n password: {found_password}")
                website_entries.delete(0,END)
        except KeyError:
            messagebox.showerror(title="Not found",message=f"There is no information for {web_infor} try again")
            website_entries.delete(0, END)


#generating password function
alphabetical_characters = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
    'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
    'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
    'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'
]
numbers=['0', '1', '2', '3', '4', '5', '6', '7', '8','9']

symbols = [
    '!', '@', '#', '$', '%', '^', '&', '*', '(', ')',
    '-', '_', '+', '=', '[', ']', '{', '}', '|', '\\',
    ';', ':', "'", '"', ',', '.', '/', '<', '>', '?', '~', '`'
]
def generating ():
    char_num=random.randint(3,6)
    numbers_num=random.randint(2,4)
    symbols_num=random.randint(2,4)

    #generating the password
    #generating for alphabet letters
    all_char = ""
    for char in range(char_num):
        random_char=random.choice(alphabetical_characters)
        all_char = all_char + random_char
    #generating for numbers
    all_num = ""
    for num in range(numbers_num):
        random_num=random.choice(numbers)
        all_num=all_num + random_num
    #generating symbol
    all_symbols = ""
    for symbol in range(symbols_num):
       random_symbol= random.choice(symbols)
       all_symbols = all_symbols + random_symbol

    #whole_generated password
    whole_password =all_char +all_num + all_symbols
    password_entries.delete(0,END)
    password_entries.insert(index=0,string=whole_password)



#interface
my_window = Tk()
my_window.minsize(width=500,height=500)



#canvas
canvas = Canvas(width=200,height=200)
lock=PhotoImage(file="./logo.png")
canvas.create_image(100,100,image=lock)
canvas.grid(row=0,column=1)

#labels
website_label = Label(text="Website:")
website_label.grid(row=1,column=0)
Email_label = Label(text="Email:")
Email_label.grid(row=2,column=0)
password_label = Label(text="Password:")
password_label.grid(row=3,column=0)

#entries
website_entries = Entry(width=16)
website_entries.grid(row=1,column=1)
email_entries = Entry(width=32)
email_entries.grid(row=2,column=1,columnspan=2)
password_entries = Entry(width=16)
password_entries.grid(row=3,column=1)



#button
search_button= Button(text="Search",command=searching)
search_button.grid(row=1,column=3)
generate_password = Button(text="generate password",command=generating)
generate_password.grid(row=3,column=2)
add_button = Button(text="Add",command=saving)
add_button.grid(row=4,column=1)




my_window.mainloop()