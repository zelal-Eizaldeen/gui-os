from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from tkinter import filedialog
from tkcalendar import *

from Backend.backend_db import Database
from Payment.payment_template import Payment
from Customer.create_customer_template import Customer
from Customer.show_all_customers import ShowAllCustomers
from Plan.show_accepted_plans import ShowAcceptedPlans
from Plan.create_plan import CreatePlan

from Appointment.appointment_template import Appointment
from Appointment.show_all_appointments import ShowAllAppointments
from Payment.payment_template import Payment

database=Database("Metra.db")


class Inspector:
  def __init__(self, master, employeeId, payment_status, rukhsah_status):
    self.master =  master
    self.employeeId = employeeId
    self.customerName = ""
    self.customerId = ""
    self.payment_status = payment_status
    self.rukhsah_status = rukhsah_status
    self.plan_type = ""


   

   
    master.title('Inspector')
    master.resizable(False, False)
    master.geometry('800x800')
    master.configure(background = '#e1d8b9')

    self.style = ttk.Style()
    self.style.configure('TFrame', background = '#e1d8b9')
    self.style.configure('TButton', background = '#e1d8b9')
    self.style.configure('TLabel', background = '#e1d8b9', font = ('Arial', 11))
    self.style.configure('Header.TLabel', font = ('Arial', 18, 'bold'))
    self.frame_header = ttk.Frame(master)
    self.frame_header.pack()
    

    
    ttk.Label(self.frame_header, style='Header.TLabel', text = "Inspector").grid(row=0, column=1, rowspan=2)

    self.frame_content = ttk.Frame(master)
    self.frame_content.pack()

  
    ttk.Button(self.frame_content, text = 'Show Accepted Plans', command=self.show_accepted_plans).grid(row = 0, column= 1,   padx= 10, pady=20)
    ttk.Button(self.frame_content, text = 'Upload Plan', command=self.upload_plan).grid(row = 4, column= 1,  padx = 10, pady=20)

    ttk.Button(self.frame_content, text = 'Make Appointment', command=self.make_appointmnet).grid(row = 2, column= 1,  padx = 10, pady=20)
    ttk.Button(self.frame_content, text = 'Show All Appointments', command=self.show_all_appointments).grid(row = 3, column= 1,  padx = 10, pady=20)
   
    
   
  def show_accepted_plans(self):
     root = Tk()
     show_accepted_plans = ShowAcceptedPlans(root, self.employeeId, self.plan_type)
     
      
  def make_appointmnet(self):
    app_win = Toplevel(self.master)
    appointment = Appointment(app_win, self.employeeId, self.customerName, self.customerId)
  def show_all_appointments(self):
    show_all_appointments_win = Toplevel(self.master)
    show_all_appointments = ShowAllAppointments(show_all_appointments_win, self.employeeId)
  

  def upload_plan(self):
    upload_win = Toplevel(self.master)
    create_plan=CreatePlan(upload_win, self.employeeId, self.customerName, self.customerId, self.payment_status, self.rukhsah_status)     
   
   
    # for plan in row:
    #   print(plan[0])
    
    # print(row[0])
            

def main():
  root = Tk()
  secretary = Secretary(root)
  root.mainloop()
  
if __name__ == "__main__": main()




























# from tkinter import *
# from tkinter import ttk
# from tkinter import messagebox
# from tkinter import filedialog
# from tkcalendar import *

# from Plan.arch_plan_backend import Database

# database=Database("Metra.db")



# class Inspector:
#   def __init__(self, master, employeeId):
     
#     master.title('Inspector')
#     master.resizable(False, False)
#     master.geometry('800x800')
#     master.configure(background = '#e1d8b9')

#     self.style = ttk.Style()
#     self.style.configure('TFrame', background = '#e1d8b9')
#     self.style.configure('TButton', background = '#e1d8b9')
#     self.style.configure('TLabel', background = '#e1d8b9', font = ('Arial', 11))
#     self.style.configure('Header.TLabel', font = ('Arial', 18, 'bold'))
#     self.frame_header = ttk.Frame(master)
#     self.frame_header.pack()
#     ttk.Label(self.frame_header, style='Header.TLabel', text = "Check Accepted Architectural Plans").grid(row=0, column=1, rowspan=2)

#     self.frame_content = ttk.Frame(master)
#     self.frame_content.pack()

    
   


#     # ttk.Button(self.frame_content, text = 'Check Accepted Architect Plan', command=self.showAcceptedArchPlan).grid(row = 2, column= 0,  padx = 5)   
#     ttk.Button(self.frame_content, text = 'Check Accepted Plan', command=self.submit).grid(row = 4, column= 1,  padx = 5, sticky='e')

    
   
 

#   def submit(self): 
#     database.view_accepted_arch_plans()
    
  
# def main():
#   root = Tk()
#   accepted_arch_plan = AcceptedArchPlan(root)
#   root.mainloop()
# if __name__ == "__main__": main()