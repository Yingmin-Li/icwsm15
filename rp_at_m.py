import sys

filepath = sys.argv[1]
delim = '\t'
if len(sys.argv) > 2:
    delim = sys.argv[2]

graph = {}
for line in open(filepath):
    entry = line.rstrip().split('\t')
    src = entry[0]
    dst = entry[1]
    tag = entry[2].lower()
    if not src in graph: graph[src] = {}
    if not dst in graph[src]: graph[src][dst] = set()
    graph[src][dst].add(tag)

reciprocal = {}
edges = {}
for src in graph:
    for dst in graph[src]:
        if src == dst: continue
        m = len(graph[src][dst])
        if not m in edges: edges[m] = 0
        if not m in reciprocal: reciprocal[m] = 0
        edges[m] += 1
        if dst in graph and src in graph[dst]:
            reciprocal[m] += 1

for m in sorted(reciprocal):
    print "%s\t%s\t%s\t%s" % (m,edges[m],reciprocal[m],float(reciprocal[m])/edges[m])
