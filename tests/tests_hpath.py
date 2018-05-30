import unittest
from ventura._hpath import is_folder

class TestsHpath(unittest.TestCase):
	def test_if_is_folder(self):
		self.assertTrue(is_folder("folder\\"))
		
	def test_if_is_not_folder(self):
		self.assertFalse(is_folder("folder"))
		
	def test_if_is_a_file(self):
		self.assertFalse(is_folder("file.txt"))
		self.assertFalse(is_folder("file"))
	
	def test_if_is_not_a_file(self):
		self.assertTrue(is_folder("file.txt\\"))
		self.assertTrue(is_folder("file\\"))
