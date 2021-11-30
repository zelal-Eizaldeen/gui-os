from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from tkinter import filedialog
from tkcalendar import *
import datetime


from Backend.backend_db import Database
from Payment.payment_template import Payment
from Directories.save_rukhsah import *

database=Database("Metra.db")


class Rukhsah:
  def __init__(self, master, employeeId, customerName, customerId, payment_status, rukhsah_status):
    self.master = master
    self.employeeId = employeeId
    self.customerName = customerName
    self.customerId = customerId
    self.payment_status = payment_status
    self.file_rukhsah = ""
    
    self.rukhsah_status = rukhsah_status
    self.created_at = datetime.datetime.now()

    self.master.title('Make Rukhsah')
   
    self.master.geometry("{0}x{1}+0+0".format(master.winfo_screenwidth(), master.winfo_screenheight()))
    self.master.configure(background = '#e1d8b9')
    

    self.style = ttk.Style()
    self.style.configure('TFrame', background = '#e1d8b9')
    self.style.configure('TButton', background = '#e1d8b9')
    self.style.configure('TLabel', background = '#e1d8b9', font = ('Arial', 11))
    self.style.configure('Header.TLabel', font = ('Arial', 18, 'bold'))
    self.frame_header = ttk.Frame(master)
    self.frame_header.pack()
    ttk.Label(self.frame_header, style='Header.TLabel', text = "Create Rukhsah").grid(row=0, column=1, rowspan=2)

    self.frame_content = ttk.Frame(master)
    self.frame_content.pack()

    ttk.Label(self.frame_content, text = 'Customer Name: ').grid(row = 0, column = 0, padx = 5,pady = 5,sticky='sw')
    ttk.Label(self.frame_content, text = 'Phone No: ').grid(row = 1, column = 0, padx = 5, pady = 5,sticky='sw')
    ttk.Label(self.frame_content, text = 'Upload Rukhsah: ').grid(row = 3, column = 0, padx = 5, pady = 5,sticky='sw')

    
    
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
    
    ttk.Button(self.frame_content, text = 'Upload Rukhsah', command=self.upload_rukhsah).grid(row = 3, column= 1,  padx = 5)   
    ttk.Button(self.frame_content, text = 'Submit', command=self.submit).grid(row = 5, column= 1,  padx = 1, sticky='e')

  def upload_rukhsah(self):
    self.file_rukhsah = filedialog.askopenfilename(title="Select A File") 
    with open(self.file_rukhsah, 'rb') as file:
        self.rukhsah_blobData = file.read()
    ttk.Label(self.frame_content, text=self.file_rukhsah).grid(row=8, column=0, padx = 5)
 
  def submit(self): 
    if (self.file_rukhsah == ""):
      messagebox.showerror("Error", "please upload Rukhsah") 
    else:
      self.rukhsah_status = 0
      self.payment_status = 1
      database.update_rukhsah(self.employeeId, self.customerName, self.customerId, self.rukhsah_blobData, self.rukhsah_status, self.created_at)
      make_output_dir(self.customerId)
      save_customer_rukhsah(self.employeeId, self.customerName,self.customerId, self.rukhsah_status, self.file_rukhsah, self.rukhsah_blobData, self.created_at)
      messagebox.showinfo(title = "Success", message = "Rukhsah Submited!")
      
      self.master.destroy()
      messagebox.showinfo(title = "Payment", message = "Make a Payment for customer:{} with phone number {}".format(self.customerName,self.customerId))    
      root = Tk() 
      payment = Payment(root, self.employeeId, self.customerName, self.customerId,self.payment_status)

    


  
    # self.close_window()
    
    # Add Task to structural and inspector--------------
  def close_window(self):
    self.master.destroy()
  


# def main():
#   root = Tk()
#   payment = Payment(root)
#   root.mainloop()
# if __name__ == "__main__": main()