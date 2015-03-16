import sys

filepath = sys.argv[1]
delim = '\t'
if len(sys.argv) > 2:
    delim = sys.argv[2]

indegrees = {}
for line in open(filepath):
    entry = line.rstrip().split(delim)
    src = entry[0]
    dst = entry[1]
    tag = entry[2]
    if not dst in indegrees: indegrees[dst] = 0
    indegrees[dst] += 1

distribution = {}
for nid in indegrees:
    d = indegrees[nid]
    if not d in distribution: distribution[d] = 0
    distribution[d] += 1

for d, count in sorted(distribution.items()):
    print d,count
