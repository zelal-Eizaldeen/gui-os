from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from tkinter import filedialog
from tkcalendar import *
import os
from os import path


from Backend.backend_db import Database
from Directories.save_documents import *

database=Database("Metra.db")


class Customer:
  def __init__(self, master, employeeId):
    self.employeeId = employeeId
    self.customerName = ""
    self.customerId = ""
    self.customerEmail = ""
    self.exist_customerId = ""
    self.master = master
    self.current_path = ""
    self.master.title('Create Customer')
    self.master.resizable(False, False)
    # self.master.geometry('800x800+300+300')
    self.master.geometry("{0}x{1}+0+0".format(self.master.winfo_screenwidth(), self.master.winfo_screenheight()))
    self.file_civilId = ""
    self.file_possessionPaper = ""
    self.file_publicLocation = ""
    self.master.configure(background = '#e1d8b9')

    self.style = ttk.Style()
    self.style.configure('TFrame', background = '#e1d8b9')
    self.style.configure('TButton', background = '#e1d8b9')
    self.style.configure('TLabel', background = '#e1d8b9', font = ('Arial', 11))
    self.style.configure('Header.TLabel', font = ('Arial', 18, 'bold'))
    self.frame_header = ttk.Frame(master)
    self.frame_header.pack()
    

    ttk.Label(self.frame_header, style='Header.TLabel', text = "Create Customer").grid(row=0, column=1, rowspan=2)

    self.frame_content = ttk.Frame(master)
    self.frame_content.pack()

    ttk.Label(self.frame_content, text = 'Name: ').grid(row = 0, column = 0, padx = 5, sticky='sw')
    ttk.Label(self.frame_content, text = 'Email: ').grid(row = 0, column = 1, padx = 5, sticky='sw')
    ttk.Label(self.frame_content, text = 'PhoneNo: ').grid(row = 0, column = 2, padx = 5, sticky='sw')

    self.entry_name = ttk.Entry(self.frame_content, width = 24)
    self.entry_email = ttk.Entry(self.frame_content, width = 24)
    self.entry_phoneNo = ttk.Entry(self.frame_content, width = 24)

    self.entry_name.grid(row=1, column=0, padx = 5)
    self.entry_email.grid(row=1, column=1, padx = 5)
    self.entry_phoneNo.grid(row=1, column=2, padx = 5)

    


    ttk.Button(self.frame_content, text = 'Upload Civil ID', command=self.uploadCivilId).grid(row = 2, column= 0,  padx = 5)
    ttk.Button(self.frame_content, text = 'Upload possess paper', command=self.uploadPssessionPaper).grid(row = 2, column= 1,  padx = 5)
    ttk.Button(self.frame_content, text = 'Upload public location', command=self.uploadPublicLocation).grid(row = 2, column= 2,  padx = 5)
    ttk.Button(self.frame_content, text = 'Submit', command=self.submit).grid(row = 4, column= 0,  padx = 5, sticky='e')

    
   
  def uploadCivilId(self):
    self.file_civilId = filedialog.askopenfilename(title="Select A File") 
    with open(self.file_civilId, 'rb') as file:
        self.civilId_blobData = file.read()
    ttk.Label(self.frame_content, text=self.file_civilId).grid(row=3, column=0, padx = 5)
  def uploadPssessionPaper(self):
    self.file_possessionPaper = filedialog.askopenfilename(title="Select A File") 
    with open(self.file_possessionPaper, 'rb') as file:
        self.possessionPaper_blobData = file.read()
    ttk.Label(self.frame_content, text=self.file_possessionPaper).grid(row=3, column=1, padx = 5)
  def uploadPublicLocation(self):
    self.file_publicLocation = filedialog.askopenfilename(title="Select A File") 
    with open(self.file_publicLocation, 'rb') as file:
        self.publicLocation_blobData = file.read()
    ttk.Label(self.frame_content, text=self.file_publicLocation).grid(row=3, column=2, padx = 5)

  
  def submit(self):
    # self.current_path = str(path.realpath())

    self.customerName = self.entry_name.get()
    self.customerEmail = self.entry_email.get()
    self.customerId = self.entry_phoneNo.get()

    database.view_customer(self.customerId)
    for row in database.view_customer(self.customerId):
      if self.customerId == row[2]:
        self.exist_customerId = row[2]

    if ((self.customerName == "") or (self.customerEmail == "") or (self.customerId == "")):
      messagebox.showerror("Error", "please fill all information....") 
    elif ((self.file_civilId == "") or (self.file_possessionPaper == "") or (self.file_publicLocation == "")):
      messagebox.showerror("Error", "please upload all files....") 
    
    elif (self.customerId == self.exist_customerId):
      messagebox.showerror("Error", "Customer has already created before.") 
    else:
      database.insert_customer(self.customerName,self.customerEmail,self.customerId)
      database.insert_document(self.customerId, self.civilId_blobData, self.possessionPaper_blobData, self.publicLocation_blobData)
      messagebox.showinfo(title = "Added Success", message = "Customer Submited!")
      self.save_customer_document()
      self.close_window()

  def save_customer_document(self): 
    
    for row in database.view_document(self.customerId):
        self.customerId = row[1]
        self.civilId = row[2]
        self.possesPaper = row[3]
        self.publicLocation = row[4]
   
    make_output_dir(self.customerId)
    save_documents(self.civilId, self.file_civilId, self.possesPaper, self.file_possessionPaper, self.publicLocation, self.file_publicLocation)
   
    

  def close_window(self):
    self.master.destroy()
  

def main():
  root = Tk()
  customer = Customer(root)
  root.mainloop()
if __name__ == "__main__": main()