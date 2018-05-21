#!/usr/bin/python
from hxml import VenturaXML
import hzip
import hweb
import hio
import sys

# pass file directory?

def update_if_is_need(version, xml_url):
	# download and read xml
	xml_text = hweb.get_page(xml_url)
	
	# setup xml
	ventura = VenturaXML(xml_text, version)
	
	# Check if need to update
	if ventura.is_updated():
		return False
		
	# delete files
	hio.delete_files(ventura.get_files_to_delete())
	
	# download the zip file
	hweb.download(ventura.get_link(), 'update.zip')
	
	# unzip file
	hzip.extract('update.zip', '')
	
	return True
	
def main():
	if len(sys.argv) == 3:
		update_if_is_need(float(sys.argv[1]), sys.argv[2])
	else:
		print('Ventura by Hermes Passer')
		print('\targ one : version')
		print('\targ two : xml link')
	
if __name__ == '__main__':
	main()
