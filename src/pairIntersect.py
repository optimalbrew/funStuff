"""
Given a table with two columns: names, company create lists of pairs of names with overlapping set of companies
Name Company
A   C1
A   C2
A   C3
B   C2
B   C3
B   C4
C   C1
C   C5

output:
(A,B) : (C2,C3)
(A,C) : (C1)
(B,C) : ()
"""

# one way to store the input is a list where each element is a list [name, company]
input = [['A','C1'], ['A','C2'], ['A','C3'], ['B','C2'], ['B','C3'], ['B','C4'], ['C','C1'],['C','C5']]

#Create a dict where a key is a unique name and value is all associated companies
combo = dict()

for data in input:
    if data[0] not in combo.keys(): #if name is not in dict
        combo[data[0]] = {data[1]}
    else:       #if name already in dict, add company to set of values
        combo[data[0]].add(data[1])

#combo

#Then pairwise intersections and make a list out of that
from itertools import combinations

output = []

for i,j in combinations(combo.keys(),2):
    inter = combo[i].intersection(combo[j])
    if len(inter) > 0:
        print(i,' and ', j,' have ', inter, 'in common')
        output.append([[i,j],inter])
    else:
        print(i,' and ',j,' have nothing in common')
        output.append([[i,j],None])

print(output)