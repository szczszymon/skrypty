import sys; from collections import Counter; print(dict(Counter(map(len, sys.stdin.read().split()))))
