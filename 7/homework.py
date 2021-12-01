import sys
from itertools import groupby

print([list(group) for key,group in groupby(
    list(map(lambda x: int(x), list(filter(lambda x: x.isdigit(), list(sys.stdin.read().strip() ))))))])

