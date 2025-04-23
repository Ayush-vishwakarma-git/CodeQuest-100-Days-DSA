# Take space-separated integers as input and convert them into a list
lst = list(map(int, input("Enter numbers: ").split()))

# Initialize sum to 0
sum = 0


for i in range(1, len(lst), 2):
    sum += lst[i]  # Add the element at even index to the sum

# Print the hidden key (sum of even-indexed elements)
print("Hidden Key :", sum)
