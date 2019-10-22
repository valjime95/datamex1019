# Robin Hood
import os
os.chdir("/Users/valeriajimeno/Desktop")
print(os.getcwd())
points = [(4, 5), (-0, 2), (4, 7), (1, -3), (3, -2), (4, 5),(3, 2), (5, 7), (-5, 7), (2, 2), (-4, 5), (0, -2),(-4, 7), (-1, 3), (-3, 2), (-4, -5), (-3, 2),(5, 7), (5, 7), (2, 2), (9, 9), (-8, -9)]
# 1. Robin Hood is famous for hitting an arrow with another arrow. Did you get it?
'''
from collections import Counter
c = Counter()
for i in points:
    c[i] += 1
c
'''
def rh(lis):
    from collections import Counter
    cont = Counter(lis)
    for i in lis:
        if cont[i]>1:
            return True
rh(points)
# 2. Calculate how many arrows have fallen in each quadrant.
I,II,III,IV = [],[],[],[]
for i in range(len(points)):
	if points[i][0] > 0 and points[i][1] > 0:
		I.append(points[i])
	elif points[i][0] < 0 and points[i][1] > 0:
		II.append(points[i])
	elif points[i][0] < 0 and points[i][1] < 0:
		III.append(points[i])
	elif points[i][0] > 0 and points[i][1] < 0:
		IV.append(points[i])
s = (len(I),len(II),len(III),len(IV))
