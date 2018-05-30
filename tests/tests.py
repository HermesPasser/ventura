import unittest
import sys
sys.path.append('..')

import tests_hpath
import tests_hxml

if __name__ == '__main__':
	print("\n\ttests_hpath:\n")
	suite = unittest.TestLoader().loadTestsFromModule(tests_hpath)
	unittest.TextTestRunner(verbosity = 2 ).run(suite)
	
	print("\n\ttests_hxml:\n")
	suite = unittest.TestLoader().loadTestsFromModule(tests_hxml)
	unittest.TextTestRunner(verbosity = 2 ).run(suite)
