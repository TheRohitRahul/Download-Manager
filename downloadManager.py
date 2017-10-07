import os
import config
import shutil


FOLDER_TO_ORGANIZE = config.FOLDER_TO_ORGANIZE
HOME_PATH = os.environ.get("HOME")
PATH_FOLDER_TO_ORGANIZE = os.path.join(HOME_PATH,FOLDER_TO_ORGANIZE)
dir_list = []
file_list = []
queue = []
folderStructure = {}
category_object = config.CATEGORY_OBJECT 

def make_relevent_folders():
	for ct in category_object:
		folder_name = category_object[ct].getFolderName()
		path_to_make = os.path.join(PATH_FOLDER_TO_ORGANIZE,folder_name)
		if(not os.path.exists(path_to_make)):
			os.mkdir(path_to_make)

def organize_folders():
	moved_flag = False
	for file_path in file_list:
		for ct in category_object:
			extensions = category_object[ct].getCategoryExtensions()
			if os.path.splitext(file_path)[1] in extensions:
				shutil.move(os.path.join(PATH_FOLDER_TO_ORGANIZE,file_path),os.path.join(os.path.join(PATH_FOLDER_TO_ORGANIZE,category_object[ct].getFolderName()),file_path))
				print "moved %s to %s"%(file_path,category_object[ct].getFolderName())
				moved_flag = True

	return moved_flag			

all_files = os.listdir(PATH_FOLDER_TO_ORGANIZE)

make_relevent_folders()
for file_name  in all_files:
	if(os.path.isdir(os.path.join(PATH_FOLDER_TO_ORGANIZE,file_name))):
		dir_list.append(file_name)
	else:
		file_list.append(file_name)
		
if(not organize_folders()):
	print "No known file to move"