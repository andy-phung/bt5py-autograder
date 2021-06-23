import unittest
from importlib import import_module # https://stackoverflow.com/questions/8790003/dynamically-import-a-method-in-a-file-from-a-string

# temp notes: 
# - make sure to remove code from github after uploading to pypi
# - use unittest
# - pull from python_i scripts to match obj name and pull unit test classes (i.e. define a pair lists (input and output), then run a for loop in a method in a class for a prob)
# - remember to handle all common exceptions, ofc

def grade(obj, pset_num):
  """
  Takes in a function/object/class/whatever, matches the string name, and runs the corresponding tests. If the script passes all tests, a unique code will be provided
  If a test fails, return the output of that test or the exception raised 
  """
  test = getattr(import_module('python_i.pset' + str(pset_num)), str(obj.__name__)) # import matching unit test
  unittest.main()