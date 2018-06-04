import unittest
import sys
sys.path.append('..')

import tests_hpath
import tests_hxml

if __name__ == '__main__':
	suite = unittest.TestLoader().loadTestsFromModule(tests_hpath)
	unittest.TextTestRunner(verbosity = 2 ).run(suite)

	suite = unittest.TestLoader().loadTestsFromModule(tests_hxml)
	unittest.TextTestRunner(verbosity = 2 ).run(suite)
