import glob

l1 = [x for x in glob.glob(r"2-练习例子\*\*.py")]
l2 = [x for x in glob.glob(r"2-练习例子\*.py")]

l1.extend(l2) 
for l in l1:
    print(l)