import sys
from functools import reduce

# print(          reduce(
#                     lambda x, y: x + y, list(
#                         open(file, 'r').read().replace('\n', ' ').split() for file in sys.argv[1:]
#                     )
#                 )
# )

a = ['44', '6', '7', '89', '7']
b = ['123', '45', '102', '763', '9']
z = lambda x,y: x+y,list(a+b)
print(reduce(lambda x,y:x+y,[['44', '6', '7', '89', '7'], ['123', '45', '102', '763', '9']]))
print(a+b)
print([1] + [2])