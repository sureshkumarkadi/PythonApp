from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.chrome.options import Options


import os
import sys

#Current Working Folder
dir_path = os.path.dirname(os.path.realpath(__file__))

#Getting Parent of current working folder
folder_path = os.path.abspath(os.path.join(dir_path,os.pardir))

#Navigating to the desired folder
sys.path.insert(0,folder_path+'\Syslibrary')

#Importing module from Syslibrary
from datadriver import readjson

#Creating a Class object and instance of that object
jsonread1 = readjson()

class launchapplication():
    def intializebrowser(self):


        env = jsonread1.jsonread(folder_path+'\Env\setup.json')
        if env['browser'] == 'chrome':
            #intialize chrome browser
            browser = webdriver.Chrome(folder_path+'\Env\chromedriver.exe')
            browser.implicitly_wait(10)
            browser.maximize_window()
            return browser
        elif env['browser'] == 'firefox':
            #intialize firefox browser
            browser = webdriver.Firefox(folder_path+'\Env\geckodriver.exe')
            browser.implicitly_wait(10)
            browser.maximize_window()
            return browser
        elif env['browser']=='headlessChrome':
            #Intialize headless chrome browser
            chrome_options = Options()
            chrome_options.add_argument("--headless")
            chrome_options.add_argument("--window-size=1980*1080")
            chrome_driver = folder_path+'\Env\chromedriver.exe'
            browser = webdriver.Chrome(chrome_options = chrome_options,executable_path = chrome_driver)
            browser.implicitly_wait(10)
            return browser
        def closebrowser(self,browser):
            browser.close()

        def inputurl(self,browser):
            url = jsonread1.jsonread(folder_path+'\Env\setup.json')
            if url['url'] == 'prestagurl':
                prestagurl = jsonread1.jsonread(folder_path+'\Env\setup.json')
                browser.get(prestagurl['prestagurl'])
            elif url['url'] == 'stagurl':
                stagurl = jsonread1.jsonread(folder_path+'\Env\setup.json')
                browser.get(stagurl['stagurl'])

        def app_locators(self):
            app_locators = jsonread1.jsonread(folder_path+'\Objects\locators.json')
            return app_locators()

        def app_testdata(self):
            app_testdata = jsonread1.jsonread(folder_path+'\Data\TestData.json')
            return  app_testdata()

        def app_loginlink(self,browser,app_locators):
            loginlink = browser.find_element_by_xpath(app_locators('loginlink'))
            return loginlink()

