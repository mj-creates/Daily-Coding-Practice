# we define lambda function to define custom sorting logic
a = [(1, 'one'), (3, 'three'), (2, 'two')]

#sorted by the second element of each tuple
sa = sorted(a, key=lambda x: x[1])
print("Sorted by second element:", sa)
