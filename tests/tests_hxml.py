import unittest
from ventura._hpath import load_file
from ventura._hxml import VenturaXML

class TestsHxml(unittest.TestCase):
	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.xml = load_file('mock_xml_file.xml')
	
	def test_get_last_version_url(self):
		ventura = VenturaXML(self.xml, 0.1)
		self.assertEqual(ventura.get_link(), 'https://hermespasser.github.io')
	
	def test_get_last_version_files_to_delete(self):
		ventura = VenturaXML(self.xml, 0.1)
		self.assertEqual(ventura.get_files_to_delete(), ["folder\\", 'file.txt'])
	
	def test_if_is_updated(self):
		ventura = VenturaXML(self.xml, 0.4)
		self.assertTrue(ventura.is_updated())
		
	def test_if_is_not_updated(self):
		ventura = VenturaXML(self.xml, 0.1)
		self.assertFalse(ventura.is_updated()) 
