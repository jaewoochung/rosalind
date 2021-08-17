# Intake DNA string
dna = input("Enter the DNA string\n")

hm = {}

for str in dna:
	if str in hm:
		hm[str] += 1
	else:
		hm[str] = 1
"""
for nuc in hm:
	print(nuc + " " + str(hm[nuc]))
"""

print(hm["A"], hm["C"], hm["G"], hm["T"])
