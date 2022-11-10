import os
from colorama import Fore, Style

"""Check Sync
Script to easily see where files are not syncronized between two folders.
(Google Drive syncronization with external drives sucks!)

"""
def printSuccess(msg):
    print(Fore.GREEN + msg)
    print(Style.RESET_ALL)

def printError(msg):
    print(Fore.RED + msg)
    print(Style.RESET_ALL)


# External hdd path with the files to backup
local='[LOCAL_PATH]'

# Cloud drive path
cloud='[CLOUD_PATH]'


# Loop sorted list of all root folders in $local ignoring hidden files 
for folder in sorted((f for f in os.listdir(local) if not f.startswith(".")), key=str.lower):
    # If files are included in root $local folder we check whether it exists in Cloud Drive 
    if os.path.isfile(os.path.join(local, folder)):
        if os.path.isfile(os.path.join(cloud, folder)):
            print(folder, 'present in both local and cloud  \n')
        else:
             printError(f"Error:  {folder} not present in cloud !!!\n")        
        continue

    print('Folder: ', folder)

    local_counter = 0
    for dirpath, dirnames, filenames in os.walk(local + folder):
        local_counter += len(filenames)

    cloud_counter = 0
    for dirpath, dirnames, filenames in os.walk(cloud + folder):
        cloud_counter += len(filenames)

    if local_counter == cloud_counter:
        printSuccess(f"Sync files: {local_counter} \n")
    else:
        printError(f"Error: Unsync files ==> Local: {local_counter}, Cloud:{cloud_counter} \n")    





