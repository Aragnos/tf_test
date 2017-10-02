""" Test file"""


file_name = 'Test.txt'
opened_file = open(file_name, 'r')

lines = sum(1 for line in opened_file)
print(lines)
opened_file.close()

values = []
values.append('Horseshit\t200000')
values.append('Some more')

for v in values:
	splitted = v.split('\t')
	for s in splitted:
		print s
	print(v)
values = []
if values:
	print('Joah')
"""
def x():
	print(5)


def ambi():
	print("ambi")


c = {}
c2 = {"func": x}
c.update(c2)
print(c)
c.update({"al": ambi})
print(c)
c["al"]()
"""
