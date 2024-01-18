import sys

print(not all(all(int(num) for num in nums) for nums in [line.split() for line in list(sys.stdin)]))