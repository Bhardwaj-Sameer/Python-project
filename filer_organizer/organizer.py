import os
from utils import moveTo

os.chdir('D:/Clutter')


#Creating an empty directory to store file and extension pairs
list_of_files={}


#Default if anything without an extension comes up, maybe a directory
destination='Others'



#Storing filename and extension separately in the dictionary
for files in os.listdir():
  full_name=files
  

  #Assigning folders to different extensions
  file_name,file_extension=os.path.splitext(files)
  if file_extension=='.exe':
        destination="App"

  elif file_extension=='.pdf':
        destination="Doc"

  elif file_extension=='.png':
        destination="Img"

  elif file_extension=='.txt':
        destination="Doc"

  elif file_extension=='.mp3':
        destination="Music"


#Sending the folder name and file name as arguements 
  moveTo(destination,full_name)
      


  

