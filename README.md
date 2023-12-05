Progress
00: 14/14 done
01: 10/10 done
02: 12/12 done
03: 7/7   done
04: 12/12 done
05: 0/9
06: 4/10
07: 10/10 done
08: 2/9
09: 7/12
10: 5/5   done
11: 8/8   done
12: 3/12
13: 3/8
14: 3/10
15: 8/8   done
16: 4/9
17: 4/8
18: 7/7   done
19: 6/7

import sys

lines = list()
for line in sys.stdin:
    lines.append(line.strip("\n").split("o"))

lines_filtered = list()

for i in range(len(lines)):
    lines[i].remove(lines[i][-1])
for line in lines:
    lines_filtered.append(filter(lambda n: len(str(n)) % 2 != 0, line))

lines.clear()
for i in lines_filtered:
    lines.append(*i)

print(lines)

 
