import os
import PyPDF2
from pathlib import Path



def make_output_dir(customerId):
  global directory
  global parent_dir
  global path
  directory = "customer_appointments/{}".format(customerId)
  if not os.path.isdir(directory):
    os.makedirs(directory)
  parent_dir=os.getcwd()
  path = os.path.join(parent_dir, directory)
  
  
def save_customer_appointments(employeeId, customerName, customerId, date):
  # filename_civilId = "civilId.png"
  file_path = os.path.join(path, "appointment")
  if not os.path.isdir(path):
    os.mkdir(path)

  file = open(file_path, "w") 
  file.write("employeeId: {}, customerName: {}, customerPhone: {}, date: {}".format(employeeId, customerName, customerId, date))
  file.close()

