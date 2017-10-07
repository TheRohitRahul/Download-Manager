class Category:
	def __init__(self,catname,catextensions):
		self.category_name = catname
		self.folder_name = catname.title()
		self.category_extensions = catextensions

	def getName(self):
		return self.category_name
		
	def getFolderName(self):
		return self.folder_name

	def getCategoryExtensions(self):
		return self.category_extensions
