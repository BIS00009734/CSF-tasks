csf = {
	'cw1-w': 0.4;
	'cw1-mark': 79,
	'exam-w': 0.6,
	'exam-mark': 65
}

totalMark = 0

totalMark+=csf.get('cw1-w')*csf.get('cw1-mark')
totalMark+=csf.get('exam-w')*csf.get('exam-mark')

print(totalMark)