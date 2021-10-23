import os
import shutil
import time
def main ():
    deletedFolderCount = 0
    deletedFileCount = 0
    days = 30
    path = 'C:\\Users\\RIYA SHAJI\\Desktop\\Class 35'
    seconds = time.time() - (days*24*60*60)
    #if a unicodeescape error then, put double \
    #Check if the path exists 
    if os.path.exists(path):
        for root,dirs,files in os.walk(path):
            if seconds >= get_file_or_folder_age(path):
                remove_folder(root) 
                deletedFolderCount += 1
                break
            else:
                for folder in dirs:
                    folder_path = os.path.join(root,folder)
                    if seconds >= get_file_or_folder_age(folder_path):
                        remove_folder(folder_path) 
                        deletedFolderCount += 1
                for file in files:
                    filePath = os.path.join(root)
                    if seconds >= get_file_or_folder_age(filePath):
                        remove_file(filePath) 
                        deletedFileCount += 1
        else:
            if seconds >= get_file_or_folder_age(path):
                remove_file(path)
                deletedFileCount += 1
    else:
        print(f'"{path}" is not found')
        #deletedFileCount += 1
    print(f"Total folders deleted:", {deletedFolderCount})
    print(f"Total files deleted:", {deletedFileCount})



def remove_folder(path):
    if not shutil.rmtree(path):
        print(f"{path} is removed.")
    else:
        print(f"Cannot remove" +path)

def remove_file(path):
    if not os.remove(path):
        print(f"{path} is removed.")
    else:
        print(f"Cannot remove" +path)

def get_file_or_folder_age(path):
    ctime = os.start(path).st_ctime
    return ctime

if __name__ == '__main__':
    main()