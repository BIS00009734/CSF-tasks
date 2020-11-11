myMarks = {'CSF': 75, 'FunPro': 80, 'WT': 85}

totalMark=0

for i in myMarks.values():
	totalMark += i

print(totalMark/len(myMarks))