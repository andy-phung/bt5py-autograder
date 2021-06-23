
import unittest

class PsetTest(unittest.TestCase):
  test_inputs = [1, 2, 3, 4]
  test_outputs = [5, 6, 7, 8]
  def test_func(self):
    for idx, i in enumerate(test_inputs):
      self.assertEqual(obj(test_inputs[idx]), test_outputs[idx])
  
