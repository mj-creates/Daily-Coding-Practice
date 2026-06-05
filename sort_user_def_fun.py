# sorted using x values and using a user defined function
class Def_init:
    def __init__(self, x, y):
        self.x = x #giving the 1st val to x
        self.y = y #giving the 2nd val to y
def sort_by_x(p):
    return p.x #returning the x value to sort by it
l = [Def_init(1, 100), Def_init(23, 12), Def_init(7, 1000)]
l.sort(key = sort_by_x) #the sorting is done through sort function

for i in l:
    print(i.x, i.y) #the final output printed