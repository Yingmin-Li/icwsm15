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
nlists = {}
for src in graph:
    for dst in graph[src]:
        for tag in graph[src][dst]:
            if not tag in nlists: nlists[tag] = set()
            nlists[tag].add(src)
            if not tag in edges: edges[tag] = 0
            if not tag in reciprocal: reciprocal[tag] = 0
            edges[tag] += 1
            if dst in graph and src in graph[dst]:
                reciprocal[tag] += 1

for tag,n in sorted(nlists.items(), key=lambda x:len(x[1]), reverse=True):
    nedges = edges[tag]
    nreciprocal = reciprocal[tag]
    print "%s\t%s\t%s\t%s\t%s\t%s" % (tag,len(n),float(nreciprocal)/nedges,(float(nreciprocal)/nedges)/0.0455887970965)
