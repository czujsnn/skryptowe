import sys
print(map(lambda x: int(x), list(filter(lambda x: x.isdigit(), list(sys.stdin.read().strip() )))))