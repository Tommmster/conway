import unittest


def change(amount, coins=[1.0, 0.5, 0.25, 0.1, 0.05, 0.01]):
	"""
		For a given amount, returns a list using coins as change, using 
		bigger denominations first. Input should be a multiple of 0.01
		Possible elements of the list are 1, 0.5, 0.25, 0.1 ,0.05, 0.01
	"""

	change = []
	
	current=0
	while(round(amount,2)>=0.01):
		while (round(amount,2)>=(coins[current]) ):
			change.append(coins[current])
			amount -= coins[current]
		current+=1

	return change
	


class ChangeEngineTest(unittest.TestCase):

	def test_when_amount_is_fifty_should_return_fifty(self):
		self.assertEqual([0.5],change(0.5))

	def test_when_amount_is_1_should_return_1(self):
		self.assertEqual([1.00],change(1))
		
	def test_when_amount_is_75_should_return_50_25(self):
		self.assertEqual([0.5, 0.25],change(0.75))

	def test_when_amount_is_80_should_return_50_25_5(self):
		self.assertEqual([0.5, 0.25, 0.05],change(0.80))

	def test_when_amount_is_90_should_return_50_25_1_5(self):
		self.assertEqual([0.5, 0.25, 0.1, 0.05],change(0.90))

	def test_when_amount_is_85_should_return_50_25_1(self):
		self.assertEqual([0.5, 0.25, 0.1],change(0.85))

	def test_when_amount_is_10_should_return_10(self):
		self.assertEqual([0.1],change(0.1))
	
	def test_when_amount_is_125_should_return_1_and_25(self):
		self.assertEqual([1.00, 0.25],change(1.25))

	def test_when_amount_is_11_should_return_10_and_1(self):
		self.assertEqual([0.10, 0.01], change(0.11))

	

if __name__ =='__main__':
	unittest.main()
