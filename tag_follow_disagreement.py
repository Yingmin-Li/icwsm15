import sys

tagging_filepath = sys.argv[1]
following_filepath = sys.argv[2]

delim = '\t'
if len(sys.argv) > 3:
    delim = sys.argv[3]

graph = {}
for line in open(tagging_filepath):
    entry = line.rstrip().split('\t')
    src = entry[0]
    dst = entry[1]
    if not src in graph: graph[src] = {}
    graph[src][dst] = 0

for line in open(following_filepath):
    entry = line.rstrip().split('\t')
    src = entry[0]
    dst = entry[1]
    if src in graph and dst in graph[src]:
        graph[src][dst] += 1
    if dst in graph and src in graph[dst]:
        graph[dst][src] += 2

w_dir = 0
wo_dir = 0
count = 0.0
for src in graph:
    for dst in graph[src]:
        val = graph[src][dst]
        count += 1
        if val in [1,3]:
            w_dir += 1
        if val in [1,2,3]:
            wo_dir += 1

print "%s\t%s" % (w_dir/count, wo_dir/count)
