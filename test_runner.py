# test_runner.py
import unittest
from test_simplecaesar import SCCipherTest
if __name__ == '__main__':
# load suite and start runner
  suite = unittest.TestLoader().loadTestsFromTestCase(SCCipherTest)
  unittest.TextTestRunner(verbosity = 2).run(suite)
