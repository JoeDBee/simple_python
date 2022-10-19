fib_nums = [0, 1]


def fibonacci(n):
    # Check is n is less
    # than 0
    if n <= 0:
        print("Incorrect input")

    # Check is n is less
    # than len(FibArray)
    elif n <= len(fib_nums):
        return fib_nums[n - 1]
    else:
        temp_fib = fibonacci(n - 1) + fibonacci(n - 2)
        fib_nums.append(temp_fib)
        return temp_fib


def fib(n):
    if n <= 1:
        return n
    return fib(n-1) + fib(n-2)


if __name__ == '__main__':
    # Driver Program
    print(fibonacci(7))
    print(fib(6))
