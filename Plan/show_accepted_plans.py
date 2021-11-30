from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from tkinter import filedialog
from tkcalendar import *
import os



from Backend.backend_db import Database

database=Database("Metra.db")
class ShowAcceptedPlans:
  def __init__(self,master, employeeId, plan_type):
    self.master = master
    self.employeeId = employeeId
    self.plan_type = plan_type
    
    master.title('All Accepted Plans')
    master.resizable(False, False)
    self.master.geometry("{0}x{1}+0+0".format(self.master.winfo_screenwidth(), self.master.winfo_screenheight()))
    master.configure(background = '#e1d8b9')

    self.style = ttk.Style()
    self.style.configure('TFrame', background = '#e1d8b9')
    self.style.configure('TButton', background = '#e1d8b9')
    self.style.configure('TLabel', background = '#e1d8b9', font = ('Arial', 11))
    self.style.configure('Header.TLabel', font = ('Arial', 18, 'bold'))
    self.frame_header = ttk.Frame(master)
    self.frame_header.pack()
    ttk.Label(self.frame_header, style='Header.TLabel', text = "View Accepted Plans").grid(row=0, column=1, rowspan=2)
    self.frame_content = ttk.Frame(master)
    self.frame_content.pack()

    ttk.Label(self.frame_content, text = 'All Accepted Plans: ' ).grid(row = 0, column = 0, padx = 5, sticky='sw')
   
    self.list_accepted_plans=Listbox(self.frame_content, height=6,width=35)
    self.list_accepted_plans.grid(row=2,column=0,rowspan=6,columnspan=2)
    self.list_accepted_plans.bind('<<ListboxSelect>>',self.get_selected_accepted_plan)
  
    self.view_all_accepted_plans()
    # ttk.Button(self.frame_content, text = 'View Document', command=self.view_document).grid(row = 22, column= 1,  padx = 10, pady=20)

  def get_selected_accepted_plan(self,event):
        index=self.list_accepted_plans.curselection()[0]
        self.selected_tuple=self.list_accepted_plans.get(index)
        print(self.selected_tuple)

        


  def view_all_accepted_plans(self):
    self.list_accepted_plans.delete(0,END)
    self.plan_type = 'Accepted'
    for row in database.view_all_accepted_plans(self.plan_type):
      self.list_accepted_plans.insert(END,row)
      print(row)
