import os
import shutil

from_dir = "/Users/amitnaik/Download"
to_dir = "/Users/amitnaik/Downloads/FolderForPro102"

dir_tree = {
    "Image_Files": [".pdf"],
    "Video_Files": [".pdf"],
    "Document_Files":[".pdf"],
    "Setup_Files":[".pdf"]
    
}
 
if extension in ['.txt', '.pdf', '.doc', '.docx']:
    path1 = "/Users/amitnaik/Download"
    path2 = "/Users/amitnaik/Downloads/FolderForPro102"
    path3 = "/Users/amitnaik/Downloads/FolderForPro102/Video_Files"
    if os.path.exists(path2):
        print("moving+file_name" + "...")
        shutil.move(path1, path3)
    else:
        os.makedirs(path2)
        print("moving + file_name"+ "...") 
        shutil.move(path1, path3)
    


