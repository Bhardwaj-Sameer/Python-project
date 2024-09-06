import os
import shutil

def move_to(destination, file_name):
   
   #Creating the folder if it does not exists
   if not os.path.exists(destination):
      os.mkdir(destination)


   destination_path=os.path.join(destination,file_name)


   #Moving the files to designated folders
   shutil.move(file_name,destination_path)
   print(f"Moved:{file_name} to:{destination_path}")
