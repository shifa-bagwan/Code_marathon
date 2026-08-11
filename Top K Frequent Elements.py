from collections import Counter

nums = [1, 2, 2, 3, 3, 3]
k = 2

count = Counter(nums)

answer = [num for num, freq in count.most_common(k)]

print(answer)