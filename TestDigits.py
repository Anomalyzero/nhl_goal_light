
import random
import os
import platform
import time

if "armv" in platform.machine() :
    # import GPIO if running on RPI
    import RPi.GPIO as GPIO
else :
    # import gpio_mock if not running on RPI
    from lib import gpio_mock as GPIO


HAWKS_A=38
HAWKS_B=36
HAWKS_C=32
HAWKS_D=22
HAWKS_E=18
HAWKS_F=16
HAWKS_G=7
OPPOSITION_A=37
OPPOSITION_B=33
OPPOSITION_C=31
OPPOSITION_D=29
OPPOSITION_E=15
OPPOSITION_F=13
OPPOSITION_G=11

def setup():
    """ Function to setup raspberry pi GPIO mode and warnings. PIN 7 OUT and PIN 15 IN """

    # Setup GPIO on raspberry pi
    GPIO.setmode(GPIO.BOARD)
    GPIO.setwarnings(False)
    GPIO.setup(7, GPIO.OUT, initial=GPIO.LOW) # Tell the program you want to use pin number 7 as output. Relay is ACTIVE LOW, so OFF is HIGH
    #GPIO.setup(15, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)  # Set GPIO 15 as a PULL DOWN switch
    #GPIO.add_event_detect(15, GPIO.RISING, activate_goal_light, 5000)
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


def shutdownScoreboard():
	GPIO.output(HAWKS_A, GPIO.LOW)
	GPIO.output(HAWKS_B, GPIO.LOW)
	GPIO.output(HAWKS_C, GPIO.LOW)
	GPIO.output(HAWKS_D, GPIO.LOW)
	GPIO.output(HAWKS_E, GPIO.LOW)
	GPIO.output(HAWKS_F, GPIO.LOW)
	GPIO.output(HAWKS_G, GPIO.LOW)
	GPIO.output(OPPOSITION_A, GPIO.LOW)
	GPIO.output(OPPOSITION_B, GPIO.LOW)
	GPIO.output(OPPOSITION_C, GPIO.LOW)
	GPIO.output(OPPOSITION_D, GPIO.LOW)
	GPIO.output(OPPOSITION_E, GPIO.LOW)
	GPIO.output(OPPOSITION_F, GPIO.LOW)
	GPIO.output(OPPOSITION_G, GPIO.LOW)


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


	
print("Testing Scoreboard Digits...")
setup()
print("0")
write0_OPP()
write0()
time.sleep(1)
print("1")
write1_OPP()
write1()
time.sleep(1)
print("2")
write2_OPP()
write2()
time.sleep(1)
print("3")
write3_OPP()
write3()
time.sleep(1)
print("4")
write4_OPP()
write4()
time.sleep(1)
print("5")
write5_OPP()
write5()
time.sleep(1)
print("6")
write6_OPP()
write6()
time.sleep(1)
print("7")
write7_OPP()
write7()
time.sleep(1)
print("8")
write8_OPP()
write8()
time.sleep(1)
print("9")
write9_OPP()
write9()
time.sleep(1)
print("Testing finished")
shutdownScoreboard()
