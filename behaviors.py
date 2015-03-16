import sys

filepath = sys.argv[1]
delim = '\t'
if len(sys.argv) > 2:
    delim = sys.argv[2]

behaviors = {}
for line in open(filepath):
    entry = line.rstrip().split(delim)
    src = entry[0]
    dst = entry[1]
    tag = entry[2]
    if not src in behaviors:
        behaviors[src] = {'T':set(), 'R':set(), 'd':set()}
    behaviors[src]['T'].add(tag)
    behaviors[src]['R'].add(dst)
    behaviors[src]['d'].add((tag,dst))

for nid in behaviors:
    Tu = len(behaviors[nid]['T'])
    Ru = len(behaviors[nid]['R'])
    du = len(behaviors[nid]['d'])
    print "%s\t%s\t%s" % (Tu,Ru,du)
