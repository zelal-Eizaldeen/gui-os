

from tkinter import *
import os

def delete_screen3():
  screen3.destroy()
def delete_screen4():
  screen4.destroy()
def delete_screen5():
  screen5.destroy()
# def logout():
#   screen7.destroy()
def saved():
  screen10 = Toplevel(screen)
  screen10.title("Saved")
  screen10.geometry("100x100")
  Label(screen10, text="Saved").pack()
def save():
  filename = raw_filename.get()
  notes = raw_notes.get()

  data = open(filename, "w")
  data.write(notes)
  data.close()

  saved()
def create_user():
  global raw_filename
  raw_filename = StringVar()
  global raw_notes
  raw_notes = StringVar()
  screen9 = Toplevel(screen)
  screen9.title("Info")
  screen9.geometry("300x250")
  Label(screen9, text="Please enter the customer name below: ").pack()
  Entry(screen9, textvariable=raw_filename).pack()
  Label(screen9, text="Please enter the notes for the file below: ").pack()
  Entry(screen9, textvariable=raw_notes).pack()
  Button(screen9, text="Save", command = save).pack()

def view_notes1():
  filename1 = raw_filename1.get()
  data = open(filename1, "r")
  data1 = data.read()
  screen12 = Toplevel(screen)
  screen12.title("Notes")
  screen12.geometry("400x400")
  Label(screen12, text=data1).pack()
  
  
def view_notes():
  screen11 = Toplevel(screen)
  screen11.title("Info")
  screen11.geometry("250x250")
  all_files = os.listdir()
  Label(screen11, text="Please use one of the filename below").pack()
  Label(screen11, text=all_files).pack()
  global raw_filename1
  raw_filename1 = StringVar()
  Entry(screen11, textvariable=raw_filename1).pack()
  Button(screen11, command=view_notes1, text="OK").pack()

def delete_note1():
  filename3 = raw_filename2.get()
  os.remove(filename3)
  screen14 = Toplevel(screen)
  screen14.title("Notes")
  screen14.geometry("400x400")
  Label(screen14, text=filename3+" removed!").pack()

def delete_note():
  screen13 = Toplevel(screen)
  screen13.title("Info")
  screen13.geometry("250x250")
  all_files = os.listdir()
  Label(screen13, text="Please use one of the filename below").pack()
  Label(screen13, text=all_files).pack()
  global raw_filename2
  raw_filename2 = StringVar()
  Entry(screen13, textvariable=raw_filename2).pack()
  Button(screen13, text="OK", command=delete_note1).pack()

# Add Secretary Dashboard...
def session():
  screen8 = Toplevel(screen)
  screen8.title("dashboard")
  screen8.geometry("400x400")
  Label(screen8, text="Welcome to Secretary dashboard").pack()
  Button(screen8,text="Create User", command=create_user).pack()
  Button(screen8, text="View User", command=view_notes).pack()
  Button(screen8, text="Delete User", command=delete_note).pack()

def login_succss():
  session()
  # global screen3
  # screen3 = Toplevel(screen)
  # screen3.title("Success")
  # screen3.geometry("150x100")
  # Label(screen3, text="Login Success").pack()
  # Button(screen3, text="OK", command = delete_screen3).pack()

def password_not_recognized():
  global screen4
  screen4 = Toplevel(screen)
  screen4.title("Success")
  screen4.geometry("150x100")
  Label(screen4, text="Password Error").pack()
  Button(screen4, text="OK", command = delete_screen4).pack()

def user_not_found():
  global screen5
  screen5 = Toplevel(screen)
  screen5.title("Success")
  screen5.geometry("150x100")
  Label(screen5, text="User Not Found").pack()
  Button(screen5, text="OK", command = delete_screen5).pack()
  

def register_user():
  username_info = username.get()
  password_info = password.get()
  file=open(username_info, "w")
  file.write(username_info+"\n")
  file.write(password_info)
  file.close()
  username_entry.delete(0, END)
  password_entry.delete(0,END)
  Label(screen1, text="Registration success!", fg="green").pack()
def login_verify():
  username1 = username_verify.get()
  password1 = password_verify.get()
  username_entry1.delete(0,END)
  password_entry1.delete(0,END)

  list_of_files = os.listdir()
  if username1 in list_of_files:
    file1 = open(username1, "r")
    verify = file1.read().splitlines()
    if password1 in verify:
      login_succss()
    else:
      password_not_recognized()
  else:
    user_not_found()


def register():
  global screen1
  screen1 = Toplevel(screen)
  screen1.title("Register")
  screen1.geometry("300x250")

  global username
  global password
  global username_entry
  global password_entry

  username = StringVar()
  password = StringVar()

  
  Label(screen1,text = "Please enter details below").pack()
  Label(screen1,text = "").pack()

  Label(screen1,text = "Username * ").pack()
  username_entry=Entry(screen1,textvariable=username)
  username_entry.pack()
  Label(screen1,text = "Password *").pack()
  password_entry=Entry(screen1,textvariable=password)
  password_entry.pack()
  Label(screen1,text = "").pack()
  Button(screen1, text="Register", width=10, height=1, command= register_user).pack()



def login():
  global screen2
  screen2=Toplevel(screen)
  screen2.title("Login")
  screen2.geometry("300x250")
 
  Label(screen2,text = "Please enter details below to login").pack()
  Label(screen2,text = "").pack()

  global username_verify
  global password_verify

  username_verify = StringVar()
  password_verify = StringVar()

  global username_entry1
  global password_entry1

  Label(screen2,text = "Username * ").pack()
  username_entry1=Entry(screen2,textvariable=username_verify)
  username_entry1.pack()
  Label(screen2,text = "").pack()
  Label(screen2,text = "Password *").pack()
  password_entry1=Entry(screen2,textvariable=password_verify)
  password_entry1.pack()
  Label(screen2,text = "").pack()
  Button(screen2, text="Login", width=10, height=1, command= login_verify).pack()
  print("Secretary session started!!")

def main_screen():
  global screen
  screen = Tk()
  screen.geometry("320x250")
  screen.title("Main Screen")
  Label(text = "Main Screen", bg = "grey", font = ("Calibri", 13)).pack()
  Label(text = "").pack()
  Button(text="Login", height="2", width="30", command= login).pack()
  Label(text="").pack()
  Button(text="Register", height="2", width="30", command= register).pack()

 screen.mainloop() 



