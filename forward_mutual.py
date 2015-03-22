import sys

tagging_filepath = sys.argv[1]
following_filepath = sys.argv[2]

delim = '\t'
if len(sys.argv) > 3:
    delim = sys.argv[3]

graph = {}
flags = {}
for line in open(tagging_filepath):
    entry = line.rstrip().split('\t')
    src = entry[0]
    dst = entry[1]
    tag = entry[2].lower()
    if not src in graph: graph[src] = {}
    if not dst in graph[src]: graph[src][dst] = set()
    graph[src][dst].add(tag)
    if not src in flags: flags[src] = {}
    flags[src][dst] = 0

for line in open(following_filepath):
    entry = line.rstrip().split('\t')
    src = entry[0]
    dst = entry[1]
    if src in flags and dst in flags[src]:
        flags[src][dst] += 1
    if dst in flags and src in flags[dst]:
        flags[dst][src] += 2

forward = {}
mutual = {}
count = {}
nlists = {}
for src in flags:
    for dst in flags[src]:
        val = flags[src][dst]
        for tag in graph[src][dst]:
            if not tag in count: count[tag] = 0.0
            if not tag in forward: forward[tag] = 0
            if not tag in mutual: mutual[tag] = 0
            count[tag] += 1
            if not tag in nlists: nlists[tag] = set()
            nlists[tag].add(src)
        if val == 1:
            for tag in graph[src][dst]:
                forward[tag] += 1
        if val == 3:
            for tag in graph[src][dst]:
                mutual[tag] += 1

for tag,n in sorted(nlists.items(), key=lambda x:len(x[1]), reverse=True):
    print "%s\t%s\t%s\t%s\t%s\t%s" % (tag, count[tag], forward[tag], forward[tag]/count[tag], mutual[tag], mutual[tag]/count[tag])
