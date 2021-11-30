from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from tkinter import filedialog
from tkcalendar import *

from Backend.backend_db import Database
from Appointment.appointment_template import Appointment
from Appointment.show_all_appointments import ShowAllAppointments
from Plan.create_plan import CreatePlan

database=Database("Metra.db")


class Architect:
  def __init__(self, master, employeeId, payment_status, rukhsah_status):
    self.master = master
    self.employeeId = employeeId
    self.payment_status = payment_status
    self.rukhsah_status = rukhsah_status
    self.customerName=""
    self.customerId = ""


    self.master.title('Architect')
    master.resizable(False, False)
    master.geometry("{0}x{1}+0+0".format(master.winfo_screenwidth(), master.winfo_screenheight()))
    master.configure(background = '#e1d8b9')

    self.style = ttk.Style()
    self.style.configure('TFrame', background = '#e1d8b9')
    self.style.configure('TButton', background = '#e1d8b9')
    self.style.configure('TLabel', background = '#e1d8b9', font = ('Arial', 11))
    self.style.configure('Header.TLabel', font = ('Arial', 18, 'bold'))
    self.frame_header = ttk.Frame(master)
    self.frame_header.pack()
    

    
    ttk.Label(self.frame_header, style='Header.TLabel', text = "Architect").grid(row=0, column=1, rowspan=2)

    self.frame_content = ttk.Frame(master)
    self.frame_content.pack()

  
    ttk.Button(self.frame_content, text = 'Upload Architectural Plan', command=self.upload_arch_plan).grid(row = 0, column= 1,   padx= 10, pady=20)
    ttk.Button(self.frame_content, text = 'Make Appointment', command=self.make_appointmnet).grid(row = 2, column= 1,  padx = 10, pady=20)
    ttk.Button(self.frame_content, text = 'Show All Appointments', command=self.show_all_appointments).grid(row = 3, column= 1,  padx = 10, pady=20)
   
               

  def upload_arch_plan(self):
    upload_plan_win = Toplevel(self.master)
    create_plan=CreatePlan(upload_plan_win, self.employeeId, self.customerName, self.customerId, self.payment_status, self.rukhsah_status)     
    
  def make_appointmnet(self):
    app_win = Toplevel(self.master)
    appointment = Appointment(app_win, self.employeeId, self.customerName, self.customerId)
    
  def show_all_appointments(self):
    root = Tk()
    show_all_appointments = ShowAllAppointments(root, self.employeeId)
  def close_window(self):
    self.master.destroy()

 


# def main():
#   root = Tk()
#   architect = Architect(root)
#   root.mainloop()
  
# if __name__ == "__main__": main()
























