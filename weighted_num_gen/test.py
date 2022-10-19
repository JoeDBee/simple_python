from .RandomGen import RandomGen
import unittest
import random


class TestMethods(unittest.TestCase):
	"""Test Methods in RandomGen class"""

	def setUp(self):
		self.nums = [random.randint(0, 100) for i in range(10)]
		self.generator = RandomGen(self.nums, self.nums)

	def tearDown(self):
		del self.generator
		del self.nums

	def test_normalise(self):
		"""Test given weights are normalised correctly"""
		assert(sum(self.generator.normalise_weights(self.nums)) == 1)

	def test_selection(self):
		"""Test weighted selection algorithm returns weighted random number correctly"""
		weights = self.generator.normalise_weights(self.nums)
		assert(self.generator.weighted_selection(weights[0]) == self.nums[0])


class TestException(unittest.TestCase):
	"""Test exceptions raised correctly in RandomGen class"""
	def setUp(self):
		self.nums = [random.randint(0, 100) for i in range(10)]
		self.weights = self.nums

	def tearDown(self):
		del self.nums
		del self.weights

	def test_inputs_not_equal(self):
		"""Test value error assertion raised if object args are not equal in length"""
		self.weights = self.weights + [1]
		self.assertRaises(ValueError, RandomGen, self.nums, self.weights)

	def test_negative_weight(self):
		"""Test value error assertion raised if negative weight supplied"""
		self.weights[0] = -1
		self.assertRaises(ValueError, RandomGen, self.nums, self.weights)


if __name__ == '__main__':
	unittest.main()

