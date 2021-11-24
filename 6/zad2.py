import sys
from collections import Counter

print(
    dict(
        sorted(Counter(
            [len(x) for x in sys.stdin.read().split()]).items()
        )
    )
)