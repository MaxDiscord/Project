unCorrect = "test"
pwCorrect = "Orchid5"
correct = False
unc = False
pnc = False
while not correct:
	un = input ("UN: ")
	if un == unCorrect:
		unc = True
	pw = input ("PW: ")
	if pw == pwCorrect:
		pnc = True

	if pnc == True and unc == True:
		correct = True
	

while Correct:
	