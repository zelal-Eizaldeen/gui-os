from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from tkinter import filedialog
from tkcalendar import *
import os



from Backend.backend_db import Database



database=Database("Metra.db")



class ShowAllCustomers:
  def __init__(self,master, employeeId):

    self.master = master
    self.employeeId = employeeId

  
    
    master.title('All Customers')
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
    ttk.Label(self.frame_header, style='Header.TLabel', text = "View All Customers").grid(row=0, column=1, rowspan=2)
    self.frame_content = ttk.Frame(master)
    self.frame_content.pack()

    ttk.Label(self.frame_content, text = 'All Customers: ' ).grid(row = 0, column = 0, padx = 5, sticky='sw')
   
    self.list_customers=Listbox(self.frame_content, height=6,width=35)
    self.list_customers.grid(row=2,column=0,rowspan=6,columnspan=2)
      

    self.list_customers.bind('<<ListboxSelect>>',self.get_selected_customer)

  


    self.view_all_customers()

  def get_selected_customer(self,event):
        index=self.list_customers.curselection()[0]
        self.selected_tuple=self.list_customers.get(index)
        self.customerId = self.selected_tuple[2]

        


  def view_all_customers(self):
    self.list_customers.delete(0,END)
    for row in database.view_all_customers():
      self.list_customers.insert(END,row)
      self.customerId = row[2]
      
  # def view_document(self):
  #   root = Tk()
  #   show_document = ShowDocument(root, self.employeeId,self.customerId)
   
    
   
    

def main():
  root = Tk()
  show_all_customer = ShowAllCustomers(root)
  root.mainloop()
if __name__ == "__main__": main()