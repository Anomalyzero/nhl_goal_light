
import random
import os
import platform

if "armv" in platform.machine() :
    # import GPIO if running on RPI
    import RPi.GPIO as GPIO
else :
    # import gpio_mock if not running on RPI
    from lib import gpio_mock as GPIO


HAWKS_A=16
HAWKS_B=18
HAWKS_C=22
HAWKS_D=32
HAWKS_E=36
HAWKS_F=38
HAWKS_G=40
OPPOSITION_A=13
OPPOSITION_B=15
OPPOSITION_C=29
OPPOSITION_D=31
OPPOSITION_E=33
OPPOSITION_F=35
OPPOSITION_G=37

def setup():
    """ Function to setup raspberry pi GPIO mode and warnings. PIN 7 OUT and PIN 15 IN """

    # Setup GPIO on raspberry pi
    GPIO.setmode(GPIO.BOARD)
    GPIO.setwarnings(False)
    GPIO.setup(7, GPIO.OUT, initial=GPIO.LOW) # Tell the program you want to use pin number 7 as output. Relay is ACTIVE LOW, so OFF is HIGH
    #GPIO.setup(15, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)  # Set GPIO 15 as a PULL DOWN switch
    GPIO.add_event_detect(15, GPIO.RISING, activate_goal_light, 5000)
    GPIO.setup(HAWKS_A, GPIO.OUT, initial=GPIO.HIGH)
    GPIO.setup(HAWKS_B, GPIO.OUT, initial=GPIO.HIGH)
    GPIO.setup(HAWKS_C, GPIO.OUT, initial=GPIO.HIGH)
    GPIO.setup(HAWKS_D, GPIO.OUT, initial=GPIO.HIGH)
    GPIO.setup(HAWKS_E, GPIO.OUT, initial=GPIO.HIGH)
    GPIO.setup(HAWKS_F, GPIO.OUT, initial=GPIO.HIGH)
    GPIO.setup(HAWKS_G, GPIO.OUT, initial=GPIO.LOW)
    GPIO.setup(OPPOSITION_A, GPIO.OUT, initial=GPIO.HIGH)
    GPIO.setup(OPPOSITION_B, GPIO.OUT, initial=GPIO.HIGH)
    GPIO.setup(OPPOSITION_C, GPIO.OUT, initial=GPIO.HIGH)
    GPIO.setup(OPPOSITION_D, GPIO.OUT, initial=GPIO.HIGH)
    GPIO.setup(OPPOSITION_E, GPIO.OUT, initial=GPIO.HIGH)
    GPIO.setup(OPPOSITION_F, GPIO.OUT, initial=GPIO.HIGH)
    GPIO.setup(OPPOSITION_G, GPIO.OUT, initial=GPIO.LOW)


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


def writeOppositionScore(score):
	if score == 0:
		write0_OPP()
	if score == 1:
		write1_OPP()
	if score == 2:
		write2_OPP()
	if score == 3:
		write3_OPP()
	if score == 4:
		write4_OPP()
	if score == 5:
		write5_OPP()
	if score == 6:
		write6_OPP()
	if score == 7:
		write7_OPP()
	if score == 8:
		write8_OPP()
	if score == 9:
		write9_OPP()


def write0():
	GPIO.output(HAWKS_A, GPIO.HIGH)
	GPIO.output(HAWKS_B, GPIO.HIGH)
	GPIO.output(HAWKS_C, GPIO.HIGH)
	GPIO.output(HAWKS_D, GPIO.HIGH)
	GPIO.output(HAWKS_E, GPIO.HIGH)
	GPIO.output(HAWKS_F, GPIO.HIGH)
	GPIO.output(HAWKS_G, GPIO.LOW)


def write1():
	GPIO.output(HAWKS_A, GPIO.LOW)
	GPIO.output(HAWKS_B, GPIO.HIGH)
	GPIO.output(HAWKS_C, GPIO.HIGH)
	GPIO.output(HAWKS_D, GPIO.LOW)
	GPIO.output(HAWKS_E, GPIO.LOW)
	GPIO.output(HAWKS_F, GPIO.LOW)
	GPIO.output(HAWKS_G, GPIO.LOW)


def write2():
	GPIO.output(HAWKS_A, GPIO.HIGH)
	GPIO.output(HAWKS_B, GPIO.HIGH)
	GPIO.output(HAWKS_C, GPIO.LOW)
	GPIO.output(HAWKS_D, GPIO.HIGH)
	GPIO.output(HAWKS_E, GPIO.HIGH)
	GPIO.output(HAWKS_F, GPIO.LOW)
	GPIO.output(HAWKS_G, GPIO.HIGH)


