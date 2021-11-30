from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from tkinter import filedialog
from tkcalendar import *
import datetime


from Backend.backend_db import Database
from Directories.save_payments import *

database=Database("Metra.db")


class Payment:
  def __init__(self, master, employeeId, customerName, customerId, payment_status):
    self.master = master
    self.employeeId = employeeId
    self.customerName = customerName
    self.customerId = customerId
    
    self.payment_status = payment_status
    self.created_at = datetime.datetime.now()

    self.master.title('Make Payment')
   
    self.master.geometry("{0}x{1}+0+0".format(master.winfo_screenwidth(), master.winfo_screenheight()))
    self.master.configure(background = '#e1d8b9')
    

    self.style = ttk.Style()
    self.style.configure('TFrame', background = '#e1d8b9')
    self.style.configure('TButton', background = '#e1d8b9')
    self.style.configure('TLabel', background = '#e1d8b9', font = ('Arial', 11))
    self.style.configure('Header.TLabel', font = ('Arial', 18, 'bold'))
    self.frame_header = ttk.Frame(master)
    self.frame_header.pack()
    ttk.Label(self.frame_header, style='Header.TLabel', text = "Create Payment").grid(row=0, column=1, rowspan=2)

    self.frame_content = ttk.Frame(master)
    self.frame_content.pack()

    ttk.Label(self.frame_content, text = 'Customer Name: ').grid(row = 0, column = 0, padx = 5,pady = 5,sticky='sw')
    ttk.Label(self.frame_content, text = 'Phone No: ').grid(row = 1, column = 0, padx = 5, pady = 5,sticky='sw')
    ttk.Label(self.frame_content, text = 'Payment Type: ').grid(row = 2, column = 0, padx = 5, pady = 5,sticky='sw')
    ttk.Label(self.frame_content, text = 'Payment Amount: ').grid(row = 3, column = 0, padx = 5, pady = 5,sticky='sw')

    
    
    self.entry_name = ttk.Entry(self.frame_content, width = 24)
    self.entry_name.insert(0, self.customerName)
    # self.entry_name.state(['disabled'])
    self.entry_name.state(['readonly'])
    self.entry_phoneNo = ttk.Entry(self.frame_content, text = self.customerId,width = 24)
    self.entry_phoneNo.insert(0, self.customerId)
    self.entry_phoneNo.state(['readonly'])
    self.entry_payment_amount = ttk.Entry(self.frame_content, width = 24)
    


    self.entry_name.grid(row=0, column=1, padx = 5)
    self.entry_phoneNo.grid(row=1, column=1, padx = 5)
    self.entry_payment_amount.grid(row=3, column=1, padx = 5)
    # -----------Select from Combobox-------------------
    self.payment_type = StringVar()
    self.payment_type_cb = ttk.Combobox(self.frame_content, textvariable=self.payment_type)
    self.payment_type_cb.grid(row=2, column=1, padx=5)
    # --------Add values to the combobox-----
    self.payment_type_cb.config(values = ('First Payment', 'Second Payment', 'Final Payment'))
    # self.payment_type.get()  #to get the chosen value

   
    self.submit_btn = ttk.Button(self.frame_content, text = 'Submit Payment', command=self.submit_payment)
    # self.submit_btn.state(['disabled'])
    
      
   
    # self.submit_btn.instate(['disabled']) 
    # self.submit_btn.state(['!disabled'])
    self.submit_btn.grid(row = 4, column= 1,  padx = 5, sticky='e')


  def submit_payment(self):
    if (self.entry_payment_amount.get() != ""): 
      self.payment_status = 0
      database.update_payment(self.employeeId, self.customerName, self.customerId, self.payment_type.get(), self.entry_payment_amount.get(), self.payment_status, self.created_at)
      make_output_dir(self.customerId)
      save_customer_payments(self.employeeId, self.customerName, self.customerId,  self.payment_status, self.entry_payment_amount.get(),  self.created_at)
      messagebox.showinfo(title = "Success", message = "Payment Submited!")
      self.master.destroy()
      
      # self.close_window()
    if (self.entry_payment_amount.get() == ""): 
       messagebox.showinfo(title = "Error", message = "Enter the payment amount please.")
      
    
    # Add Task to structural and inspector--------------
 
  


# def main():
#   root = Tk()
#   payment = Payment(root)
#   root.mainloop()
# if __name__ == "__main__": main()