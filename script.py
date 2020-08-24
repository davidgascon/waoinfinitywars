#imports
import pyautogui
import time
import random
import keyboard



#functions
def boxpress(left, top, right, bottom):
	''' Input: Left, to    p, right, bottom boundaries. This function will randomly press within the 4 boundaries of the cordinates input'''
	randomX = random.randrange(left, right, 1)
	randomY = random.randrange(top, bottom, 1)
	pyautogui.click(randomX, randomY)
def clickpause():
	'''clicks pause/play'''
	boxpress(1185, 206, 1216, 235)


def runpause(runtime=1, pausetime=1, elapsedtime=0, totalruntime=0):
	'''make sure game is paused, will end paused'''
	start = time.time()
	clickpause()

	if runtime > 5: #this will allow for the user to exit by pressing q. Without this, it will not stop until the time has lapsed
		runtimecounter = 0
		while runtimecounter < runtime:
			counterstart = time.time()
			time.sleep(1)
			counterend = time.time()
			runtimecounter += counterend - counterstart
			print(f"runtimecounter = {runtimecounter}")
			if keyboard.is_pressed("q"):
				clickpause()
				return runtimecounter
	else:
		time.sleep(runtime)

	end = time.time()
	cycleruntime = end - start

	pausestart = time.time()
	clickpause()
	time.sleep(pausetime)
	pauseend = time.time()
	cyclepausetime = pauseend - pausestart

	totalruntime = totalruntime + cycleruntime
	elapsedtime = elapsedtime + cycleruntime + cyclepausetime
	print(f"Your cycle runtime is {cycleruntime}")
	print(f"Your cycle pause time is {cyclepausetime}")
	print(f"Your total runtime is {totalruntime}")
	print(f"Your elapsed total is {elapsedtime}\n")



	return elapsedtime, totalruntime



def welcome(): #Couldve been named something like 'variables' but oh well.
	runtime = float(input("What is your runtime wait?"))
	if runtime < 0:
		runtime = 1
	pausetime = float(input("What is your pausetime wait?"))
	if pausetime < 0:
		pausetime = 1

	return runtime, pausetime



#script

print("Welcome.")
elapsedtime = 0
totalruntime = 0
runtime, pausetime = welcome()


while True: #Loop
	if keyboard.is_pressed(" "):
		elapsedtime, totalruntime = runpause(runtime, pausetime, elapsedtime, totalruntime)

	if keyboard.is_pressed("r"):
		while True:
			if keyboard.is_pressed("q"):
				print("Break\n")
				break
			else:
				elapsedtime, totalruntime = runpause(runtime, pausetime, elapsedtime, totalruntime)


	elif keyboard.is_pressed("c"):
		runtime, pausetime = welcome()
		print("Press and hold the spacebar to run.")

	elif keyboard.is_pressed("t"):
		elapsedtime = 0
		print("Reset time.")
		time.sleep(.25) #without this 

	elif keyboard.is_pressed("b"):
		exit()




exit()
