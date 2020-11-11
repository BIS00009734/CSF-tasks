myMarks = {'CSF': 75, 'FunPro': 80, 'WT': 85}

def averageMark(marks):

	totalMark=0

	for i in myMarks.values():
		totalMark += i

	return totalMark

print(averageMark(myMarks))