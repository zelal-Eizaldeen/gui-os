from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from tkinter import filedialog
from tkcalendar import *
import datetime


from Backend.backend_db import Database
# from Directories.save_tasks import *

database=Database("Metra.db")


class Task:
  def __init__(self, master, employeeId, customerName, customerId):
    
    self.master = master
    self.employeeId = employeeId
    self.customerName = customerName
    self.customerId = customerId
    self.created_at = datetime.datetime.now()
    self.master.title('Make Task')
    self.master.geometry('800x800+300+300')
    # self.master.geometry("{0}x{1}+0+0".format(master.winfo_screenwidth(), master.winfo_screenheight()))
    self.master.configure(background = '#e1d8b9')
    

    self.style = ttk.Style()
    self.style.configure('TFrame', background = '#e1d8b9')
    self.style.configure('TButton', background = '#e1d8b9')
    self.style.configure('TLabel', background = '#e1d8b9', font = ('Arial', 11))
    self.style.configure('Header.TLabel', font = ('Arial', 18, 'bold'))
    self.frame_header = ttk.Frame(master)
    self.frame_header.pack()
    ttk.Label(self.frame_header, style='Header.TLabel', text = "Create Task").grid(row=0, column=1, rowspan=2)

    self.frame_content = ttk.Frame(master)
    self.frame_content.pack()

    ttk.Label(self.frame_content, text = 'Customer Name: ').grid(row = 0, column = 0, padx = 5,pady = 5,sticky='sw')
    ttk.Label(self.frame_content, text = 'Phone No: ').grid(row = 1, column = 0, padx = 5, pady = 5,sticky='sw')
    ttk.Label(self.frame_content, text = 'Task Type: ').grid(row = 2, column = 0, padx = 5, pady = 5,sticky='sw')
    ttk.Label(self.frame_content, text = 'Task for?').grid(row = 3, column = 0, padx = 5, pady = 5,sticky='sw')

    
    
    self.entry_name = ttk.Entry(self.frame_content, width = 24)
    self.entry_name.insert(0, self.customerName)
    # self.entry_name.state(['disabled'])
    # self.entry_name.state(['readonly'])
    self.entry_phoneNo = ttk.Entry(self.frame_content, text = self.customerId,width = 24)
    self.entry_phoneNo.insert(0, self.customerId)
    # self.entry_phoneNo.state(['readonly'])
    self.entry_name.grid(row=0, column=1, padx = 5)
    self.entry_phoneNo.grid(row=1, column=1, padx = 5)

    # -----------Select from Combobox-------------------
    self.task_type = StringVar()
    self.task_type_cb = ttk.Combobox(self.frame_content, textvariable=self.task_type)
    self.task_type_cb.grid(row=2, column=1, padx=5)
    # --------Add values to the combobox-----
    self.task_type_cb.config(values = ('Payment', 'Architect', 'Strutural', 'Inspect', 'Rukhsah'))

    # -----------Select from Combobox-------------------
    self.employee_for= StringVar()
    self.employee_for_cb = ttk.Combobox(self.frame_content, textvariable=self.employee_for)
    self.employee_for_cb.grid(row=3, column=1, padx=5)
    # --------Add values to the combobox-----
    self.employee_for_cb.config(values = ('secretary', 'architect', 'strutural Enf', 'inspector'))
    #-----------------Checkbutton--------------------------
    self.task_status_checkButton = ttk.Checkbutton(self.frame_content, text="Completed?")
    self.task_status_checkButton.grid(row = 5, column= 1,  padx = 5, sticky='e')
    # To store String into Variable
    self.task_status=StringVar() 
    self.task_status.set('Not Completed')
    self.task_status_checkButton.config(variable=self.task_status, onvalue= 'Completed', offvalue='Not_completed')
    

    self.submit_btn = ttk.Button(self.frame_content, text = 'Submit Task', command=self.submit_task)
    self.submit_btn.grid(row = 6, column= 1,  padx = 5, sticky='e')
  
  def submit_task(self):
    database.insert_task(self.task_type.get(), self.task_status.get(), self.employeeId, self.customerName, self.customerId, self.employee_for.get(), self.created_at)
    messagebox.showinfo(title = "Success", message = "Task Submited!")
    self.master.destroy()

  
  

  
      
    
     
    
      

