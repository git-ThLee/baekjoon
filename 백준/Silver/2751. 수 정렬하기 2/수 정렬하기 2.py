import sys
case = int(sys.stdin.readline())
s = list()
for _ in range(case):
  a = int(sys.stdin.readline())
  s.append(a)
for i in sorted(s):
  print(i)