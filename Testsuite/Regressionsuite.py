import os
import sys
import unittest

dir_path = os.path.dirname(os.path.realpath(__file__))
folder_path = os.path.abspath(os.path.join(dir_path,os.pardir))

sys.path.insert(0,folder_path+'\Library')
sys.path.insert(0,folder_path+'\Testscripts')

from HTMLTestRunner import HTMLTestRunner

from testcaseNo100001 import TestcaseNo100001

suite = unittest.TestSuite()
#Collecting as a suite

suite.addTest(TestcaseNo100001('test_TestcaseNo100001'))

outfile = file(folder_path+'\Regressionreport\Regressionreport.html','w+')

runner = HTMLTestRunner(stream=outfile,verbosity=1, title='DeltaX', description='Regressionreport',dirTestScreenshots=folder_path+'\Screenshots')

runner.run(suite)

outfile.close()
