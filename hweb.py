import urllib.request as req
import hio
import os

def download(url, file_name):
	response = req.urlopen(url)
	
	# Create folders if need
	hio.create_dir(file_name)
	
	file = open(file_name,'wb')
	file.write(response.read()) 
	file.close()

def get_page(url):
	response = req.urlopen(url)
	return response.read().decode("utf8")