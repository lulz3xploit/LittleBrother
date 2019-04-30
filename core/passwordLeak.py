from core.leaked import leaked

def passwordLeak(passw):
	l = leaked()
	emails = l.password(passw)

	print(emails)