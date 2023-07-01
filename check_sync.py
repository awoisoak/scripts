import os, sys
from colorama import Fore, Style

""" Check Sync
Script to easily see which files are not syncronized between two folders.
(Google Drive syncronization with external drives sucks!)
This script will ignore hidden files (the ones started by a dot)

1) Fill $local_root with the local folder path and $cloud_root with the cloud folder path

To check everything simply execute the script (ex. python3 check_sync.py) 
To check a specific folder just pass its relative path (respect $local_root) as a parameter (ex. python3 check_sync.py my/SubFolder/path)

"""
def printSuccess(msg):
    print(Fore.GREEN + msg)
    print(Style.RESET_ALL)

def printError(msg):
    print(Fore.RED + msg)
    print(Style.RESET_ALL)


# External hdd path with the files to backup
# ex. local_root = r'/Volumes/xxx/Photos/'
local_root = r'[LOCAL_PATH]'

# Cloud drive path
# ex. cloud_root = r'/Users/xxx/Library/CloudStorage/GoogleDrive-xxx@gmail.com/My Drive/Photos/'
cloud_root = r'[ROOT_PATH]'

if len(sys.argv) == 2:
    subpath= sys.argv[1] if sys.argv[1].endswith('/') else sys.argv[1] +'/'
    local_root = os.path.join(local_root, subpath)
    cloud_root = os.path.join(cloud_root, subpath)
    if os.path.exists(local_root) == False:
        printError(f'{local_root} is not a valid directory')
        quit()

# Loop sorted list of all root items in $local ignoring hidden files 
# First will check the number of files, if they are the same it will assume everything is sync correxctly
# If number of files do not match it will prompt the unsync files
for item in sorted((f for f in os.listdir(local_root) if not f.startswith(".")), key=str.lower):
    local_path = os.path.join(local_root, item)
    cloud_path = os.path.join(cloud_root, item)
    # If files are included in root $local folder we check whether it exists in Cloud Drive 
    if os.path.isfile(local_path):
        if os.path.isfile(cloud_path) == False: 
            printError(f"Error: root file {item} not present in cloud !!!\n")        
        continue

    print('Folder: ', item)

    local_counter = 0
    for dirpath, dirnames, filenames in os.walk(local_path):
        filtered_files = [x for x in filenames if not x.startswith(".")]
        local_counter += len(filtered_files)

    cloud_counter = 0
    for dirpath, dirnames, filenames in os.walk(cloud_path):
        filtered_files = [x for x in filenames if not x.startswith(".")]
        cloud_counter += len(filtered_files)

    if local_counter == cloud_counter:
        printSuccess(f"Sync files: {local_counter} \n")
    else:  
        printError(f"Unsync files ==> Local: {local_counter}, Cloud:{cloud_counter}")       
        if cloud_counter > local_counter:
            printError(f"Error! {cloud_counter - local_counter} more file(s) in cloud than in local (duplicated)? Check them below:")  
        elif cloud_counter != 0: 
            printError(f"Error! {local_counter - cloud_counter} files are missing in cloud folder. Check them below: ")  

        for dirpath, dirnames, files in os.walk(local_root + item):    
            # print(f'Subfolder: {dirpath}')
            localfiles = [x for x in files if not x.startswith(".")]
            subpath = dirpath.replace(local_root,'')
            cloud_subpath = os.path.join(cloud_root, subpath)    

            # If folder does not exist in cloud report it and continue
            if os.path.exists(cloud_subpath) == False:
                printError(f"Error! Folder does not exist in cloud: {subpath}")
                continue


            cloudfiles = [x for x in os.listdir(cloud_subpath) if os.path.isfile(os.path.join(cloud_subpath, x)) and not x.startswith(".")]
            set_dif = set(localfiles).symmetric_difference(set(cloudfiles))
            for x in list(set_dif): # The list could be empty (When the subpath might be correclty sync)
                    printError(f'diff: {subpath + "/" + x}') 

                

            



