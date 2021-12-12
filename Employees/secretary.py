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
from Task.task_template import *


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
    self.year = datetime.date.today().year
    self.month = datetime.date.today().month
    self.day = datetime.date.today().day
   
    self.structural_engineer_id = "Structural Engineer"
    
    self.master.title('Secretary')
    self.master.geometry("{0}x{1}+0+0".format(self.master.winfo_screenwidth(), self.master.winfo_screenheight()))
    
    self.master.configure(background = '#e1d8b9')

    self.style = ttk.Style()
    self.style.configure('TFrame', background = '#e1d8b9')
    self.style.configure('TButton', background = '#e1d8b9')
    self.style.configure('TLabel', background = '#e1d8b9', font = ('Arial', 11))
    self.style.configure('Header.TLabel', font = ('Arial', 14, 'bold'))
    
    # self.panedwindow = ttk.Panedwindow(self.master, orient = HORIZONTAL)
    self.panedwindow = ttk.Panedwindow(self.master, orient = VERTICAL)

    self.panedwindow.pack(fill = BOTH, expand = True)
    self.frame_header = ttk.Frame(self.panedwindow, width =100, height=300, relief=SUNKEN)
    self.frame_task = ttk.Frame(self.panedwindow, width =50, height=400, relief=SUNKEN)
    self.frame_alert_appointments = ttk.Frame(self.panedwindow, width =400, height=400, relief=SUNKEN)



    self.panedwindow.add(self.frame_header, weight = 1)
    self.panedwindow.add(self.frame_task, weight = 3)
    self.panedwindow.add(self.frame_alert_appointments, weight = 2)




    ttk.Button(self.frame_header,  text = 'Refresh', command=self.refresh ).grid(row=0, column=0, sticky='wn') 
    ttk.Button(self.frame_header, text = 'Tasks', command=self.view_all_tasks).grid(row = 0, column= 1,   padx= 10, pady=20)
    ttk.Button(self.frame_header, text = 'Create New Customer', command=self.create_new_customer).grid(row = 0, column= 2,   padx= 10, pady=20)
    ttk.Button(self.frame_header, text = 'Show Customers', command=self.show_customers).grid(row = 0, column= 3, padx= 10, pady=20 )
    ttk.Button(self.frame_header, text = 'Make Appointment', command=self.make_appointmnet).grid(row = 0, column= 4,  padx = 10, pady=20)
    ttk.Button(self.frame_header, text = 'Show All Appointments', command=self.show_all_appointments).grid(row = 0, column= 5,  padx = 10, pady=20)
    ttk.Button(self.frame_header, text = 'Upload Final Plan', command=self.upload_final_plan).grid(row = 0, column= 6,  padx = 10, pady=20)
   
    ttk.Label(self.frame_task, text = 'All Tasks: ' ).grid(row = 1, column = 0, padx = 5, sticky='sw')
    self.list_tasks=Listbox(self.frame_task, height=16,width=60)
    self.list_tasks.grid(row=2,column=1,rowspan=6,columnspan=2)
    
    scrollbar_tasks=ttk.Scrollbar(self.frame_task)
    scrollbar_tasks.grid(row=2, column=3, rowspan=6)

    self.list_tasks.config(yscrollcommand=scrollbar_tasks.set)
    scrollbar_tasks.config(command=self.list_tasks.yview)
    self.list_tasks.bind('<<ListboxSelect>>',self.get_selected_task)
    ttk.Button(self.frame_task, text = 'Delete Task', command=self.delete_task).grid(row = 3, column= 5,   padx= 10, pady=20)

    ttk.Label(self.frame_alert_appointments, text = 'Appointments for tomorrow: ' ).grid(row = 1, column = 0, padx = 5, sticky='sw')
    ttk.Button(self.frame_alert_appointments, text = 'View Tomorrow\'s Appointment', command=self.view_urgent_appointments).grid(row = 2, column= 0,   padx= 10, pady=20)

    self.list_appointments=Listbox(self.frame_alert_appointments, height=16,width=60)
    self.list_appointments.grid(row=2,column=1,rowspan=6,columnspan=2)  
    scrollbar_appointments=ttk.Scrollbar(self.frame_alert_appointments)
    scrollbar_appointments.grid(row=2, column=3, rowspan=6)
    self.list_appointments.config(yscrollcommand=scrollbar_appointments.set)
    scrollbar_appointments.config(command=self.list_appointments.yview)
    self.list_appointments.bind('<<ListboxSelect>>',self.get_selected_appointment)

    ttk.Button(self.frame_alert_appointments, text = 'Delete appointment', command=self.delete_appointment).grid(row = 3, column= 5,   padx= 10, pady=20)



  def refresh(self):
    self.master.destroy()
    root=Tk()
    self.__init__(root, self.employeeId, self.payment_status, self.rukhsah_status)


  def get_selected_appointment(self,event):
        self.index_app=self.list_appointments.curselection()[0]
        self.selected_tuple_app=self.list_appointments.get(self.index_app)
        self.appId = self.selected_tuple_app[3]
       
  def view_urgent_appointments(self):
    self.list_appointments.delete(0,END)
    for row in database.view_all_sec_appointments():
      target_date = datetime.datetime.strptime(row[2],'%d-%m-%Y')
      # today = datetime.datetime.strptime(self.created_at, '%Y-%m-%d %H:%M:%S.%f')
      # print(abs((target_date - today).days))
      if (abs(target_date.day - self.day) == 1):
         self.list_appointments.insert(END,row)
         self.customerId = row[0]
         self.customerName = row[1]
         self.date = row[2]
        
      else:
        print("NOOO")
       
      
  def delete_appointment(self):     
    database.delete_appointment(self.customerId)
    self.list_appointments.delete(self.index_app)
  
  def get_selected_task(self,event):
        self.index=self.list_tasks.curselection()[0]
        self.selected_tuple=self.list_tasks.get(self.index)
        self.taskId = self.selected_tuple[3]
       
       
  def view_all_tasks(self):
    self.list_tasks.delete(0,END)
    for row in database.view_tasks(self.employeeId):
      self.list_tasks.insert(END,row)
      self.customerName = row[1]
      self.customerId = row[2]
  def delete_task(self):     
    database.delete_task(self.customerId)
    self.list_tasks.delete(self.index)

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
   
  
  
    # self.panedwindow.insert(1, self.frame_task, weight = 4)
    # self.panedwindow.forget(1)



    # self.frame_header = ttk.Frame(master)
    # self.frame_header.pack()
    # ttk.Label(self.frame_header, style='Header.TLabel', text = "Secretary").grid(row=3, column=1, rowspan=2)


    
    # self.frame_content = ttk.Frame(master)
    # self.frame_content.pack()
    # self.frame_content.config(height = 100, width=200)


    # ttk.Button(self.frame_content, text = 'Tasks', command=self.view_tasks).grid(row = 0, column= 1,   padx= 10, pady=20)

    # ttk.Button(self.frame_content, text = 'Create New Customer', command=self.create_new_customer).grid(row = 1, column= 1,   padx= 10, pady=20)
    # ttk.Button(self.frame_content, text = 'Show Customers', command=self.show_customers).grid(row = 2, column= 1, padx= 10, pady=20 )

    # ttk.Button(self.frame_content, text = 'Make Appointment', command=self.make_appointmnet).grid(row = 3, column= 1,  padx = 10, pady=20)
    # ttk.Button(self.frame_content, text = 'Show All Appointments', command=self.show_all_appointments).grid(row = 4, column= 1,  padx = 10, pady=20)
    # ttk.Button(self.frame_content, text = 'Upload Final Plan', command=self.upload_final_plan).grid(row = 5, column= 1,  padx = 10, pady=20)
    

   
    # self.alert_payment()
    # self.alert_rukhsah()
  
    
  # def alert_payment(self):
  #   row = database.view_payments()
  #   for payment in row:
  #     if(payment[6] == 1):
  #       self.employeeId = payment[1]
  #       self.customerName = payment[2]
  #       self.customerId = payment[3]
  #       self.payment_status = payment[6]    
        # messagebox.showinfo(title = "Payment", message = "Make a Payment for customer:{} with phone number {}".format(self.customerName,self.customerId))
        # payment_win = Toplevel(self.master) 
        # payment = Payment(payment_win, self.employeeId, self.customerName, self.customerId,self.payment_status)
        
  # def alert_rukhsah(self):
  #   row = database.view_rukhsahs()
  #   for rukhsah in row:
  #     if(rukhsah[5] == 1):
  #       self.employeeId = rukhsah[1]
  #       self.customerName = rukhsah[2]
  #       self.customerId = rukhsah[3]
  #       self.rukhsah_status = 1
        # messagebox.showinfo(title = "Rukhsah", message = "Make Rukhsah for customer:{} with phone number {}".format(rukhsah[2],rukhsah[3]))
        # rukhsah_win = Toplevel(self.master) 
        # rukhsah = Rukhsah(rukhsah_win, self.employeeId, self.customerName, self.customerId,self.payment_status, self.rukhsah_status)
        

  

