import sys

filepath = sys.argv[1]
delim = '\t'
if len(sys.argv) > 2:
    delim = sys.argv[2]

graph = {}
for line in open(filepath):
    entry = line.rstrip().split(delim)
    src = entry[0]
    dst = entry[1]
    tag = entry[2]
    if not src in graph: graph[src] = {}
    if not dst in graph[src]: graph[src][dst] = 0
    graph[src][dst] += 1

multiplicities = {}
for src in graph:
    for dst in graph[src]:
        m = graph[src][dst]
        if not m in multiplicities: multiplicities[m] = 0
        multiplicities[m] += 1

for m,count in sorted(multiplicities.items()):
    print m,count
