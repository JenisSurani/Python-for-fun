import os

def clearTheClutter(extension:str,directory:str)->None:
    
    extension=extension.strip()
    extension=extension.lower()
    
    # if user give extemsion as like .jpg remove . first
    if extension.startswith("."):
        extension=extension.replace(f"{extension}",f"{extension[1:]}")
        
        
    
    # first collect all the file with the extension given by the user from the folder
    filesInFolder= [file for file in os.listdir(directory) if file.endswith(f".{extension}")]
    
    # now you have all the file with given extension as list and each member as string itself
    
    # now sort the files if you can
    filesInFolder.sort()
    
    
    # now for renaming a file
    
    for index,file in enumerate(filesInFolder,start=1):
        
        # we have created the new file names 
        new_name=f"{index}.{extension}"
        
        # now we need the path
        #  ex your directory path is C:/Users/Pictures and your file name is abc.jpg
         
        old_path=os.path.join(directory,file) # C:/Users/Pictures/abc.jpg
        new_path=os.path.join(directory,new_name) # C:/Users/Pictures/1.jpg
        
        # now it may be happen that cureent directory have 1.jpg already
        
        if os.path.exists(new_path):
            print(f"Skipping the current {file} because {new_name} already exist in the directory")
        else:
            # if not rename the file
            os.rename(old_path,new_path)
            print(f"{file} → {new_name}")
            

# Give your extension here and valid directory path for clear the clutter in your directory for example.. 
# clearTheClutter("          .jpg              ","D:\Coding\Python_for_temp\ClearMe")


# Author : Jenis Surani
# Topic  : ClearTheClutter
# Date   : 21/02/2025
        
        
    
    

    