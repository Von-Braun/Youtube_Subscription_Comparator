import sys 
xml_fnameA=open(sys.argv[1],'r').read().split('outline text') #old

xml_fnameB=open(sys.argv[2],'r').read().split('outline text') #new

#find things in old not in new
print '\nGONE\n===='
for i in range(0,len(xml_fnameA)):
	A_old = xml_fnameA[i]
	if A_old not in xml_fnameB:
		print  A_old.split('\"')[1].split('\"')[0]

#find things in new not in old
print '\nNEW\n==='
for i in range(0,len(xml_fnameB)):
	B_new = xml_fnameB[i]
	if B_new not in xml_fnameA:
		print B_new.split('\"')[1].split('\"')[0]