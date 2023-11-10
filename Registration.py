from tkinter import *
from tkinter import messagebox
import tkinter as tk

main_window = tk.Tk()
main_window.geometry("1260x700+0+0")
main_window.title("Registration Form")
main_window.configure(bg="#FFB6C1")

def register():
    if (
        stringUsername.get() == ""
        or stringPassword.get() == ""
        or stringConfirmPassword.get() == ""
    ):
        messagebox.showwarning("Warning!", "Potential fields are required.")
    elif stringPassword.get() != stringConfirmPassword.get():
        messagebox.showwarning("Warning!", "Passwords do not match.")
    else:
        username = stringUsername.get()
        password = stringPassword.get()
        print(f"Registration Successful:\nUsername: {username}\nPassword: {password}")
        messagebox.showinfo("Successful", "Registration successful.")

def sign_in():
    messagebox.showinfo("Sign-In", "Sign-In functionality goes here.")

frameDetail = tk.LabelFrame(master=main_window, bg="#FFFFFF", fg="lightgrey")
frameDetail.place(x=60, y=60, width=1140, height=575)

registrationTitle = tk.Label(main_window, text="Registration", font=("Comic Sans MS", 25), fg="black", bg="white")
registrationTitle.place(x=130, y=120)

stringUsername = StringVar()
stringPassword = StringVar()
stringConfirmPassword = StringVar()

username_lbl = tk.Label(main_window, text="Username:", font=("Arial", 20), bg="white", fg="black")
username_lbl.place(x=130, y=220)

username_ent = tk.Entry(main_window, bd=2, font=("Arial", 20), textvariable=stringUsername)
username_ent.place(x=130, y=260, width=500)

password_lbl = tk.Label(main_window, text="Password:", font=("Arial", 20), bg="white", fg="black")
password_lbl.place(x=130, y=320)

password_ent = tk.Entry(main_window, bd=2, font=("Arial", 20), show='*', textvariable=stringPassword)
password_ent.place(x=130, y=355, width=500)

confirm_password_lbl = tk.Label(main_window, text="Confirm Password:", font=("Arial", 20), bg="white", fg="black")
confirm_password_lbl.place(x=130, y=415)

confirm_password_ent = tk.Entry(main_window, bd=2, font=("Arial", 20), show='*', textvariable=stringConfirmPassword)
confirm_password_ent.place(x=130, y=450, width=500)

registerButton = tk.Button(main_window, text="Register", font=("impact", 16), bd=3, fg="white", bg="red", command=register)
registerButton.place(x=130, y=520, width=250)

sign_inButton = tk.Button(main_window, text="Sign-In", font=("impact", 16), fg="white", bg="black", command=sign_in)
sign_inButton.place(x=400, y=520, width=230)

image = PhotoImage(file="C:\\Users\\DELL\\Downloads\\Python picture (1).png")
image_label = tk.Label(main_window, image=image, bg="white")
image_label.image = image
image_label.place(x=650,y=120,width=500,height=450)

main_window.mainloop()
