import pathlib
import os

def create_dir(dir):	
	dir = os.path.dirname(dir)
	if dir == '':
		return
	
	path = pathlib.Path(dir)
	path.mkdir(parents = True, exist_ok = True) 
