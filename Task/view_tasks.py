from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from tkinter import filedialog
from tkcalendar import *
import os



from Backend.backend_db import Database



database=Database("Metra.db")

class ViewTasks:
  def __init__(self,master, employeeId):

    self.master = master
    self.employeeId = employeeId
    self.master.title('All Tasks')
    self.master.geometry('800x800+300+300')  
    self.master.configure(background = '#e1d8b9')

    self.style = ttk.Style()
    self.style.configure('TFrame', background = '#e1d8b9')
    self.style.configure('TButton', background = '#e1d8b9')
    self.style.configure('TLabel', background = '#e1d8b9', font = ('Arial', 11))
    self.style.configure('Header.TLabel', font = ('Arial', 18, 'bold'))
    self.frame_header = ttk.Frame(master)
    self.frame_header.pack()
    ttk.Label(self.frame_header, style='Header.TLabel', text = "View All Tasks").grid(row=0, column=1, rowspan=2)
    self.frame_content = ttk.Frame(master)
    self.frame_content.pack()

    ttk.Label(self.frame_content, text = 'All Tasks: ' ).grid(row = 0, column = 0, padx = 5, sticky='sw')
   
    self.list_tasks=Listbox(self.frame_content, height=800,width=800)
    self.list_tasks.grid(row=2,column=0,rowspan=6,columnspan=2)
  
    self.list_tasks.bind('<<ListboxSelect>>',self.get_selected_task)

  


    self.view_all_tasks()

  def get_selected_task(self,event):
        index=self.list_tasks.curselection()[0]
        self.selected_tuple=self.list_tasks.get(index)
        self.taskId = self.selected_tuple[3]
        print(self.taskId)

        


  def view_all_tasks(self):
    self.list_tasks.delete(0,END)
    for row in database.view_tasks(self.employeeId):
      self.list_tasks.insert(END,row)
      print(row)
  def delete_task(self):
    database.delete_task(self.taskId)

      
  # def view_document(self):
  #   root = Tk()
  #   show_document = ShowDocument(root, self.employeeId,self.customerId)
   
    
   
    

def main():
  root = Tk()
  show_all_customer = ShowAllCustomers(root)
  root.mainloop()
if __name__ == "__main__": main()