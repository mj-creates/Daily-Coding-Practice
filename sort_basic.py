a = list(map(int, input().split()))
print(a)
a.sort()
print(a)

# the sort() function just modifies the given list

b = sorted(a)
print(b)

# the sorted() function returns a different sorted list
# the sorted() function is not only for lists but also for tuples string

#sorting a tuple
a = (21, 1, 43, 12, 54)
b = sorted(a)
print(b) # returns list

#sorting a set
a = {'abc', 'man', 'opq', 'bed'}
b = sorted(a)
print(b) # returns list


#sorting a dictionary
s = {100 : 'man', 21 : 'abc', 12 : 'pqr', 5 : 'mao'}
b = sorted(s)
print(s) #sorts by key values

#sorting a list of tuples
l = [(23, 45), (12, 21), (34, 43)]
b = sorted(l)
print(b) #sorts by first element of tuple

