import sys
from itertools import groupby

print([list(group) for key,group in groupby(
    list(map(lambda x: int(x), list(filter(lambda x: x.isdigit(), list(sys.stdin.read().strip() ))))))])

#we make list from read input, then strip it, then check if x is digit, then filtering it, because isdigit returns bool, then we make list again,
#we use map to convert all items to int.
#then we use groupby to group: it takes data to group, and then func to group with:
#eg: [list(group) for key, group in groupby('AAAABBBCCD')] --> AAAA BBB CC D