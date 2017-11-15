
import random
import os
import platform

if "armv" in platform.machine() :
    # import GPIO if running on RPI
    import RPi.GPIO as GPIO
else :
    # import gpio_mock if not running on RPI
    from lib import gpio_mock as GPIO


A=16
B=18
C=22
D=32
E=36
F=38
G=40

def setup():
    """ Function to setup raspberry pi GPIO mode and warnings. PIN 7 OUT and PIN 15 IN """

    # Setup GPIO on raspberry pi
    GPIO.setmode(GPIO.BOARD)
    GPIO.setwarnings(False)
    GPIO.setup(7, GPIO.OUT, initial=GPIO.LOW) # Tell the program you want to use pin number 7 as output. Relay is ACTIVE LOW, so OFF is HIGH
    GPIO.setup(15, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)  # Set GPIO 15 as a PULL DOWN switch
    GPIO.add_event_detect(15, GPIO.RISING, activate_goal_light, 5000)
    GPIO.setup(A, GPIO.OUT, initial=GPIO.HIGH)
    GPIO.setup(B, GPIO.OUT, initial=GPIO.HIGH)
    GPIO.setup(C, GPIO.OUT, initial=GPIO.HIGH)
    GPIO.setup(D, GPIO.OUT, initial=GPIO.HIGH)
    GPIO.setup(E, GPIO.OUT, initial=GPIO.HIGH)
    GPIO.setup(F, GPIO.OUT, initial=GPIO.HIGH)
    GPIO.setup(G, GPIO.OUT, initial=GPIO.LOW)


def writeScore(score):
	if score == 0:
		write0()
	if score == 1:
		write1()
	if score == 2:
		write2()
	if score == 3:
		write3()
	if score == 4:
		write4()
	if score == 5:
		write5()
	if score == 6:
		write6()
	if score == 7:
		write7()
	if score == 8:
		write8()
	if score == 9:
		write9()


def write0():
	GPIO.output(A, GPIO.HIGH)
	GPIO.output(B, GPIO.HIGH)
	GPIO.output(C, GPIO.HIGH)
	GPIO.output(D, GPIO.HIGH)
	GPIO.output(E, GPIO.HIGH)
	GPIO.output(F, GPIO.HIGH)
	GPIO.output(G, GPIO.LOW)


def write1():
	GPIO.output(A, GPIO.LOW)
	GPIO.output(B, GPIO.HIGH)
	GPIO.output(C, GPIO.HIGH)
	GPIO.output(D, GPIO.LOW)
	GPIO.output(E, GPIO.LOW)
	GPIO.output(F, GPIO.LOW)
	GPIO.output(G, GPIO.LOW)


def write2():
	GPIO.output(A, GPIO.HIGH)
	GPIO.output(B, GPIO.HIGH)
	GPIO.output(C, GPIO.LOW)
	GPIO.output(D, GPIO.HIGH)
	GPIO.output(E, GPIO.HIGH)
	GPIO.output(F, GPIO.LOW)
	GPIO.output(G, GPIO.HIGH)


def write3():
	GPIO.output(A, GPIO.HIGH)
	GPIO.output(B, GPIO.HIGH)
	GPIO.output(C, GPIO.HIGH)
	GPIO.output(D, GPIO.HIGH)
	GPIO.output(E, GPIO.LOW)
	GPIO.output(F, GPIO.LOW)
	GPIO.output(G, GPIO.HIGH)


def write4():
	GPIO.output(A, GPIO.LOW)
	GPIO.output(B, GPIO.HIGH)
	GPIO.output(C, GPIO.HIGH)
	GPIO.output(D, GPIO.LOW)
	GPIO.output(E, GPIO.LOW)
	GPIO.output(F, GPIO.HIGH)
	GPIO.output(G, GPIO.HIGH)


def write5():
	GPIO.output(A, GPIO.HIGH)
	GPIO.output(B, GPIO.LOW)
	GPIO.output(C, GPIO.HIGH)
	GPIO.output(D, GPIO.HIGH)
	GPIO.output(E, GPIO.LOW)
	GPIO.output(F, GPIO.HIGH)
	GPIO.output(G, GPIO.HIGH)


def write6():
	GPIO.output(A, GPIO.HIGH)
	GPIO.output(B, GPIO.LOW)
	GPIO.output(C, GPIO.HIGH)
	GPIO.output(D, GPIO.HIGH)
	GPIO.output(E, GPIO.HIGH)
	GPIO.output(F, GPIO.HIGH)
	GPIO.output(G, GPIO.HIGH)


def write7():
	GPIO.output(A, GPIO.HIGH)
	GPIO.output(B, GPIO.HIGH)
	GPIO.output(C, GPIO.HIGH)
	GPIO.output(D, GPIO.LOW)
	GPIO.output(E, GPIO.LOW)
	GPIO.output(F, GPIO.LOW)
	GPIO.output(G, GPIO.LOW)


def write8():
	GPIO.output(A, GPIO.HIGH)
	GPIO.output(B, GPIO.HIGH)
	GPIO.output(C, GPIO.HIGH)
	GPIO.output(D, GPIO.HIGH)
	GPIO.output(E, GPIO.HIGH)
	GPIO.output(F, GPIO.HIGH)
	GPIO.output(G, GPIO.HIGH)


def write9():
	GPIO.output(A, GPIO.HIGH)
	GPIO.output(B, GPIO.HIGH)
	GPIO.output(C, GPIO.HIGH)
	GPIO.output(D, GPIO.LOW)
	GPIO.output(E, GPIO.LOW)
	GPIO.output(F, GPIO.HIGH)
	GPIO.output(G, GPIO.HIGH)


def activate_goal_light(main_dir, gpio_event_var=0):
    """ Function to activate GPIO for goal light and plar random audio clip. """

    songrandom = random.randint(1, 3) #Set random numbers depending on number of audio clips available
    GPIO.output(7, GPIO.HIGH) #Turn on light, active low relay, so on is low
    # Prepare commande to play sound (change file name if needed)
    command_play_song = 'sudo mpg123 -q {directory}/audio/goal_horn_{SongId}.mp3'.format(directory=main_dir,SongId=str(songrandom))
    os.system(command_play_song) # Play sound
    GPIO.output(7, GPIO.LOW) #Turn off light


def cleanup():
    """ Function to cleanup raspberry pi GPIO at end of code """

    # Restore GPIO to default state
    GPIO.remove_event_detect(15) #Add to end of function
    GPIO.cleanup()
    print("GPIO cleaned!")
