import json
import unittest

class readjson():
    def jsonread(self,filename):         # run time will provide the path
        with open(filename) as jsonfile: # opens the json object
            value = json.load(jsonfile)  # convers the json object into python object
            return value                 # returns Value