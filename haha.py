##Olivia Gallager
##Softdev homework 


#Consider in python using lists to represent sets, as they are defined in math. If you do so, you can perform basic set operations using 
#list comprehensions. 

#Your mission, create list comprehension-based functions that perform the following set operations on python lists:

	

def union(L1,L2):
	h =  [a for a in L1]
	addOn = [a for a in L2 if a not in h]
	return h.append(addOn)

def upsideDownU(L1,L2):
	return [a for a in L1 if a not in L2]



#def setDiff(L1,L2):


#def symDiff(L1,L2):



#def cartesianProd(L1,L2):


print union([1,2,3],[3,4,5])
print upsideDownU([1,2,3],[3,4,5])