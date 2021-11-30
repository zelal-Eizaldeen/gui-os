import os
import subprocess

def display_cwd():
  cwd=os.getcwd()
  print("current working directory:", cwd)

def up_one_directory_level():
  os.chdir("../")
def display_entries_in_directory(directory):
  # os.listdir
  with os.scandir(directory) as entries:
    for entry in entries:
      print(entry.name)
def read_image():
  f = open('tour_logo.gif', 'rb')
  print(content)
  f.close()
def display_file():
  file_to_show = "tour_logo.gif"
  subprocess.call(["open", "-R", file_to_show])


if __name__ == "__main__":
  display_cwd()
  # up_one_directory_level()
  display_cwd()
  display_entries_in_directory("Document/")
  display_file()