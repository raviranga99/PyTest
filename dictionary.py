d={"1":"4","f":7,"r":"r"}
print d
print d["1"]
d["r"]="ravi"# update existing entry
d["s"]="ranga"# Add new entry
print d
del d['f']; # remove entry with key 'Name'
print d
d.clear(); # remove all entries in dict
print d
del d ; # delete entire dictionary
#print d
"""(a) More than one entry per key not allowed. Which means no duplicate key is
allowed. When duplicate keys encountered during assignment, the last assignment
wins."""
d1={"a":"a","b":"b","a":2}
print d1
"""----------------method---------------"""
d3=d1.copy()
print d3
"""
1   dict.fromkeys(seq[, value]))
2   dict.get(key, default=None)
3   dict.has_key(key)
4   dict.items()
5   dict.keys()
6   dict.setdefault(key, default=None)
7   dict.update(dict2)
8   dict.values()
"""