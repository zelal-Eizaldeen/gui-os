from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from tkinter import filedialog
from tkcalendar import *
import datetime


from Backend.backend_db import Database
from Payment.payment_template import Payment
from Customer.create_customer_template import Customer
from Customer.show_all_customers import ShowAllCustomers
from Appointment.appointment_template import Appointment
from Appointment.show_all_appointments import ShowAllAppointments
from Rukhsah.rukhsah_template import Rukhsah
from Plan.create_plan import CreatePlan

database=Database("Metra.db")


class Secretary:
  def __init__(self, master, employeeId,payment_status, rukhsah_status):
    self.master = master
    self.employeeId = employeeId
    self.payment_status = payment_status
    self.rukhsah_status = rukhsah_status
    self.customerName = ""
    self.customerId = ""

   
    self.created_at = datetime.datetime.now()
   
    self.structural_engineer_id = "Structural Engineer"
    
    self.master.title('Secretary')
    # self.master.state('zoomed')
    self.master.geometry('800x800+300+300')
    # self.master.geometry("{0}x{1}+0+0".format(self.master.winfo_screenwidth(), self.master.winfo_screenheight()))
    
    self.master.configure(background = '#e1d8b9')

    self.style = ttk.Style()
    self.style.configure('TFrame', background = '#e1d8b9')
    self.style.configure('TButton', background = '#e1d8b9')
    self.style.configure('TLabel', background = '#e1d8b9', font = ('Arial', 11))
    self.style.configure('Header.TLabel', font = ('Arial', 14, 'bold'))
    self.frame_header = ttk.Frame(master)
    self.frame_header.pack()

    ttk.Button(self.frame_header,  text = 'Refresh', command=self.refresh ).grid(row=0, column=1, sticky='wn') 
    ttk.Label(self.frame_header, style='Header.TLabel', text = "Secretary").grid(row=3, column=1, rowspan=2)

    self.frame_content = ttk.Frame(master)
    self.frame_content.pack()

    ttk.Button(self.frame_content, text = 'Create New Customer', command=self.create_new_customer).grid(row = 0, column= 1,   padx= 10, pady=20)
    ttk.Button(self.frame_content, text = 'Show Customers', command=self.show_customers).grid(row = 1, column= 1, padx= 10, pady=20 )

    ttk.Button(self.frame_content, text = 'Make Appointment', command=self.make_appointmnet).grid(row = 2, column= 1,  padx = 10, pady=20)
    ttk.Button(self.frame_content, text = 'Show All Appointments', command=self.show_all_appointments).grid(row = 3, column= 1,  padx = 10, pady=20)
    ttk.Button(self.frame_content, text = 'Upload Final Plan', command=self.upload_final_plan).grid(row = 4, column= 1,  padx = 10, pady=20)
    

    self.check_payment()
    self.alert_payment()
    self.alert_rukhsah()
  def refresh(self):
    self.master.destroy()
    root=Tk()
    self.__init__(root, self.employeeId, self.payment_status, self.rukhsah_status)
  def check_payment(self):
    pass
   
  def alert_payment(self):
    row = database.view_payments()
    for payment in row:
      if(payment[6] == 1):
        self.employeeId = payment[1]
        self.customerName = payment[2]
        self.customerId = payment[3]
        self.payment_status = payment[6]
        messagebox.showinfo(title = "Payment", message = "Make a Payment for customer:{} with phone number {}".format(self.customerName,self.customerId))
        payment_win = Toplevel(self.master) 
        payment = Payment(payment_win, self.employeeId, self.customerName, self.customerId,self.payment_status)
        
  def alert_rukhsah(self):
    row = database.view_rukhsahs()
    for rukhsah in row:
      if(rukhsah[5] == 1):
        self.employeeId = rukhsah[1]
        self.customerName = rukhsah[2]
        self.customerId = rukhsah[3]
        self.rukhsah_status = 1
        messagebox.showinfo(title = "Rukhsah", message = "Make Rukhsah for customer:{} with phone number {}".format(rukhsah[2],rukhsah[3]))
        rukhsah_win = Toplevel(self.master) 
        rukhsah = Rukhsah(rukhsah_win, self.employeeId, self.customerName, self.customerId,self.payment_status, self.rukhsah_status)
        

  def view_payments(self):
    for row in database.view_payments():
      print(row)

  def show_customers(self):
     show_all_customers_win = Toplevel(self.master)
     show_all_customers = ShowAllCustomers(show_all_customers_win, self.employeeId)
    
  
  def create_new_customer(self):
    new_customer_win = Toplevel(self.master)
    customer = Customer(new_customer_win, self.employeeId)
  

  def save_customer_document(self):
    root = TK()
    save_document = CreateDocument(root, self.employeeId, self.customerId)
         
  def make_appointmnet(self):
    app_win = Toplevel(self.master)
    appointment = Appointment(app_win, self.employeeId, self.customerName, self.customerId)
  def show_all_appointments(self):
    show_all_appointments_win = Toplevel(self.master)
    show_all_appointments = ShowAllAppointments(show_all_appointments_win, self.employeeId)
    
  def upload_final_plan(self):
    upload_final_plan_win = Toplevel(self.master)
    create_plan=CreatePlan(upload_final_plan_win, self.employeeId, self.customerName, self.customerId, self.payment_status, self.rukhsah_status)     
   

# def main():
#   root = Tk()
#   secretary = Secretary(root)
#   root.mainloop()
  
# if __name__ == "__main__": main()