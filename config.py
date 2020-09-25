import category as cat

CATEGORY_OBJECT = {}
####################################################################
FOLDER_TO_ORGANIZE = "Downloads"

################## ADD ALL FILES TO CONSIDER HERE ##################################

FILES_TO_CONSIDER = {
						"VIDEO" : [".mp4",".mkv", ".webm"],
						"AUDIO" : [".mp3"],
						"DOCUMENTS" : [".pdf", ".doc", ".docx", "PDF", ".odt"],
						"HTMLFILES" :[".html"],
						"PRESENTATIONS" : [".pptx", ".ppt", ".odp"],
						"JSONFILES":[".json"],
						"TEXTFILES" : [".txt"],
						"ExcelSheets" : [".xlsx", ".xls",".ods"],
						"certificates" : [".crt"],
						"DATASETS" : [".csv"],
						"COMPRESSED" : [".zip",".gz",".rar",".tgz",".bz2", ".tar", ".7z"],
						"IMAGES" : [".jpg",".png",".JPG", ".jpeg", ".tif"],
						"SQLFILES" : [".sql"],
						"JAVA_LIBRARY_FILES" : [".jar"],
						"PYTHON_PROGRAMS" : [".py"],
						"JAVASCRIPT_PROGRAMS" : [".js"],
						"INSTALLERS" : [".deb",".exe",".run", ".AppImage"],
						"TORRENT" : [".torrent"],
						"E_BOOKS" : [".epub",".mobi"],
						"DISC_IMAGES" : [".iso"]
						}

##########################################################################

for ct in FILES_TO_CONSIDER:
	CATEGORY_OBJECT[ct] = cat.Category(ct,FILES_TO_CONSIDER[ct])