import sys

filepath = sys.argv[1]
delim = '\t'
if len(sys.argv) > 2:
    delim = sys.argv[2]

outdegrees = {}
for line in open(filepath):
    entry = line.rstrip().split(delim)
    src = entry[0]
    dst = entry[1]
    tag = entry[2]
    if not src in outdegrees: outdegrees[src] = 0
    outdegrees[src] += 1

distribution = {}
for nid in outdegrees:
    d = outdegrees[nid]
    if not d in distribution: distribution[d] = 0
    distribution[d] += 1

for d, count in sorted(distribution.items()):
    print d,count
