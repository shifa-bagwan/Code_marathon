nums = [1, 2, 4, 6]

output = []

for i in range(len(nums)):
    product = 1

    for j in range(len(nums)):
        if i != j:
            product = product * nums[j]

    output.append(product)

print(output)