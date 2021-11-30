from tkinter import *
from tkinter import ttk
from tkinter import messagebox



class Feedback:
  def __init__(self, master):
   
    master.title('Explore')
    master.resizable(False, False)
    master.configure(background = 'red')
    self.frame_header = ttk.Frame(master)
    self.frame_header.pack()
    # self.master.resizable(False, False)
    # self.master.state('zoomed')
    # self.master.geometry('800x800+300+300')
    # self.master.geometry("{0}x{1}+0+0".format(self.master.winfo_screenwidth(), self.master.winfo_screenheight()))


    self.style = ttk.Style() 
    self.style.configure('TFrame', background = '#e1d8b9')
    self.style.configure('TButton', background = '#e1d8b9')
    self.style.configure('TLabel', background = '#e1d8b9', font = ('Arial', 11))
    self.style.configure('Header.TLabel', font = ('Arial', 18, 'bold'))      

    

    self.logo = PhotoImage(file='tour_logo.gif')
    ttk.Label(self.frame_header, image = self.logo).grid(row = 0, column = 0, rowspan=2)
    ttk.Label(self.frame_header, style='Header.TLabel', text = "Thanks for Exploring").grid(row=0, column =1)
    ttk.Label(self.frame_header, wraplength=300, text = ("We're glad you choose Explore Kuwait for your adventure. "
                                         "Please tell us what you thought about the 'Desert to Sea' tour.")).grid(row=1,column=1)
    self.frame_content = ttk.Frame(master)
    self.frame_content.config(style='TFrame')
    self.frame_content.pack()

    ttk.Label(self.frame_content, text = 'Name: ').grid(row = 0, column = 0, padx = 5, sticky='sw')
    ttk.Label(self.frame_content, text = 'Email: ').grid(row = 0, column = 1, padx = 5,sticky='sw')
    ttk.Label(self.frame_content, text = 'Comments: ').grid(row=2, column=0, padx = 5, sticky='sw')

    self.entry_name = ttk.Entry(self.frame_content, width = 24, font=('Arial, 10'))
    self.entry_email = ttk.Entry(self.frame_content, width = 24, font=('Arial, 10'))
    self.text_comments = Text(self.frame_content, width = 50, height = 10, font=('Arial, 10'))

    self.entry_name.grid(row=1, column=0, padx = 5)
    self.entry_email.grid(row=1, column=1, padx = 5)
    self.text_comments.grid(row=3, column=0, columnspan = 2, padx = 5)

    ttk.Button(self.frame_content, text = 'Submit', command=self.submit).grid(row=4, column=0, padx = 5, sticky='e')
    ttk.Button(self.frame_content, text = 'Clear', command=self.clear).grid(row=4, column=1, padx = 5, sticky='w')

  def submit(self):
    print('Name: {}'.format(self.entry_name.get()))
    print('Email: {}'.format(self.entry_email.get()))
    print('Comments: {}'.format(self.text_comments.get(1.0,END)))
    self.clear()
    messagebox.showinfo(title = "Explore Kuwait Feedback", message = "Comments Submited!")
  def clear(self):
    self.entry_name.delete(0,END)
    self.entry_email.delete(0,END)   
    self.text_comments.delete(1.0,END)  


def main():
  root = Tk()
  feedback = Feedback(root)
  root.mainloop()
if __name__ == "__main__": main()