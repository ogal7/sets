##Olivia Gallager
##Softdev homework 


#Consider in python using lists to represent sets, as they are defined in math. If you do so, you can perform basic set operations using 
#list comprehensions. 

#Your mission, create list comprehension-based functions that perform the following set operations on python lists:

	

def union(L1,L2):
	h =  [a for a in L1]
	print h
	addOn = [a for a in L2 if a not in h]
	print addOn
	h.extend(addOn)
	return h

def upsideDownU(L1,L2):
	return [a for a in L1 if a in L2]

#Set difference of U and A, denoted U \ A, is the set of all members of U that are not members of A. 
#The set difference {1, 2, 3} \ {2, 3, 4} is {1}, while, conversely, the set difference {2, 3, 4} \ {1, 2, 3} is {4} . 
#When A is a subset of U, the set difference U \ A is also called the complementof A in U. In this case, if the choice 
#of U is clear from the context, the notation Ac is sometimes used instead of U \ A, particularly if U is a universal 
#set as in the study of Venn diagrams.

def setDiff(L1,L2):
	return [a for a in L1 if a not in L2]


def symDiff(L1,L2):
	u = union(L1,L2)
	print u
	intersect = upsideDownU(L1,L2)
	if len(intersect) != 0:
		return [a for a in u if a not in intersect]


def cartesianProd(L1,L2):
	setS = [(L1[i],L2[i]) for i in range(len(L1))]
	setS += [(L1[i], L2[i]) for i in range(len(L2))]
	return setS

print union([1,2,3],[3,4,5])
print "\n"

print upsideDownU([1,2,3],[3,4,5])
print "\n"

print setDiff([1,2,3],[2,3,4])
print "shud be 1\n"

print setDiff([2,3,4],[1,2,3])
print "shud be 4\n"


print symDiff([2,3,4],[1,2,3])
print "shud be 1,4\n"

print cartesianProd([1,2],[3,4])




