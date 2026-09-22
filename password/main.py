from tkinter import *
from  tkinter import messagebox
import random
import json

symbols = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '_', '+', '=', '[', ']', '{', '}', '|', '\\', ';', ':', '\'', '"', ',', '<', '.', '>', '/', '?']
all_chars_list = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm','n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
numbers=['1', '2', '3', '4', '5', '6', '7', '8', '9', '10']

#function to write the entered information in a .txt file
def writing():
    # getting what was entered
    website_message = website_entry.get()
    email_message = email_entry.get()
    password_message = password_entry.get()

    if website_message == "" or email_message == "" or password_message == "":
        messagebox.showerror(message="please dont leave any field empty")
    else:
        inform_dict={website_message:{
            "email":email_message,
            "password":password_message }
        }

        try:
            with open("information.json", mode="r") as data:
                #reading the file
                updating=json.load(data)
                #updating the file with new data
                updating.update(inform_dict)
                #writing the new data
                with open("information.json", mode="w") as data:
                    json.dump( updating,data,indent=4)
        except FileNotFoundError:
            with open("information.json", mode="w") as data:
                json.dump(inform_dict, data)
        finally:
                website_entry.delete(0,END)
                email_entry.delete(0, END)
                password_entry.delete(0, END)
                messagebox.showinfo(message=f"website: {website_message} \n email:{email_message} \n password:{password_message} \n"
                                            f"has been saved successfully saved")

#function to generate password
def generate_password():
    nr_letters=random.randint(8,10)
    nr_symbols=random.randint(2,4)
    nr_number = random.randint(2, 4)

    password=[]

    for char in range(nr_letters):
        password.append(random.choice(all_chars_list))
    for char in range(nr_symbols):
        password+=random.choice(symbols)
    for char in range(nr_number):
        password+=random.choice(numbers)
    random.shuffle(password)
    password_in_char=""
    for pas in password:
        password_in_char=password_in_char+pas
    password_entry.insert(END,string=password_in_char,)

def searching ():
    website_message = website_entry.get()

    with open("information.json") as data_file:
        infor_in=json.load(data_file)
        try:
            email_in= infor_in[website_message]["email"]
            password_in = infor_in[website_message]["password"]

            messagebox.showinfo(message=f"your information are  \n"
                                        f"email {email_in} ,\n"
                                        f"password is {password_in}")
            website_entry.delete(0,END)
        except KeyError:
            messagebox.showerror(title="key error",message=f"There is no information for {website_message} try another website")
            website_entry.delete(0,END)



#my window
my_window = Tk()
my_window.minsize(width=1000,height=1000)
my_window.title("password manager")
#my canvas
my_canvas= Canvas(width=200,height=200)
lock_image=PhotoImage(file="../information_saver_fullProject/logo.png")
my_canvas.create_image(100,100,image=lock_image)
my_canvas.grid(column=1,row=0)
#website label
website_label =Label(text="Website:")
website_label.grid(column=0,row=1)
#website entry
website_entry=Entry()
website_entry.grid(column=1,row=1)
#email label
email_label =Label(text="Email/Username:")
email_label.grid(column=0,row=2)
#email entry
email_entry=Entry(width=35)
email_entry.insert(END,string="alexnjuguna@gmail.com")
email_entry.grid(column=1,row=2,columnspan=2)
#password label
password_label =Label(text="Password:")
password_label.grid(column=0,row=3)
#password entry
password_entry=Entry(width=21)
password_entry.grid(column=1,row=3)
#generate_password button
generate_password_button= Button(text="Generate password",command=generate_password)
generate_password_button.grid(column=2,row=3)
#add button
add_button = Button(text="Add",command=writing,width=36)
add_button.grid(column=1,row=4,columnspan=2)
# search button
search_button=Button(text="search",command=searching)
search_button.grid(row=1,column=2)


my_window.mainloop()