from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from tkinter import filedialog
from tkcalendar import *
import os



from Backend.backend_db import Database



database=Database("Metra.db")



class ShowAllAppointments:
  def __init__(self,master, employeeId):
   
    self.employeeId = employeeId
    
    master.title('All Appointments')
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
    ttk.Label(self.frame_header, style='Header.TLabel', text = "View All Appointments").grid(row=0, column=1, rowspan=2)
    self.frame_content = ttk.Frame(master)
    self.frame_content.pack()

    ttk.Label(self.frame_content, text = 'All Appointment: ' ).grid(row = 0, column = 0, padx = 5, sticky='sw')
   
    self.list_appointmnets=Listbox(self.frame_content, height=6,width=35)
    self.list_appointmnets.grid(row=2,column=0,rowspan=6,columnspan=2)
    self.list_appointmnets.bind('<<ListboxSelect>>',self.get_selected_appointmnet)
    ttk.Button(self.frame_content, text = 'Delete Appointment', command=self.delete_appointment).grid(row = 3, column= 5,   padx= 10, pady=20)


    if self.employeeId == 'secretary':
      self.view_all_sec_appointments()
    else:
      self.view_all_appointments()
   


  def get_selected_appointmnet(self,event):
        self.index=self.list_appointmnets.curselection()[0]
        self.selected_tuple=self.list_appointmnets.get(self.index)
        
  def view_all_appointments(self):
    self.list_appointmnets.delete(0,END)
    for row in database.view_all_appointments(self.employeeId):
      self.list_appointmnets.insert(END,row)
      self.customerId = row[0]
  def view_all_sec_appointments(self):
    self.list_appointmnets.delete(0,END)
    for row in database.view_all_sec_appointments():
      self.list_appointmnets.insert(END,row)
      self.customerId = row[0]
     

  def delete_appointment(self):
    database.delete_appointment(self.customerId)
    self.list_appointmnets.delete(self.index)
  

       
      
  # def view_document(self):
  #   root = Tk()
  #   show_document = ShowDocument(root, self.employeeId,self.customerId)
   
    
   
    

def main():
  root = Tk()
  show_all_customer = ShowAllCustomers(root)
  root.mainloop()
if __name__ == "__main__": main()