def write3():
	GPIO.output(HAWKS_A, GPIO.HIGH)
	GPIO.output(HAWKS_B, GPIO.HIGH)
	GPIO.output(HAWKS_C, GPIO.HIGH)
	GPIO.output(HAWKS_D, GPIO.HIGH)
	GPIO.output(HAWKS_E, GPIO.LOW)
	GPIO.output(HAWKS_F, GPIO.LOW)
	GPIO.output(HAWKS_G, GPIO.HIGH)


def write4():
	GPIO.output(HAWKS_A, GPIO.LOW)
	GPIO.output(HAWKS_B, GPIO.HIGH)
	GPIO.output(HAWKS_C, GPIO.HIGH)
	GPIO.output(HAWKS_D, GPIO.LOW)
	GPIO.output(HAWKS_E, GPIO.LOW)
	GPIO.output(HAWKS_F, GPIO.HIGH)
	GPIO.output(HAWKS_G, GPIO.HIGH)


def write5():
	GPIO.output(HAWKS_A, GPIO.HIGH)
	GPIO.output(HAWKS_B, GPIO.LOW)
	GPIO.output(HAWKS_C, GPIO.HIGH)
	GPIO.output(HAWKS_D, GPIO.HIGH)
	GPIO.output(HAWKS_E, GPIO.LOW)
	GPIO.output(HAWKS_F, GPIO.HIGH)
	GPIO.output(HAWKS_G, GPIO.HIGH)


def write6():
	GPIO.output(HAWKS_A, GPIO.HIGH)
	GPIO.output(HAWKS_B, GPIO.LOW)
	GPIO.output(HAWKS_C, GPIO.HIGH)
	GPIO.output(HAWKS_D, GPIO.HIGH)
	GPIO.output(HAWKS_E, GPIO.HIGH)
	GPIO.output(HAWKS_F, GPIO.HIGH)
	GPIO.output(HAWKS_G, GPIO.HIGH)


def write7():
	GPIO.output(HAWKS_A, GPIO.HIGH)
	GPIO.output(HAWKS_B, GPIO.HIGH)
	GPIO.output(HAWKS_C, GPIO.HIGH)
	GPIO.output(HAWKS_D, GPIO.LOW)
	GPIO.output(HAWKS_E, GPIO.LOW)
	GPIO.output(HAWKS_F, GPIO.LOW)
	GPIO.output(HAWKS_G, GPIO.LOW)


def write8():
	GPIO.output(HAWKS_A, GPIO.HIGH)
	GPIO.output(HAWKS_B, GPIO.HIGH)
	GPIO.output(HAWKS_C, GPIO.HIGH)
	GPIO.output(HAWKS_D, GPIO.HIGH)
	GPIO.output(HAWKS_E, GPIO.HIGH)
	GPIO.output(HAWKS_F, GPIO.HIGH)
	GPIO.output(HAWKS_G, GPIO.HIGH)


def write9():
	GPIO.output(HAWKS_A, GPIO.HIGH)
	GPIO.output(HAWKS_B, GPIO.HIGH)
	GPIO.output(HAWKS_C, GPIO.HIGH)
	GPIO.output(HAWKS_D, GPIO.LOW)
	GPIO.output(HAWKS_E, GPIO.LOW)
	GPIO.output(HAWKS_F, GPIO.HIGH)
	GPIO.output(HAWKS_G, GPIO.HIGH)


def write0_OPP():
	GPIO.output(OPPOSITION_A, GPIO.HIGH)
	GPIO.output(OPPOSITION_B, GPIO.HIGH)
	GPIO.output(OPPOSITION_C, GPIO.HIGH)
	GPIO.output(OPPOSITION_D, GPIO.HIGH)
	GPIO.output(OPPOSITION_E, GPIO.HIGH)
	GPIO.output(OPPOSITION_F, GPIO.HIGH)
	GPIO.output(OPPOSITION_G, GPIO.LOW)


def write1_OPP():
	GPIO.output(OPPOSITION_A, GPIO.LOW)
	GPIO.output(OPPOSITION_B, GPIO.HIGH)
	GPIO.output(OPPOSITION_C, GPIO.HIGH)
	GPIO.output(OPPOSITION_D, GPIO.LOW)
	GPIO.output(OPPOSITION_E, GPIO.LOW)
	GPIO.output(OPPOSITION_F, GPIO.LOW)
	GPIO.output(OPPOSITION_G, GPIO.LOW)


