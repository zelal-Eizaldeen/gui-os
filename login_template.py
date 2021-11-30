from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from tkinter import filedialog
from tkcalendar import *


from Employees.inspector import Inspector
from Employees.secretary import Secretary
from Employees.architect import Architect



class Login:
  # special method to initialize attributes (initilizer function)
  #  self parameter is the object itself passed into this para
  def __init__(self, master):
    self.master = master
    self.master.title('Login')
    self.master.resizable(False, False)
    # self.master.geometry('800x800+300+300')
    self.master.geometry("{0}x{1}+0+0".format(self.master.winfo_screenwidth(), self.master.winfo_screenheight()))

    self.master.configure(background = '#e1d8b9')

   

    self.style = ttk.Style()
    self.style.configure('TFrame', background = '#e1d8b9')
    self.style.configure('TButton', background = '#e1d8b9')
    self.style.configure('TLabel', background = '#e1d8b9', font = ('Arial', 14))
    self.style.configure('Header.TLabel', font = ('Arial', 18, 'bold'))
    self.frame_header = ttk.Frame(master)
    self.frame_header.pack()
    
    
    
    ttk.Label(self.frame_header, style='Header.TLabel', text = "Login Employee").grid(row=0, column=1, rowspan=2)

    self.frame_content = ttk.Frame(master)
    self.frame_content.pack()

    ttk.Label(self.frame_content, text = 'Username: ').grid(row = 0, column = 0, padx = 5, sticky='sw')
    ttk.Label(self.frame_content, text = 'Password: ').grid(row = 0, column = 1, padx = 5, sticky='sw')

    self.entry_username = ttk.Entry(self.frame_content, width = 24)
    self.entry_password = ttk.Entry(self.frame_content, width = 24)
    
    self.entry_username.grid(row=1, column=0, padx = 5)
    self.entry_password.grid(row=1, column=1, padx = 5)

    self.entry_password.config(show = '*')
   
   
    ttk.Button(self.frame_content, text = 'Login', command=self.login).grid(row = 4, column= 0,  padx = 5, sticky='e')
   
   
  
  def login(self):
    employees = {"secretary": "secpassword", "architect": "arcpassword", "inspector": "inspassword"}
    employee = self.entry_username.get()
    password = self.entry_password.get()
    payment_status = 0
    rukhsah_status = 0


    if employees[employee] == password and employee == "secretary":
      self.colse_login_window()
      root = Tk()
      secretary = Secretary(root, employee,payment_status, rukhsah_status)
    
    elif employees[employee] == password and employee == "architect":
      self.colse_login_window()
      root = Tk()
      architect = Architect(root, employee,payment_status, rukhsah_status)
    
    elif employees[employee] == password and employee == "inspector":
      self.colse_login_window()
      root = Tk()
      inspector = Inspector(root, employee,payment_status, rukhsah_status)

    else:
      messagebox.showerror("Error", "Wrong Username or Password, please try again!!!!")



      
    
  def colse_login_window(self):
    self.master.destroy()

  
          
def main():
  root = Tk()
  # login is an instance from Login class
  login = Login(root)
  root.mainloop()
  
if __name__ == "__main__": main()