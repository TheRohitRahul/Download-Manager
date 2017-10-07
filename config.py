import category as cat

CATEGORY_OBJECT = {}
####################################################################
FOLDER_TO_ORGANIZE = "Downloads"

################## ADD ALL FILES TO CONSIDER HERE ##################################

FILES_TO_CONSIDER = {
						"VIDEO" : [".mp4",".mkv"],
						"AUDIO" : [".mp3"],
						"DOCUMENTS" : [".pdf",".ods"],
						"DATASETS" : [".csv"],
						"COMPRESSED" : [".zip",".gz",".rar",".tgz","bz2"],
						"IMAGES" : [".jpg",".png",".JPG"],
						"JAVA_LIBRARY_FILES" : [".jar"],
						"PYTHON_PROGRAMS" : [".py"],
						"JAVASCRIPT_PROGRAMS" : [".js"],
						"INSTALLERS" : [".deb",".exe",".run"],
						"TORRENT" : [".torrent"],
						"E_BOOKS" : [".epub",".mobi"],
						"DISC_IMAGES" : [".iso"]
						}

##########################################################################

for ct in FILES_TO_CONSIDER:
	CATEGORY_OBJECT[ct] = cat.Category(ct,FILES_TO_CONSIDER[ct])