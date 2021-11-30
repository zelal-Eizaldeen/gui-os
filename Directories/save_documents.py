import os
import PyPDF2
from pathlib import Path


def split_civilId_name(filename):
  civilId_file = (os.path.basename(filename))
def make_output_dir(customerId):
  global directory
  global parent_dir
  global path
  directory = "customer_documents/{}".format(customerId)
  if not os.path.isdir(directory):
    os.makedirs(directory)
  parent_dir=os.getcwd()
  path = os.path.join(parent_dir, directory)
  
  
  # dir_path = Path("customer_documents/")
  # dir_path.mkdir(exist_ok=True)
  # dir_path = os.path.join(dir_path, customerId)
  
def save_documents(civilId, filename_civilId, possesPaper, filename_possesPaper, publicLocation, filename_publicLocation):
  # filename_civilId = "civilId.png"
  filename_civilId = (os.path.basename(filename_civilId))
  file_path_civilId = os.path.join(path, filename_civilId)
  if not os.path.isdir(path):
    os.mkdir(path)
 
  file = open(file_path_civilId, "wb") 
  file.write(civilId)
  file.close()
#---------save Posses papers into local disk
  filename_possesPaper = (os.path.basename(filename_possesPaper))
  file_path_possessPaper = os.path.join(path, filename_possesPaper)
  file = open(file_path_possessPaper, "wb") 
  file.write(possesPaper)
  file.close()
#------------save public location into local disk
  filename_publicLocation = (os.path.basename(filename_publicLocation))
  file_path_publicLocation = os.path.join(path, filename_publicLocation)
  file = open(file_path_publicLocation, "wb") 
  file.write(publicLocation)
  file.close()


# def read_pdf(pdfname_file):
#   with open(pdfname_file, 'r+b') as f:
#     reader=PyPDF2.PdfFileReader(f)
 


def print_directory_contents():
  entries = Path.cwd()


  # entries = Path('images/')
  # entries = Path.home()

