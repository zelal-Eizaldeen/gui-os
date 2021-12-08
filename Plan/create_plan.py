from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from tkinter import filedialog
import datetime
import os

from Backend.backend_db import Database
from Appointment.appointment_template import Appointment
from Task.task_template import *
from Directories.save_plans import *


database=Database("Metra.db")



class CreatePlan:
  def __init__(self, master, employeeId, customerName, customerId, payment_status, rukhsah_status):
    
    self.created_at = datetime.datetime.now()
    self.master=master
    self.employeeId=employeeId
    self.customerName = customerName
    self.customerId = customerId
    self.payment_status = payment_status
    self.rukhsah_status = rukhsah_status

    self.master.title('Create Plan')
    self.master.resizable(False, False)
    # self.master.geometry("{0}x{1}+0+0".format(master.winfo_screenwidth(), master.winfo_screenheight()))
    self.master.state('zoomed')
    self.master.configure(background = '#e1d8b9')
    

    self.style = ttk.Style()
    self.style.configure('TFrame', background = '#e1d8b9')
    self.style.configure('TButton', background = '#e1d8b9')
    self.style.configure('TLabel', background = '#e1d8b9', font = ('Arial', 11))
    self.style.configure('Header.TLabel', font = ('Arial', 18, 'bold'))

    self.frame_header = ttk.Frame(master)
    self.frame_header.pack()
    ttk.Label(self.frame_header, style='Header.TLabel', text = "Upload plan").grid(row=0, column=1, rowspan=2)

    self.frame_content = ttk.Frame(master)
    self.frame_content.pack()

   

    ttk.Label(self.frame_content, text = 'Customer Name: ' ).grid(row = 0, column = 0, padx = 5, sticky='sw')
    ttk.Label(self.frame_content, text = 'Customer Phone ' ).grid(row = 0, column = 1, padx = 5, sticky='sw')
    ttk.Label(self.frame_content, text = 'Employee ID: ').grid(row = 0, column = 2, padx = 5, sticky='sw')
   
    self.entry_customerName = ttk.Entry(self.frame_content, width = 24)
    self.entry_customerId = ttk.Entry(self.frame_content, width = 24)
    self.entry_employeeId = ttk.Entry(self.frame_content, width = 24)
    self.entry_employeeId.insert(0, self.employeeId)
    self.entry_employeeId.state(['readonly'])
   
    self.entry_customerName.grid(row=1, column=0, padx = 5)
    self.entry_customerId.grid(row=1, column=1, padx = 5)
    self.entry_employeeId.grid(row=1, column=2, padx = 5)

    self.employeeId = self.entry_employeeId.get()
    self.customerName = self.entry_customerName.get()
    self.customerId = self.entry_customerId.get()

   
    self.frame_plans = ttk.Frame(master)
    self.frame_plans.pack()

    self.type_plan = StringVar()
    
    self.radio_arch = ttk.Radiobutton(self.frame_content, text='Architectural', variable = self.type_plan, value='Architectural') 
    self.radio_struc = ttk.Radiobutton(self.frame_content, text='Structural', variable = self.type_plan, value='Structural')  
    self.radio_acc = ttk.Radiobutton(self.frame_content, text='Accepted', variable = self.type_plan,value='Accepted')  
    self.radio_app = ttk.Radiobutton(self.frame_content, text='Approved', variable = self.type_plan,value='Approved')
    self.radio_final = ttk.Radiobutton(self.frame_content, text='Final', variable = self.type_plan,value='Final')

    self.radio_arch.grid(row = 4, column= 0,  padx = 5) 
    self.radio_struc.grid(row = 5, column= 0,  padx = 5)
    self.radio_acc.grid(row = 6, column= 0,  padx = 5)
    self.radio_app.grid(row = 7, column= 0,  padx = 5)  
    self.radio_final.grid(row = 8, column= 0,  padx = 5)  


    


    ttk.Button(self.frame_content, text = 'Upload Plan', command=self.upload_plan).grid(row = 9, column= 0,  padx = 5)   
    ttk.Button(self.frame_content, text = 'Submit', command=self.submit).grid(row = 9, column= 1,  padx = 5, sticky='e')

  
  def upload_plan(self):
    self.file_plan = filedialog.askopenfilename(title="Select A File") 
    with open(self.file_plan, 'rb') as file:
        self.plan_blobData = file.read()
    ttk.Label(self.frame_content, text=self.file_plan).grid(row=8, column=0, padx = 5)
 
  def submit(self): 
    database.insert_plan(self.entry_employeeId.get(), self.entry_customerName.get(), self.entry_customerId.get(), self.type_plan.get(), self.plan_blobData, self.created_at)
    make_output_dir(self.entry_customerId.get())
    save_customer_plans(self.entry_employeeId.get(), self.entry_customerName.get(), self.entry_customerId.get(), self.type_plan.get(), self.file_plan, self.plan_blobData, self.created_at)
    if self.type_plan.get() == 'Accepted':
      self.payment_status = 1
      database.insert_payment(self.employeeId, self.entry_customerName.get(), self.entry_customerId.get(),  self.payment_status, self.created_at)
      # self.master.withdraw()
     
    if self.type_plan.get() == 'Final':
      self.rukhsah_status = 1
      database.insert_rukhsah(self.employeeId, self.entry_customerName.get(), self.entry_customerId.get(),  self.rukhsah_status, self.created_at)
    messagebox.showinfo(title = "Success", message = "Plan Submited!")
    task_win = Toplevel(self.master)
    Task(task_win,self.employeeId, self.entry_customerName.get(), self.entry_customerId.get())
      

    # self.make_appointmnet()
 
  
  def make_appointmnet(self):
    root=Tk()
    appointment = Appointment(root, self.employeeId, self.customerName, self.customerId)
    