import os
import PyPDF2
from pathlib import Path



def make_output_dir(customerId):
  global directory
  global parent_dir
  global path
  directory = "customer_rukhsah/{}".format(customerId)
  if not os.path.isdir(directory):
    os.makedirs(directory)
  parent_dir=os.getcwd()
  path = os.path.join(parent_dir, directory)
  
  
  
def save_customer_rukhsah(employeeId, customerName,customerId, rukhsah_status, rukhsah_name, rukhsah_blobData, created_at):
  
  # filename_civilId = "civilId.png"
  filename_rukhsah = (os.path.basename(rukhsah_name))
  file_path_rukhsah = os.path.join(path, filename_rukhsah)
  if not os.path.isdir(path):
    os.mkdir(path)
 
  file = open(file_path_rukhsah, "wb") 
  file.write(rukhsah_blobData)
  file.close()
#---------save info ----------------
  
  file_path = os.path.join(path, "rukhsah_info")
  file = open(file_path, "w") 
  file.write("employeeId: {}, customerName: {}, customerPhone: {}, date: {}".format(employeeId, customerName, customerId,created_at))
  file.close()


