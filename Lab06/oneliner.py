import sys; from collections import Counter as Ctr; print(dict(Ctr(map(lambda x: len(x), sys.stdin.read().split()))))
