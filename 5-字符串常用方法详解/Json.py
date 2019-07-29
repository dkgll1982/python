#!/usr/bin/python
import json

data = [ { 'a' : 1, 'b' : 2, 'c' : 3, 'd' : 4, 'e' : 5 } ]

json2 = json.dumps(data)
print(json.dumps({'av': 'Runoob', 'ab': 7}, sort_keys=True, indent=4, separators=(',', ': ')))