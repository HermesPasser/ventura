import hzip
import hweb
import hxml

# passar isso por agumento junto com o xml_url and file_name
VERSION = 0.1

def main():
	
	# download and read xml
	xml_url = 'https://gist.githubusercontent.com/HermesPasser/c0bad2f954eb8c0d7783e19952666d45/raw/b69f364c7047a3cf7ee16c09d50c617dc3ff885c/update.xml'
	xml_text = hweb.get_page(xml_url)
	
	# look for newest version (i need to compare and store the current version of the project)
	
	# delete files
	# hxml.
	
	# download the zip file
	download_url = 'https://github.com/HermesPasser/HermesPasser.github.io/blob/master/downloads/HermesMangaDownloader.zip?raw=true'
	file_name	= 'folder1\\folder2\\file.zip'
	# hweb.download(download_url, file_name)
	
	# unzip file
	
	
if __name__ == '__main__':
	main()
