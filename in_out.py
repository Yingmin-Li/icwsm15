import sys

filepath = sys.argv[1]
delim = '\t'
if len(sys.argv) > 2:
    delim = sys.argv[2]

indegrees = {}
outdegrees = {}
for line in open(filepath):
    entry = line.rstrip().split(delim)
    src = entry[0]
    dst = entry[1]
    tag = entry[2]
    if not src in outdegrees: outdegrees[src] = 0
    if not src in indegrees: indegrees[src] = 0
    outdegrees[src] += 1
    if not dst in outdegrees: outdegrees[dst] = 0
    if not dst in indegrees: indegrees[dst] = 0
    indegrees[dst] += 1

for uid in indegrees:
    ind = indegrees[uid]
    outd = outdegrees[uid]
    print "%s\t%s" % (ind,outd)
