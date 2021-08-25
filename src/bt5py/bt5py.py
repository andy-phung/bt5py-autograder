import unittest
from contextlib import contextmanager
from io import StringIO
import sys

@contextmanager
def captured_output():
    new_out, new_err = StringIO(), StringIO()
    old_out, old_err = sys.stdout, sys.stderr
    try:
        sys.stdout, sys.stderr = new_out, new_err
        yield sys.stdout, sys.stderr
    finally:
        sys.stdout, sys.stderr = old_out, old_err

class test_pset1(unittest.TestCase):
	codes = ["aha", None, None, None, None, None, None, None, None, None]

	def test_prob1(self):
		test_inputs = [(1, 2), (4, 3), (76, 64), (77, 77)]
		test_outputs = ["1 is under 2", "4 is over 3", "76 is over 64", "77 is the same as 77"]
		for idx, i in enumerate(test_inputs):
			with captured_output() as (out, err):
				self.obj(test_inputs[idx][0], test_inputs[idx][1])
				# This can go inside or outside the `with` block
				output = out.getvalue().strip()
				self.assertEqual(output, test_outputs[idx])

		print("Problem 1 Code (save this for later!): " + str(self.codes[0]))

	def test_prob2(self):
		test_inputs = [("Dog", 4), ("BT5", 5), ("Notion", 2), ("hellos", 1)]
		test_outputs = ["DogDogDogDog", "BT5BT5BT5BT5BT5", "NotionNotion", "hellos"]
		for idx, i in enumerate(test_inputs):
			with captured_output() as (out, err):
				self.obj(test_inputs[idx][0], test_inputs[idx][1])
				# This can go inside or outside the `with` block
				output = out.getvalue().strip()
				self.assertEqual(output, test_outputs[idx])
		print("Problem 2 Code (save this for later!): " + str(self.codes[1]))

	def test_prob3(self):
		test_inputs = [(14, 5), (64, 4), (1, 2), (2, 2)]
		test_outputs = ["14 15 16 17 18 19", "64 65 66 67 68", "1 2 3", "2 3 4"]
		for idx, i in enumerate(test_inputs):
			with captured_output() as (out, err):
				self.obj(test_inputs[idx][0], test_inputs[idx][1])
				# This can go inside or outside the `with` block
				output = out.getvalue().strip()
				self.assertEqual(output, test_outputs[idx])

		print("Problem 3 Code (save this for later!): " + str(self.codes[2]))

	def test_prob4(self):
		test_inputs = [(7, -20, 28), (4, 10, 20)]
		test_outputs = ["-14 -7 0 7 14 21 28", "12 16 20"]
		for idx, i in enumerate(test_inputs):
			with captured_output() as (out, err):
				self.obj(test_inputs[idx][0], test_inputs[idx][1], test_inputs[idx][2])
				# This can go inside or outside the `with` block
				output = out.getvalue().strip()
				self.assertEqual(output, test_outputs[idx])

		print("Problem 4 Code (save this for later!): " + str(self.codes[3]))

	def test_prob5(self):
		test_inputs = [()]
		test_outputs = ["3"]
		for idx, i in enumerate(test_inputs):
			with captured_output() as (out, err):
				self.obj() 
				# This can go inside or outside the `with` block
				output = out.getvalue().strip()
				self.assertEqual(output, test_outputs[idx])

		print("Problem 5 Code (save this for later!): " + str(self.codes[4]))

	def test_prob6(self):
		test_inputs = [(1, 4), (1, 5), (1,1)]
		test_outputs = ["o o o o", "o o o o o", "o"]
		for idx, i in enumerate(test_inputs):
			with captured_output() as (out, err):
				self.obj(test_inputs[idx][0], test_inputs[idx][1])
				# This can go inside or outside the `with` block
				output = out.getvalue().strip()
				self.assertEqual(output, test_outputs[idx])

		print("Problem 6 Code (save this for later!): " + str(self.codes[5]))

	def test_prob7(self):
		test_inputs = [2, 3, 4]
		test_outputs = ["1\n1", "1\n1\n2", "1\n1\n2\n3"]
		for idx, i in enumerate(test_inputs):
			with captured_output() as (out, err):
				self.obj(test_inputs[idx])
				# This can go inside or outside the `with` block
				output = out.getvalue().strip()
				self.assertEqual(output, test_outputs[idx])

		print("Problem 7 Code (save this for later!): " + str(self.codes[6]))

	def test_prob8(self):
		print("Not added yet")

	def test_prob9(self):
		print("Not added yet")

	def test_prob10(self):
		test_inputs = [(25), (0), (100)]
		test_outputs = ["3 4", "There are no such pairs of integers", "6 8"]
		for idx, i in enumerate(test_inputs):
			with captured_output() as (out, err):
				self.obj(test_inputs[idx][0])
				# This can go inside or outside the `with` block
				output = out.getvalue().strip()
				self.assertEqual(output, test_outputs[idx])

		print("Problem 10 Code (save this for later!): " + str(self.codes[9]))



class test_pset2:
	codes = [None, None, None, None, None, None, None, None, None, None]

class test_pset3:
	codes = [None, None, None, None, None, None, None, None, None, None]

class test_pset4:
	codes = [None, None, None, None, None, None, None, None, None, None]

class test_pset5:
	codes = [None, None, None, None, None, None, None, None, None, None]

class test_pset6:
	codes = [None, None, None, None, None, None, None, None, None, None]

class test_pset7:
	codes = [None, None, None, None, None, None, None, None, None, None]

class test_pset8:
	codes = [None, None, None, None, None, None, None, None, None, None]

class test_pset9:
	codes = [None, None, None, None, None, None, None, None, None, None]

psets = {
	1 : test_pset1,
	2 : test_pset2,
	3 : test_pset3,
	4 : test_pset4,  
	5 : test_pset5,
	6 : test_pset6,
	7 : test_pset7, 
	8 : test_pset8,
	9 : test_pset9
	}

def grade(pset_num, prob_num, obj):

	cl = psets[pset_num]

	singletest = unittest.TestSuite()
	cl.obj = obj
	singletest.addTest(cl('test_prob' + str(prob_num)))
	unittest.TextTestRunner().run(singletest)
