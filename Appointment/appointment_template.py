
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from tkcalendar import *
import datetime

from Backend.backend_db import Database
from Directories.save_appointments import *

database=Database("Metra.db")


class Appointment:
  def __init__(self, master, employeeId, customerName, customerId):
    self.master=master
    self.employeeId=employeeId
    self.customerName = customerName
    self.customerId = customerId
    self.created_at = datetime.datetime.now()

    self.year = datetime.date.today().year
    self.month = datetime.date.today().month
    self.day = datetime.date.today().day
    

   

    
   
    master.title('Create Appointment')
    # master.resizable(False, False)
    master.geometry('800x800')
    master.configure(background = '#e1d8b9')
    self.frame_header = ttk.Frame(master)
    self.frame_header.pack()

    ttk.Label(self.frame_header, text = "Make an appointment").grid(row=0, column =1)
    self.frame_content = ttk.Frame(master)
    self.frame_content.pack()

    ttk.Label(self.frame_content, text = 'Customer Name:').grid(row = 0, column = 0)
    self.entry_customerName = ttk.Entry(self.frame_content, width = 24, font = ('Arial', 14))   
    self.entry_customerName.grid(row = 0, column = 1, padx=5)
    ttk.Label(self.frame_content, text = 'Phone No:').grid(row = 1, column = 0)
    self.entry_customerId = ttk.Entry(self.frame_content, width = 24, font = ('Arial', 14))   
    self.entry_customerId.grid(row = 1, column = 1, padx=5)

    
   

    ttk.Label(self.frame_content, text = 'Date:').grid(row = 3, column = 0)
    self.cal = Calendar(self.frame_content, date_pattern="dd-mm-y",showweeknumbers=False, foreground='black', background='blue', font=(14),selectedmode="day", year=self.year, month=self.month, day=self.day)
    self.cal.grid(row = 3, column=1, padx=5)
    
    
    # self.entry_app_date = ttk.Entry(self.frame_content, width = 24, font = ('Arial', 14))   
    # self.entry_app_date.grid(row = 1, column = 2, padx = 5)

    ttk.Label(self.frame_content, text = 'Employee Id: ').grid(row = 4, column = 0)

     # -----------Select from Combobox-------------------
    self.employee_Id = StringVar()
    self.employee_Id_cb = ttk.Combobox(self.frame_content, textvariable=self.employee_Id)
    self.employee_Id_cb.grid(row=4, column=1, padx=5)
    # --------Add values to the combobox-----
    self.employee_Id_cb.config(values = ('Architect', 'Structural', 'Inspector'))
    # self.payment_type.get()  #to get the chosen value
  
    
    ttk.Button(self.frame_content, text = 'Save',
                command = self.submit).grid(row = 8, column = 0, padx = 5, pady = 5, sticky = 'e')
   
  def submit(self):    
    
    self.customerId = self.entry_customerId.get()
    database.insert_appointment(self.employeeId, self.entry_customerId.get(), self.entry_customerName.get(), self.cal.get_date())
    print(self.cal.get_date())
    # database.insert_appointment(self.employeeId, self.customerId, self.entry_customerName.get(), self.entry_app_date.get())
    make_output_dir(self.customerId)
    save_customer_appointments(self.employee_Id.get(), self.entry_customerId.get(), self.entry_customerName.get(), self.cal.get_date())
    messagebox.showinfo(title = "Appointment", message = "Appointment Submited!")
    self.close_window()
  def close_window(self):
    self.master.destroy()
  






