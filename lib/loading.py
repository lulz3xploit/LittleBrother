import sys, random, time, importlib
import threading, settings

def loadingHack(importlib):
	chaine = "[*]"+' Start LittleBrother...'
	charspec = "$*.X^%_/\\#~!?;"

	while importlib.is_alive():
		chainehack = ""
		for c in chaine:
			chainehack += c
			r = random.choice(charspec)+random.choice(charspec)+random.choice(charspec)
			if len(chainehack+r) <= len(chaine):
				pass
			else:
				r = ""
			sys.stdout.write('\r'+chainehack+r)
			time.sleep(0.06)

def loadingUpper(importlib):
	string = "Start littlebrother"
	string = list(string)
	nb = len(string)

	while importlib.is_alive():
		x = 0
		while x < nb:
			c = string[x]
			c = c.upper()
			string[x] = c
			sys.stdout.write("\r[*] "+''.join(string) +'...')
			time.sleep(0.1)
			c = string[x]
			c = c.lower()
			string[x] = c
			x += 1

def loadingTextPrint(importlib):
	string = "Start littlebrother"

	while importlib.is_alive():
		space = " " * 100
		sys.stdout.write("\r"+space)

		x = 1

		while x <= len(string):
			times = "0."
			times += str(random.choice(range(1, 3)))
			sys.stdout.write("\rroot@littlebrother:~$ "+string[:x]+"|")
			time.sleep(float(times))
			x += 1

def thread_loading():
	num = random.choice([1, 2, 3])

	importlib = threading.Thread(target=settings.init)
	importlib.start()

	if num == 1:
		load = threading.Thread(target=loadingHack(importlib))
	elif num == 2:
		load = threading.Thread(target=loadingUpper(importlib))
	elif num == 3:
		load = threading.Thread(target=loadingTextPrint(importlib))

	load.start()
	importlib.join()
	load.join()
