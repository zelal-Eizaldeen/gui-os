import os
import PyPDF2
from pathlib import Path



def make_output_dir(customerId):
  global directory
  global parent_dir
  global path
  directory = "customer_plans/{}".format(customerId)
  if not os.path.isdir(directory):
    os.makedirs(directory)
  parent_dir=os.getcwd()
  path = os.path.join(parent_dir, directory)
  
  
  
def save_customer_plans(employeeId, customerName,customerId, type_plan, plan_name, plan_blobData, created_at):
  if not os.path.isdir(path):
    os.mkdir(path)
  filename_plan = (os.path.basename(plan_name))
  if type_plan == 'Architectural':
    arc_path_plan = os.path.join(path, filename_plan) 
    file = open(arc_path_plan, "wb") 
    file.write(plan_blobData)
    file.close()
    #---------save info ----------------
    arc_file_path = os.path.join(path, "arc_info")
    file = open(arc_file_path, "w") 
    file.write("employeeId: {}, customerName: {}, customerPhone: {}, type_of_plan: {}, date: {}".format(employeeId, customerName, customerId, type_plan,created_at))
    file.close()

  if type_plan == 'Structural':
    struc_path_plan = os.path.join(path, filename_plan) 
    file = open(struc_path_plan, "wb") 
    file.write(plan_blobData)
    file.close()
    struc_file_path = os.path.join(path, "struc_info")
    file = open(struc_file_path, "w") 
    file.write("employeeId: {}, customerName: {}, customerPhone: {}, type_of_plan: {}, date: {}".format(employeeId, customerName, customerId, type_plan,created_at))
    file.close()
  if type_plan == 'Accepted':
    acc_path_plan = os.path.join(path, filename_plan) 
    file = open(acc_path_plan, "wb") 
    file.write(plan_blobData)
    file.close()
    acc_file_path = os.path.join(path, "acc_info")
    file = open(acc_file_path, "w") 
    file.write("employeeId: {}, customerName: {}, customerPhone: {}, type_of_plan: {}, date: {}".format(employeeId, customerName, customerId, type_plan,created_at))
    file.close()
  if type_plan == 'Approved':
    app_path_plan = os.path.join(path, filename_plan) 
    file = open(app_path_plan, "wb") 
    file.write(plan_blobData)
    file.close()
    app_file_path = os.path.join(path, "app_info")
    file = open(app_file_path, "w") 
    file.write("employeeId: {}, customerName: {}, customerPhone: {}, type_of_plan: {}, date: {}".format(employeeId, customerName, customerId, type_plan,created_at))
    file.close()
  if type_plan == 'Final':
    final_path_plan = os.path.join(path, filename_plan) 
    file = open(final_path_plan, "wb") 
    file.write(plan_blobData)
    file.close()
    final_file_path = os.path.join(path, "acc_info")
    file = open(final_file_path, "w") 
    file.write("employeeId: {}, customerName: {}, customerPhone: {}, type_of_plan: {}, date: {}".format(employeeId, customerName, customerId, type_plan,created_at))
    file.close()
  
  
  
 
  