def write2_OPP():
	GPIO.output(OPPOSITION_A, GPIO.HIGH)
	GPIO.output(OPPOSITION_B, GPIO.HIGH)
	GPIO.output(OPPOSITION_C, GPIO.LOW)
	GPIO.output(OPPOSITION_D, GPIO.HIGH)
	GPIO.output(OPPOSITION_E, GPIO.HIGH)
	GPIO.output(OPPOSITION_F, GPIO.LOW)
	GPIO.output(OPPOSITION_G, GPIO.HIGH)


def write3_OPP():
	GPIO.output(OPPOSITION_A, GPIO.HIGH)
	GPIO.output(OPPOSITION_B, GPIO.HIGH)
	GPIO.output(OPPOSITION_C, GPIO.HIGH)
	GPIO.output(OPPOSITION_D, GPIO.HIGH)
	GPIO.output(OPPOSITION_E, GPIO.LOW)
	GPIO.output(OPPOSITION_F, GPIO.LOW)
	GPIO.output(OPPOSITION_G, GPIO.HIGH)


def write4_OPP():
	GPIO.output(OPPOSITION_A, GPIO.LOW)
	GPIO.output(OPPOSITION_B, GPIO.HIGH)
	GPIO.output(OPPOSITION_C, GPIO.HIGH)
	GPIO.output(OPPOSITION_D, GPIO.LOW)
	GPIO.output(OPPOSITION_E, GPIO.LOW)
	GPIO.output(OPPOSITION_F, GPIO.HIGH)
	GPIO.output(OPPOSITION_G, GPIO.HIGH)


def write5_OPP():
	GPIO.output(OPPOSITION_A, GPIO.HIGH)
	GPIO.output(OPPOSITION_B, GPIO.LOW)
	GPIO.output(OPPOSITION_C, GPIO.HIGH)
	GPIO.output(OPPOSITION_D, GPIO.HIGH)
	GPIO.output(OPPOSITION_E, GPIO.LOW)
	GPIO.output(OPPOSITION_F, GPIO.HIGH)
	GPIO.output(OPPOSITION_G, GPIO.HIGH)


def write6_OPP():
	GPIO.output(OPPOSITION_A, GPIO.HIGH)
	GPIO.output(OPPOSITION_B, GPIO.LOW)
	GPIO.output(OPPOSITION_C, GPIO.HIGH)
	GPIO.output(OPPOSITION_D, GPIO.HIGH)
	GPIO.output(OPPOSITION_E, GPIO.HIGH)
	GPIO.output(OPPOSITION_F, GPIO.HIGH)
	GPIO.output(OPPOSITION_G, GPIO.HIGH)


def write7_OPP():
	GPIO.output(OPPOSITION_A, GPIO.HIGH)
	GPIO.output(OPPOSITION_B, GPIO.HIGH)
	GPIO.output(OPPOSITION_C, GPIO.HIGH)
	GPIO.output(OPPOSITION_D, GPIO.LOW)
	GPIO.output(OPPOSITION_E, GPIO.LOW)
	GPIO.output(OPPOSITION_F, GPIO.LOW)
	GPIO.output(OPPOSITION_G, GPIO.LOW)


def write8_OPP():
	GPIO.output(OPPOSITION_A, GPIO.HIGH)
	GPIO.output(OPPOSITION_B, GPIO.HIGH)
	GPIO.output(OPPOSITION_C, GPIO.HIGH)
	GPIO.output(OPPOSITION_D, GPIO.HIGH)
	GPIO.output(OPPOSITION_E, GPIO.HIGH)
	GPIO.output(OPPOSITION_F, GPIO.HIGH)
	GPIO.output(OPPOSITION_G, GPIO.HIGH)


def write9_OPP():
	GPIO.output(OPPOSITION_A, GPIO.HIGH)
	GPIO.output(OPPOSITION_B, GPIO.HIGH)
	GPIO.output(OPPOSITION_C, GPIO.HIGH)
	GPIO.output(OPPOSITION_D, GPIO.LOW)
	GPIO.output(OPPOSITION_E, GPIO.LOW)
	GPIO.output(OPPOSITION_F, GPIO.HIGH)
	GPIO.output(OPPOSITION_G, GPIO.HIGH)


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
