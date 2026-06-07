#sorting the numbers based on their absolute values while preserving the orginal signs

a = [1, -5, 10, 6, 3, -4, -9]

#sorting by absolute values in descending order
sa = sorted(a, key=abs, reverse=True)
print("Sorted by absolute values: ", sa)