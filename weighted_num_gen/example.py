from .RandomGen import RandomGen


def main():
	nums = [-1, 0, 1, 2, 3]
	weights = [0.01, 0.3, 0.58, 0.1, 0.01]
	thing = RandomGen(nums, weights)

	results = [0] * len(nums)
	runs = 100000

	for run in range(runs):
		random_num = thing.next_num()
		for index, num in enumerate(nums):
			if random_num == num:
				results[index] = results[index]+1

	results = [result/runs for result in results]
	print('weights: ', weights)
	print('results: ', results)


if __name__ == "__main__":
	main()
