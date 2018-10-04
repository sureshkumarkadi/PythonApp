import unittest
import os
import sys
import traceback
import time
from selenium.webdriver.common.keys import Keys

dir_path = os.path.dirname(os.path.realpath(__file__))
folder_path = os.path.abspath(os.path.join(dir_path,os.pardir))

sys.path.insert(0,folder_path+'\Syslibrary')
sys.path.insert(0,folder_path+'\Library')

from datadriver import readjson
jsonread1 = readjson()

tf = 'test_TestcaseNo100001'

from Launchapplicaton import launchapplication
application = launchapplication()

class TestcaseNo100001(unittest.TestCase):
    def test_TestcaseNo100001(self):
        try:

            browser = application.intializebrowser()
            application.inputurl(browser)
            login_locators = application.app_locators()

            uid = browser.find_element_by_xpath(login_locators['loginlink'])
            if uid.is_displayed():
                print 'pass'
            else:
                self.fail('Element Not Found')

        except Exception:
            traceback.print_exc()
            browser.save_screenshot(folder_path+'\Screenshots\Testcase-%s.png,%tf')
            self.fail("Test Case No 100001 is Failed")
        finally:
            application.closebrowser(browser)
if __name__ == '__main__':
    unittest.main()





